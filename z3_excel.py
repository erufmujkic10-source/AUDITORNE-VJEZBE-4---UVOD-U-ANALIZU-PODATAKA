import os
import pandas as pd
import csv




pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
EXCEL = os.path.join(FOLDER, "studenti.xlsx")
IZLAZ_XLSX = os.path.join(FOLDER, "rezultati.xlsx")
IZLAZ_CSV = os.path.join(FOLDER, "rezultati.csv")


# a) TODO: učitaj Grupa_A i Grupa_B


grupa_a = pd.read_excel(EXCEL, sheet_name="Grupa_A")
print("Grupa A:", grupa_a.shape)
print(grupa_a.head(3))

grupa_b = pd.read_excel(EXCEL, sheet_name="Grupa_B")
print("Grupa B:", grupa_b.shape)
print(grupa_b.head(3))

# b) TODO: kolona "grupa"a

svi_sheetovi = pd.read_excel(EXCEL, sheet_name=None)
svi = pd.concat(svi_sheetovi, names=["grupa", None]).reset_index(level="grupa")
print(svi.head())


# c) TODO: concat

svi = pd.concat([svi_sheetovi["Grupa_A"], svi_sheetovi["Grupa_B"]], ignore_index=True)
print("Nakon concat:", svi.shape)          # (40, 7)
print(svi.tail(3))

# d) TODO: prosjek i polozio
svi["prosjek"] = ((svi["matematika"] + svi["programiranje"] + svi["statistika"]) / 3).round(2)
svi["polozio"] = (svi["matematika"] > 1) & (svi["programiranje"] > 1) & (svi["statistika"] > 1)
print(svi[["matematika", "programiranje", "statistika", "prosjek", "polozio"]].head())




# e) TODO: ExcelWriter sa dva sheeta


IZLAZ_DVA_SHEETA = os.path.join(FOLDER, "studenti_izvjestaj.xlsx")

with pd.ExcelWriter(IZLAZ_DVA_SHEETA) as writer:
    svi_sheetovi["Grupa_A"].to_excel(writer, sheet_name="Grupa_A", index=False)
    svi_sheetovi["Grupa_B"].to_excel(writer, sheet_name="Grupa_B", index=False)

print("Excel fajl sa dva sheeta je uspješno kreiran!")

