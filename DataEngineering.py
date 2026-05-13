import pandas as pd
df = pd.read_csv("data.csv")
df = df.dropna()
df = df.drop_duplicates()