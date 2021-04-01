#api
import requests
url = "https://api-escapamet.vercel.app/"
response = requests.get(url)
info_rooms = response.json() #lista de diccionarios #objetos de la api

#diccionario para cada cuarto
lab_dic = info_rooms[0]
biblioteca_dic = info_rooms[1]
plaza_dic = info_rooms[2]
pasillo_dic = info_rooms[3]
servidores_dic = info_rooms[4]

#objetos laboratorio
pizarra_dic = lab_dic['objects'][0]
comp1_dic = lab_dic['objects'][1]
comp2_dic = lab_dic['objects'][2]

#objetos biblioteca
mueble_libros_dic = biblioteca_dic['objects'][0]
mueble_sentarse_dic = biblioteca_dic['objects'][1]
mueble_pequeño_dic = biblioteca_dic['objects'][2]

#objetos Plaza rectorado
saman_dic = plaza_dic['objects'][0]
banco1_dic = plaza_dic['objects'][1]
banco2_dic = plaza_dic['objects'][2]

#objetos Cuarto de servidores
puerta_serv_dic=servidores_dic['objects'][0]
rack_dic = servidores_dic['objects'][1]
papelera_dic = servidores_dic['objects'][2]

#objeto pasillo de laboratorio
puerta_lab_dic = pasillo_dic['objects'][0]


#juego quizizz en banco 1 a la izquierda del saman 
juego_quizizz = banco1_dic['game']

#juego de logica booleana en pasillo laboratorio
juego_booleana = puerta_lab_dic['game']

#juego adivinanzas en laboratorio en computadora 2
juego_adivinanzas = comp2_dic['game']

#juego ahorcado en Biblioteca en mueble de libros
juego_ahorcado = mueble_libros_dic['game']

#juego de logica con dibujos en Plaza rectorado en Saman (Centro)
juego_dibujos = saman_dic['game']

#juego de criptograma en Biblioteca Mueble pequeño 
juego_criptograma = mueble_pequeño_dic['game']





