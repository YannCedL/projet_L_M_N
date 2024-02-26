from packages.infra import Infra

#Création de la classe Batiment
class Batiment:
    def __init__(self, id_building, list_infras) -> None:
        self.id_building = id_building
        self.building_diff = 0
        if type(list_infras) == Infra: 
            self.list_infras = list_infras

    #Cette méthode permet de calculer la difficulté d'un batiment en sommant les difficultés de ces infra
    def get_building_difficulty(self) -> float:
        self.building_diff = sum(self.list_infras)
        return self.building_diff
    
    # Cette méthode permet de comparer la difficulté entre 02 batiments
    def __lt__(self, other_object):
        return self.building_diff < other_object.building_diff 
    