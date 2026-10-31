import os
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER, "narudzbe.csv")
DANI = ["Pon", "Uto", "Sri", "Čet", "Pet", "Sub", "Ned"]

df = pd.read_csv(os.path.join(FOLDER, "narudzbe.csv"))


# a) TODO: učitaj i pogledaj kolone

print(df.columns)
print("Dimenzije: ",df.shape)

# b) TODO: čišćenje

df["iznos"] = pd.to_numeric(df["iznos"], errors="coerce")
df["datum_vrijeme"] = pd.to_datetime(df["datum_vrijeme"], errors="coerce")


# c) TODO: izvedene kolone sat, dan, mjesec

df["sat"] = df["datum_vrijeme"].dt.hour
df["mjesec"] = df["datum_vrijeme"].dt.month
df["dan"] = df["datum_vrijeme"].dt.dayofweek
print("\nPrva 3 reda:")
print(df[["sat", "mjesec", "dan"]].head(3))

# d) TODO: top 5 gradova + grafikon

top_5_gradova = df["grad"].value_counts().head(5)
print("\nTop 5 gradova po broju narudžbi:")
print(top_5_gradova)

top_5_gradova.plot(kind="bar", color="#E07A5F", figsize=(8, 4))
plt.title("Top 5 gradova po broju narudžbi")
plt.xlabel("Grad")
plt.ylabel("Broj narudžbi")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)


SLIKA_GRAD = os.path.join(FOLDER, "top_gradovi_grafikon.png")
plt.savefig(SLIKA_GRAD, dpi=120, bbox_inches="tight")
print("\nGrafikon sačuvan kao:", SLIKA_GRAD)
plt.show()


# e) TODO: narudžbe po satu + grafikon


narudzbe_po_satu = df["sat"].value_counts().sort_index()
print("\nNarudžbe po satu:")
print(narudzbe_po_satu)

narudzbe_po_satu.plot(kind="bar", color="#3A7CA5", figsize=(10, 5))
plt.title("Broj narudžbi po satu u danu")
plt.xlabel("Sat")
plt.ylabel("Broj narudžbi")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)

SLIKA_SAT = os.path.join(FOLDER, "narudzbe_po_satu_grafikon.png")
plt.savefig(SLIKA_SAT, dpi=120, bbox_inches="tight")
print("\nGrafikon sačuvan kao:", SLIKA_SAT)
plt.show()

# f) TODO: prosječan iznos po kategoriji


prosjek_po_kategoriji = df.groupby("kategorija")["iznos"].mean().round(2)

print("\nProsječan iznos po kategoriji:")
print(prosjek_po_kategoriji)

prosjek_po_kategoriji.plot(kind="bar", color="#81B29A", figsize=(8, 4))
plt.title("Prosječan iznos narudžbe po kategoriji")
plt.xlabel("Kategorija")
plt.ylabel("Prosječan iznos")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

SLIKA_KAT = os.path.join(FOLDER, "prosjek_kategorija_grafikon.png")
plt.savefig(SLIKA_KAT, dpi=120, bbox_inches="tight")
print("\nGrafikon sačuvan kao:", SLIKA_KAT)
plt.show()