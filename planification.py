# on importe nos packages 

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 



class Planification: 

	def __init__(self, chemin_du_csv):
		self.chemin_du_csv = chemin_du_csv
		self.df_reseau = pd.read_csv(chemin_du_csv)
		print(self.df_reseau.head())

	def data_preparation(self):
		pass


		