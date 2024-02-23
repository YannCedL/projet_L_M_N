import pandas as pd
df=pd.read_csv("reseau_en_arbre.csv")
print(df)

infras=df.groupby('infra_id')
df["nb_maison_total"]=infras["nb_maisons"].transform('sum')
df["diff_infra"]=df["longueur"]/df["nb_maison_total"]
df.loc[df['infra_type'] == 'infra_intacte', 'diff_infra'] =0 
print(df)

bats=df.groupby('id_batiment')
df["diff_bat"]=bats["diff_infra"].transform('sum')
print(df)
df_bat_diff=df[['id_batiment','diff_bat']]
df_bat_diff=df_bat_diff.drop_duplicates()
df_bat_diff=df_bat_diff.sort_values(by='diff_bat')
df_bat_diff=df_bat_diff[df_bat_diff['diff_bat']>0]
print(df_bat_diff)

# print(df)