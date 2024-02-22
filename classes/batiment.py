from .infrastructure import *
class Batiment:
  def __init__(self,id_batiment):
    self.id_bat=id_batiment
  
  def diff_batiment(reseau):
    bats=reseau.groupby('id_batiment')
    return bats["diff_infra"].transform('sum')
  

