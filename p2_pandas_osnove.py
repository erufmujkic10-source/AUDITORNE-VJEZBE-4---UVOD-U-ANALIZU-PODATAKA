import os
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.widht",120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER,"studenti.csv")

df = pd.read_csv(FAJL)

print("Prva 3 reda: ")
print(df.head(3))

print("\nZadnja 2 reda: ")
print(df.tail(2))


print("\nDimenzije (redovi, kolone):", df.shape)
print("Kolone:", list(df.columns))
print("\nTipovi kolona:")
print(df.dtypes)   

