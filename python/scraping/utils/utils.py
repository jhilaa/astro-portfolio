import requests
from bs4 import BeautifulSoup
import csv

def get_soup(url: str) -> BeautifulSoup:
    resp = requests.get(url)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")

# Récupère les éléments correspondant à element_selector compris entre start_selector et end_selector.
def get_between(soup, start_selector: str, end_selector: str, element_selector: str):
    start = soup.select_one(start_selector)
    end = soup.select_one(end_selector)
    if not start or not end:
        return []
    results = []
    for el in start.find_all_next():
        if el == end:
            break
        # récupérer directement les éléments qui matchent
        if el.name == element_selector or el.select_one(element_selector):
            # si c'est exactement le bon type
            if el.name == element_selector:
                results.append(el)
            else:
                results.extend(el.select(element_selector))
    return results

# Retourne la <table> dont la première balise <th> contient le texte donné.
def get_table_by_first_th(soup: BeautifulSoup, text: str):
    result = None
    for table in soup.find_all("table"):
        first_th = table.find("th")
        if first_th and first_th.get_text(strip=True) == text:
            result = table
            break   # on s’arrête dès qu’on a trouvé
    return result


# export en csv "brut"
def export_csv(filename: str, data: list[list], delimiter=";"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerows(data)
        
