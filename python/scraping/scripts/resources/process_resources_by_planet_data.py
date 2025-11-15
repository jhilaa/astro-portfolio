import csv
from bs4 import BeautifulSoup
import scraping.utils.utils as utils

def resources_by_planet_data_to_csv(soup: BeautifulSoup):
    print("     ✅ Lancement du script process_resources_planet_data.py")
    # On récupére la table ciblée
    resources_by_planet_data_table = utils.get_table_by_first_th(soup, "Ressource")

    # En-tête
    data = []
    # Extraire les lignes si la table existe
    if resources_by_planet_data_table is not None:
        for tr in resources_by_planet_data_table.find_all("tr"):
            cells = tr.find_all(["th", "td"])
            row = [el.get_text(strip=True) for el in cells]
            if row:  
                data.append(row)

    # Export en CSV
    utils.export_csv(r"scraping\data\resources_by_planet.csv", data, ";")

    print("✅ Scraping terminé, fichier resources_by_planet.csv généré")

