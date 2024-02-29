import pandas as pd
from classes.batiment import Batiment 
from classes.infrastructure import Infrastructure
from classes.dataframe import Dataset
# Utilisation des classes
dataset = Dataset("reseau_en_arbre.csv")
infra = Infrastructure(dataset)
bat = Batiment(dataset)

infra.sum_maisons_par_infra()
infra.calcul_diff_infra()
bat.sum_diff_infra_par_batiment()
print(dataset.get_df_bat_diff())
