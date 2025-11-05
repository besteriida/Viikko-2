"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime
def main():
    varaukset = "varaukset.txt" # Täällä on varauksia
    nimet = [
        "Varausnumero", "Varaaja", "Päivämäärä", "Aloitusaika", "Tuntimäärä",
        "Tuntihinta", "Kokonaishinta", "Maksettu", "Kohde", "Puhelin", "Sähköposti"
    ] # Tässä kerrotaan mitä tietoja tulostetaan

    with open(varaukset, "r", encoding="utf-8") as f:
        for rivi in f:
            varaus = rivi.strip().split("|")
            paivamaara = datetime.strptime(varaus[2], "%Y-%m-%d").date()
            aloitusaika = datetime.strptime(varaus[3], "%H:%M").time()
            tuntimaara = int(varaus[4])
            tuntihinta = float(varaus[5])
            kokonaishinta = tuntihinta * tuntimaara
            maksettu = "Kyllä" if varaus[6].strip() == "True" else "Ei"

            arvot = [
                varaus[0], varaus[1], paivamaara, aloitusaika, varaus[4],
                f"{tuntihinta:.2f} €", f"{kokonaishinta:.2f} €", maksettu,
                varaus[7], varaus[8], varaus[9]]
            for nimi, arvo in zip(nimet, arvot):
                print(f"{nimi}: {arvo}")
            print("")  # tyhjä rivi väliin
if __name__ == "__main__":
    main()