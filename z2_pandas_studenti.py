import os 
import pandas as pd

pd.set_option("display.max_columns",None)
pd.set_option("display.width",120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER,"studenti.csv")

# a) TODO: učitaj podatke i ispiši shape i head()
df = pd.read_csv(FAJL,encoding="utf-8")

print(df.head(5))

print(df.shape)

# b) TODO: kolona prosjek

df["prosjek"] = (df["matematika"] + df["programiranje"] + df["statistika"]) / 3
print("\nNova kolona prosjek:")
print(df[["ime", "prosjek"]].head(3).round(2))

# c) TODO: top 5

print("\nTop 5 po prosjeku:")
top5 = df.sort_values("prosjek", ascending=False, kind="stable").head(5)
print(top5[["ime", "smjer", "prosjek"]].round(2))

# d) TODO: value_counts

print("\nBroj studenata po smjeru:")
print(df["smjer"].value_counts())

# e) TODO: groupby

print("\nProsjek po smjeru:")
print(df.groupby("smjer")["prosjek"].mean().round(2).sort_values(ascending=False))


# f) TODO: filtriranje prisustva


slabo_prisustvo = df[df["prisustvo"] < 70]
print("\nStudenti sa prisustvom ispod 70%:", len(slabo_prisustvo))
print(slabo_prisustvo[["ime", "prisustvo"]])