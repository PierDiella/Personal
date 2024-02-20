import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin



# Funzione per il download del file
def download_file(url, directory):
    filename = os.path.join(directory, url.split("/")[-1])
    with open(filename, 'wb') as f:
        response = requests.get(url)
        f.write(response.content)

# Funzione per l'analisi delle pagine
def analyze_page(url, directory):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    for link in links:
        href = link.get('href')
        # Se il link è interno al sito, segue quel link e analizza la pagina collegata
        if href.startswith('/') or href.startswith(url):
            # Se il link inizia con '/', lo consideriamo come relativo all'URL base
            full_url = urljoin(url, href)
            # Analizza la pagina collegata per trovare link PDF
            analyze_page(full_url, directory)
        elif href.endswith('.pdf'):
            # Se il link termina con '.pdf', scarica il file
            download_file(href, directory)
            print("File scaricato:", href)

# URL del sito da cui vuoi recuperare i PDF
url = 'https://www.nwgenergia.it/'

# Crea una cartella per salvare i file PDF, se non esiste già
directory = 'pdfs'
if not os.path.exists(directory):
    os.makedirs(directory)

# Analizza la pagina iniziale per trovare link PDF e pagine interne
analyze_page(url, directory)


response = requests.get(url, timeout=(10, 30))
