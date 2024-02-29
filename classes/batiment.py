import pandas as pd

class Batiment:
    def __init__(self, dataset):
        self.dataset = dataset

    def sum_diff_infra_par_batiment(self):
        bats = self.dataset.df.groupby('id_batiment')
        self.dataset.df["diff_bat"] = bats["diff_infra"].transform('sum')
