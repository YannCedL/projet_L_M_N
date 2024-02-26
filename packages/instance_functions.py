from packages.infra import Infra

#Cette fonction permet de créer une liste d'objets de type Infra à partir des données du Dataframe
def infra_list(df) -> list:
    return list(map(lambda row: Infra(infra_id=row[1], nb_houses=row[2], infra_type=row[3], length=row[4]), df.values.tolist()))