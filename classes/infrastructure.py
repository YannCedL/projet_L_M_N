import pandas as pd

class Infrastructure:
    def __init__(self, dataset):
        self.dataset = dataset

    def sum_maisons_par_infra(self):
        infras = self.dataset.df.groupby('infra_id')
        self.dataset.df["nb_maison_total"] = infras["nb_maisons"].transform('sum')

    def calcul_diff_infra(self):
        self.dataset.df["diff_infra"] = self.dataset.df["longueur"] / self.dataset.df["nb_maison_total"]
        self.dataset.df.loc[self.dataset.df['infra_type'] == 'infra_intacte', 'diff_infra'] = 0
