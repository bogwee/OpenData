import pandas as pd
from bulk_geocoding import geocode
from pyproj import Transformer
from sklearn.metrics import pairwise_distances

#code git pour geocode l le dataframe et n le nombre de rows en paquets
def chunks(l, n):
    """ Yield successive n-sized chunks from l. """
    for i in range(0, len(l), n):
        yield l.iloc[i:i + n]



dpe=pd.read_excel("OpenData/data_sets/dpe03existant.xlsx")
real=pd.read_csv("OpenData/data_sets/consommation-annuelle-residentielle-par-adresse.csv",sep=";",encoding="utf-8",nrows=1000)
real_copy=real.copy()
geocoded = []
chunk_size = 10
for chunk in chunks(real_copy, chunk_size):
  chunk_dict=chunk.to_dict(orient="records")
  r = geocode(data=chunk_dict,columns=["Adresse"],citycode="Code Commune")
  geocoded.extend(r)

geocoded=pd.DataFrame(geocoded)
real["Code Commune"] = real["Code Commune"].astype(str) #str par ce que si en int 0123 devient 123
geocoded["Code Commune"] = geocoded["Code Commune"].astype(str)
real_prime=real.merge(geocoded[["Adresse", "Code Commune","longitude","latitude"]],on=["Adresse","Code Commune"],how="left")
# --- Convert lon/lat (EPSG:4326) -> Lambert-93 (EPSG:2154) ---
to_l93 = Transformer.from_crs(4326, 2154, always_xy=True)

real_prime["longitude"], real_prime["latitude"] = to_l93.transform(
    real_prime["longitude"].values,
    real_prime["latitude"].values
)
#on eleve les na et laisse le bon index
rp_valid = real_prime.loc[real_prime[["longitude","latitude"]].notna().all(axis=1)]
dp_valid = dpe.loc[dpe[["coordonnee_cartographique_x_ban",
                        "coordonnee_cartographique_y_ban"]].notna().all(axis=1)]
#coordonnees des maisons
rp_xy = rp_valid[["longitude","latitude"]].to_numpy()
dp_xy = dp_valid[["coordonnee_cartographique_x_ban","coordonnee_cartographique_y_ban"]].to_numpy()
#construction des distances entre maison
dist_matrix = pairwise_distances(rp_xy, dp_xy, metric="euclidean")
dist_min=dist_matrix.min(axis=1) #distance minimal pour chaque maison
index_min=dist_matrix.argmin(axis=1)#index minimal pour chque maison

rp_idx=rp_valid.index.to_numpy() #les index original des maison dans real_prime
dp_idx=dp_valid.index.to_numpy() #les index original des maison dans dep
min_dist_ind=pd.DataFrame({"house_index":rp_idx,"nearest_dpe_index":dp_idx[index_min],"distance_m":dist_min}) #ici dp_idx[index_min] prend les index minimal des index originaux de dep
min_dist_ind=min_dist_ind[min_dist_ind["distance_m"]<=5].reset_index(drop=True) #matching dataframe
#now we match 
real_prime_match=real_prime.loc[min_dist_ind["house_index"]].reset_index(drop=True)
dpe_match=dpe.loc[min_dist_ind["nearest_dpe_index"]].reset_index(drop=True)
merged=pd.concat([real_prime_match,dpe_match,min_dist_ind[["distance_m"]]],axis=1)
print(merged.shape)
merged.to_excel("merged.xlsx",index=False)




