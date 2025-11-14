from scraping.utils import utils

BASE_URL = "https://astroneer.fandom.com"


# Parsing avec BeautifulSoup
soup = utils.get_soup(BASE_URL)

# --- Extraction ---
def extract_resource_urls(list_resources_url: str) -> list[str]:
    """Récupère toutes les URLs des ressources depuis une page de catégorie."""
    soup = utils.get_soup(list_resources_url)
    return [BASE_URL + a["href"] for a in soup.select(".mw-category-group li a[href]")]

def extract_resource_data(resource_detail_url: str) -> list:
    """Récupère les infos principales d'une ressource (titre, image, etc.)."""
    soup = utils.get_soup(resource_detail_url)

    # 1. Titre
    infoboxtable = soup.select_one("table.infoboxtable")
    title = infoboxtable.select_one(".infoboxname").get_text(strip=True) if infoboxtable else None
    # 2. Miniature
    image = soup.select_one('span[typeof="mw:File"] img')
    image_src = image["src"] if image else None
    # 3. Image
    miniature = soup.select_one(".mw-file-description.image img")   
    miniature_src = miniature.get("data-src") if miniature else None

    print("url:", resource_detail_url)
    print("title:", title)
    print("image_src:", image_src)
    print("miniature_src:", miniature_src)
    
    return [title, image_src, miniature_src]       

# --- Orchestration ---
def main():
    print("✅ Lancement du scraping")
    list_resources_url = BASE_URL + "/fr/wiki/Catégorie:Ressources"
    
    # 1. Extraction de toutes les URLs de ressources
    urls = extract_resource_urls(list_resources_url)
    print(f"➡️ {len(urls)} ressources trouvées")

    # 2. Extraction de données de chaque ressource
    resources = []
    for url in urls:
        data = extract_resource_data(url)
        resources.append(data)
        # print(f"✔️ {data['title']}")

    # 3. Export CSV
    utils.export_csv(r"scraping\data\resources.csv", resources, ";")
    
    print("✅ Scraping terminé, fichier resources.csv généré")

if __name__ == "__main__":
    main()
