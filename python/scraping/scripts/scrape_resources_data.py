from scraping.utils import utils
from scraping.scripts.resources import process_natural_resources_data


# URL
URL = "https://astroneer.fandom.com/fr/wiki/Ressources"


# --- Orchestration ---
def main():
    print("✅ Lancement du script principal")
    # Parsing avec BeautifulSoup
    soup = utils.get_soup(URL)

    if soup:
        process_natural_resources_data.natural_resources_data_to_csv(soup)
        #process_resources_data.resources_by_planet_data_to_csv(soup)
        #process_resources_data.refined_resources_data_to_csv(soup)
        #process_resources_data.atmospheric_resources_data_to_csv(soup)
        #process_resources_data.composed_resources_data_to_csv(soup)
        #process_resources_data.composed_resources_data_to_csv(soup)
        #process_resources_data.other_resources_data_to_csv(soup)
        
    print("✅ Script principal terminé")

if __name__ == "__main__":
    main()
    