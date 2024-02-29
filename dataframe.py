class DataFrameBatiments:
    def __init__(self, data):
        self.data = data

    def determiner_ordre_rehabilitation(self):
        # Trier les bâtiments par la valeur de longueur en ordre croissant
        sorted_batiments = sorted(self.data, key=lambda x: x.diff_bat)
        # Extraire les identifiants des bâtiments dans l'ordre de réhabilitation
        ordre_rehabilitation = [batiment.id_batiment for batiment in sorted_batiments]
        return ordre_rehabilitation
    
    def verif_type(self):
        self.loc[self['infra_type'] == 'infra_intacte', 'diff_bat'] =0 
  
