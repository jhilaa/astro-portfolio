import csv
from bs4 import BeautifulSoup
from scraping.utils import utils


def planets_data_to_csv(soup: BeautifulSoup): 
# traitement des données
    ref = soup.find("span", {"id": "Liste_des_planètes"})
    table = ref.find_parent("h2").find_next("table")
    table_rows = table.find_all("tr")

    rows = []
    for tr in table_rows:
        data = []
        table_data = tr.find_all(["th", "td"])
        for th_td in table_data:
            text = th_td.get_text(separator="<br>", strip=True)
            if text:
                data.append(text)
        if (len(data) > 0):
            rows.append(data)
        
    # Export en CSV
    print (rows)
    utils.export_csv(r"scraping\data\planets.csv", rows, ";")


print("✅ Scraping terminé, fichier planets.csv généré")

