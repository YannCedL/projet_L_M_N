from packages.infra import Infra
from packages.batiment import Batiment


#Cette fonction permet de créer une liste d'objets de type Infra à partir des données du Dataframe
def infra_list(df) -> list:
    infra_objects = df.apply(lambda row: Infra(*row.to_list()), axis=1)
    return list(infra_objects)
    
def batiments_list(df) -> list:
    bat_objects = df.apply(lambda row: Batiment(id_building = row[0], list_infras= row[2]), axis=1)
    return list(bat_objects)