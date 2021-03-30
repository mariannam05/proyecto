#api
import requests
url = "https://api-escapamet.vercel.app/"
response = requests.get(url)
info_rooms = response.json() #lista de diccionarios

