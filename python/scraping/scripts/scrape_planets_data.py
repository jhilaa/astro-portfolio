from bs4 import BeautifulSoup
from scraping.utils import utils
from scraping.scripts.planets import process_planets_data


# URL
URL = "https://astroneer.fandom.com/fr/wiki/Plan%C3%A8tes"


# --- Orchestration ---
def main():
    print("✅ Lancement du script principal")
    # Parsing avec BeautifulSoup
    soup = utils.get_soup(URL)

    if soup:
        process_planets_data.planets_data_to_csv(soup)
        
    print("✅ Script principal terminé")

if __name__ == "__main__":
    main()


