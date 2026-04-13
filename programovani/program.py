import csv

def zpracuj_csv(filename):

    objednavky = {}

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for radek in reader:
            try:
                cislo = radek['cislo_objednavky']
                
                if cislo not in objednavky:
                    objednavky[cislo] = {
                        "cislo": cislo,
                        "zakaznik": radek['zakaznik'],
                        "zaplaceno": radek['zaplaceno'].lower() == 'true',
                        "polozky": []
                    }
                
                mnozstvi = int(radek['mnozstvi'])
                cena = float(radek['cena_za_kus'])
                nazev = radek['nazev_polozky']

                if nazev != "" and mnozstvi > 0 and cena > 0:
                    objednavky[cislo]["polozky"].append({
                        "m": mnozstvi,
                        "c": cena
                    })
            
            except:
                continue

    vysledek = []

    for id_obj in objednavky:
        o = objednavky[id_obj]
        if o["zaplaceno"] == True and len(o["polozky"]) > 0:
            
            celkova_cena = 0
            celkove_kusu = 0

            for p in o["polozky"]:
                celkova_cena += p["m"] * p["c"]
                celkove_kusu += p["m"]
            
            vysledek.append({
                "cislo": int(o["cislo"]),
                "zakaznik": o["zakaznik"],
                "celkem": int(celkova_cena),
                "pocet_polozek": int(celkove_kusu)
            })

    vysledek.sort(key=lambda x: (-x["celkem"], -x["pocet_polozek"], x["cislo"]))

    return vysledek

zpracovane = zpracuj_csv("complex.csv")

for poradi, o in enumerate(zpracovane, start=1):

  print(

      f"{poradi}. Objednávka {o['cislo']} – {o['zakaznik']} – "

      f"Položek: {o['pocet_polozek']} – Celkem: {o['celkem']} Kč"

  )
        
        
