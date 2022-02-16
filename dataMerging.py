import pandas as pd

df = pd.read_csv("dwarf_stars.csv")

df = df.dropna()
#print(df)

df["Radius"] = 0.102763*df["Radius"]
#print(df)

df["Mass"] = 0.000954588*df["Radius"]
#print(df)

df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)

#df.to_csv("unit_converted_stars.csv")