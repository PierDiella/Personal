import requests
from bs4 import BeautifulSoup
import os

# Funzione per il download del file
def download_file(url, directory):
    filename = os.path.join(directory, url.split("/")[-1])
    with open(filename, 'wb') as f:
        response = requests.get(url)
        f.write(response.content)

# URL del sito da cui vuoi recuperare i PDF
url = 'https://www.eolo.it/home/pagine-legali/documentazione-economica.html'

# Esegui una richiesta GET alla pagina web
response = requests.get(url)

# Analizza il contenuto HTML della pagina con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Trova tutti i link sulla pagina
links = soup.find_all('a')

# Crea una cartella per salvare i file PDF, se non esiste già
directory = 'pdfs'
if not os.path.exists(directory):
    os.makedirs(directory)

# Ciclo attraverso tutti i link per trovare quelli che terminano con '.pdf'
for link in links:
    href = link.get('href')
    if href and href.endswith('.pdf'):
        # Se il link termina con '.pdf', scarica il file
        download_file(href, directory)
        print("File scaricato:", href)



for link in links:
    href = link.get('href')
    if href and href.endswith('.pdf'):
        print("Link PDF trovato:", href)
        try:
            download_file(href, directory)
            print("File scaricato:", href)
        except Exception as e:
            print("Errore durante il download:", e)
