import requests
from bs4 import BeautifulSoup

PAGE_SOURCE = "https://fstream.info/"

try:
    r = requests.get(PAGE_SOURCE, timeout=10)
    r.raise_for_status()
except Exception as e:
    print("Erreur lors de la récupération de la page :", e)
    exit(1)

soup = BeautifulSoup(r.text, "html.parser")
balise = soup.find("a", id="mainUrl")

if balise is None:
    print("Balise <a id='mainUrl'> non trouvée.")
    exit(1)

url_actuelle = balise.get("href")
print("URL récupérée :", url_actuelle)

# === Génération du fichier HTML pour GitHub Pages ===
html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Redirection</title>
    <meta http-equiv="refresh" content="0;url={url_actuelle}">
</head>
<body>
    Redirection vers {url_actuelle}...
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html mis à jour avec :", url_actuelle)
