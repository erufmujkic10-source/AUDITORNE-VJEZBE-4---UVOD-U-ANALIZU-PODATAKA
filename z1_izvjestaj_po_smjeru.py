import csv
import os
FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER,"studenti.csv")

studenti = []

with open(FAJL, "r",encoding="utf-8") as f:
    citac = csv.DictReader(f)
    for red in citac:
        studenti.append(red)
print("Broj studenata: ",len(studenti))
print("Prvi student (sve je tekst): ",studenti[0])


for s in studenti:
    s["prosjek"] = (s["matematika"] + s["programiranje"] + s["statistika"])




po_smjeru = {}
for s in studenti:
    smjer=s["smjer"]
    if smjer not in po_smjeru:
        po_smjeru[smjer] = []
    po_smjeru[smjer].append(s)


najbolji = sorted(studenti, key=lambda s: s["prosjek"], reverse=True)
print("\nTop 3 studenta:")
for i, s in enumerate(najbolji[:3], start=1):
    print(f"{i}. {s['ime']} ({s['smjer']}) - {s['prosjek']}")


IZLAZ = os.path.join(FOLDER, "izvjestaj_smjerovi.csv")
with open(IZLAZ,"w",newline="",encoding="utf-8") as f:
    pisac = csv.DictWriter(f, fieldnames=["smjer","broj_studenata"])
    pisac.writeheader()
    for smjer, lista in po_smjeru.items():
        pisac.writerow({"smjer":smjer,"broj_studenata":len(lista)})
    print("\nIzvjestaj sacuvan u: ",IZLAZ)

    