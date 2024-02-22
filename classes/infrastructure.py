class infra:
  def __init__(self,infra_id,infra_type,longueur):
    self.id_inf=infra_id
    self.type=infra_type
    self.long=longueur
    self.nb_mais=0
 
  def total_maison(self,reseau):
    infras=reseau.groupby('infra_id')
    return infras["nb_maisons"].transform('sum')
  
  def diff_infra(reseau):
    diff=reseau["longueur"]/reseau["nb_maison_total"]
    return diff
  