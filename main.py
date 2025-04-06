import pandas as pd
# ex 1
df = pd.read_csv('clienti_leasing.csv')
columns = ["NAME_CLIENT", "DEPOSIT_AMOUNT", "PRESCORING"]

clienti_leasing_df = df[(df["VAL_CREDITS_RON"] == 0) & (df["DEPOSIT_AMOUNT"] > 150000)][columns]
clienti_leasing_df.loc[df["DEPOSIT_AMOUNT"] > 500000, "PRESCORING"] = 6
print(clienti_leasing_df)

# ex 2
import json
#deschidem fisierul clienti_daune.json
with open ('clienti_daune.json') as f:
    data=json.load(f)

# numaram cuvintele si le adaugam intr-un dictionar
dictionar = {}
for dauna in data:
    lista_cuvinte = str(dauna['Dauna']).lower().split()
    for cuvant in lista_cuvinte:
        if cuvant not in dictionar:
            dictionar[cuvant] = 1
        else:
            dictionar[cuvant] += 1
#formam lista cuvintelor si a frecventei de aparitie sortata descrescator
aparitie = []
for key, value in dictionar.items():
    if value > 1000 and key not in {"the", "and", "to", "a"}:
        aparitie.append((value, key))
aparitie.sort(reverse=True)
aparitie = pd.DataFrame(data=aparitie, columns=["Nr aparitii", "Cuvinte"])
print(aparitie)
