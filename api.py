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
nombre_quizizz = banco1_dic['name']
juego_quizizz = banco1_dic['game']
posicion_quizizz = banco1_dic['position']

#juego de logica booleana en pasillo laboratorio
nombre_booleana = puerta_lab_dic['name']
juego_booleana = puerta_lab_dic['game']
posicion_booleana = puerta_lab_dic['position']

#juego adivinanzas en laboratorio en computadora 2
nombre_adivinanzas = comp2_dic['name']
juego_adivinanzas = comp2_dic['game']
posicion_adivinanzas = comp2_dic['position']

#juego ahorcado en Biblioteca en mueble de libros
nombre_ahorcado = mueble_libros_dic['name']
juego_ahorcado = mueble_libros_dic['game']
posicion_ahorcado = mueble_libros_dic['position']

#juego de logica con dibujos en Plaza rectorado en Saman (Centro)
nombre_dibujos = saman_dic['name']
juego_dibujos = saman_dic['game']
posicion_dibujos = saman_dic['position']

#juego de criptograma en Biblioteca Mueble pequeño 
nombre_criptograma = mueble_pequeño_dic['name']
juego_criptograma = mueble_pequeño_dic['game']
posicion_criptograma = mueble_pequeño_dic['position']

#juego de preguntas de python en Laboratorio computadora 1
nombre_python = comp1_dic['name']
juego_python = comp1_dic['game']
posicion_python = comp1_dic['position']

#juego de sopa de letras en Laboratorio pizarra
nombre_sopa = pizarra_dic['name']
juego_sopa = pizarra_dic['game']
posicion_sopa = pizarra_dic['position']


#juego numeros en Servidores papelera
nombre_num = papelera_dic['name']
juego_numeros = papelera_dic['game']
posicion_num = papelera_dic['position']

#juego numeros en Servidores Rack
nombre_mezclada = rack_dic['name']
juego_mezclada = rack_dic['game']
posicion_mezclada = rack_dic['position']

#juego adivina la pelicula en servidores final 
juego_final = puerta_serv_dic['game']
nombre_final = puerta_serv_dic['name']
posicion_final = puerta_serv_dic['position']

#juego matematica en Biblioteca mueble de sentarse 
juego_mate = mueble_sentarse_dic['game']
nombre_mate = mueble_sentarse_dic['name']
posicion_mate = mueble_sentarse_dic['position']