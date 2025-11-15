import csv
from bs4 import BeautifulSoup
from scraping.utils import utils
import scraping.utils.utils as utils


def atmospheric_resources_data_to_csv(soup: BeautifulSoup):
    atmospheric_resources_data = utils.get_between(soup, "#Ressources_atmosphériques", "#Ressources_Composées", "dd")
  
    rows = [["title", "texte", "icon_data_src"]]  # en-tête
    data = []
    for element in natural_resources_data:
        text = element.get_text(separator="", strip=True)
        icon_data = element.select_one("a:has(img)")
        title = icon_data.get("title") if icon_data else None
        img = icon_data.select_one("img")
        icon_data_src = img.get("data-src") if img else None
        data = [title, text, icon_data_src]
        rows.append(data)

    # Export en CSV
    utils.export_csv(r"scraping\data\natural_resources.csv", rows, ";")
    
print("✅ Scraping terminé, fichier resources.csv généré")
