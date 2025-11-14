from scraping.utils import utils


planet

# Récupération des données
ref = soup.find("span", {"id": "Ressources_Naturelles"})
dl = ref.find_parent("h3").find_next("dl")
data = dl.find_all("dd")

header = ["resource", "image"]
rows = [header]
        
for row in data:
    text = row.get_text(strip=True)
    img_tag = row.find("img")
    img = img_tag.get("data-src") if img_tag else ""
    if text:
        rows.append([text, img])

# Export en CSV
utils.export_csv(r"scraping\data\natural_resources.csv", rows, ";")

print("✅ Scraping terminé, fichier resources.csv généré")

