# on importe nos packages 

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

class Planification:
    def __init__(self, chemin_du_csv):
        self.data = pd.read_csv(chemin_du_csv)

    def info(self):

   		# compter le nombre de lignes
   		print(f'\nTotal Rows: {self.data.shape[0]} \n' + '--'*10)

   		#information sur notre dataframe 

   		print(f'Data Summary\n' + '--'*10)
   		data_summary = self.data.info()

   		#regarder s'il y a des valeurs manquantes dans le dataframe
   		null_values = self.data.isnull().sum()
   		print(f'\nValeurs nulles\n' + '--'*10 + f'\n{null_values} \n \n')

   		# statistiques descriptives : 
   		describe_data = self.data.describe()
   		print(f'\nDescriptive Statistiques\n' + '--'*10 +  f'\n{describe_data} \n \n')

   		# compter le nombre de valeurs pour chaque type d'infrastructures:
   		infras_count = self.data['infra_type'].value_counts()
   		print(f'\nType infras\n' + '--'*10 + f'\n{infras_count} \n \n')

		# un petit graphique:
		print(self.data['infra_type'].value_counts().plot(kind="bar"))


    

    def plot_reseau(self):
    	plt.plot(self.data['nb_maisons'], self.data['longueur'])
    	plt.xlabel('nb_de_maisons')
    	plt.ylabel('longueur')
    	plt.title('taille des maisons selon le nombre')
    	plt.show()


    def run(self):
    	print("Statistiques descriptives:")
    	print(self.data.describe())
    	print('\n')
    	print("graphique")
    	#self.data.plot_reseau() 


