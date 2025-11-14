import csv
from bs4 import BeautifulSoup
from scraping.utils import utils

import scraping.utils.utils as utils
print("utils path:", utils.__file__)
print("has get_between:", hasattr(utils, "get_between"))


def natural_resources_data_to_csv(soup: BeautifulSoup):
    natural_resources_data = utils.get_between(soup, "#Ressources_Naturelles", "table", "dd")
  
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
    
    
def resources_by_planet_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\resources_by_planet.csv", rows, ";")
    
    
def refined_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\refined_resources.csv", rows, ";")
    
    
def atmospheric_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\atmospheric_resources.csv", rows, ";")
    
   
    
def composed_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\composed_resources.csv", rows, ";")
    
    
def other_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\other_resources.csv", rows, ";")



print("✅ Scraping terminé, fichier resources.csv généré")

