import pandas as pd

class Dataset:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def get_df_bat_diff(self):
        df_bat_diff = self.df[['id_batiment', 'diff_bat']]
        df_bat_diff = df_bat_diff.drop_duplicates()
        df_bat_diff = df_bat_diff.sort_values(by='diff_bat')
        df_bat_diff = df_bat_diff[df_bat_diff['diff_bat'] > 0]
        return df_bat_diff