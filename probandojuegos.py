import time

# playtime = 60
# tiempo_limite = playtime * 60
# comenzar_tiempo = time.time() #para comenzar el tiempo
# # # fin_tiempo = comenzar_tiempo + tiempo_limite
# while True:
#     tiempo_past = time.time() - comenzar_tiempo
#     tiempo_restante = round((tiempo_limite - tiempo_past)/60)
#     print(f'Su tiempo es de: {tiempo_restante} minutos')



import time

def main():
    playtime = 30
    tiempo_limite = playtime * 60
    inicio_de_tiempo = time.time()
    fin_tiempo = inicio_de_tiempo + tiempo_limite

    tiempo_past = time.time() - inicio_de_tiempo
    tiempo_transcurrido = round((tiempo_limite - inicio_de_tiempo)/60)
    print ("\nTomo %d minutos." % (tiempo_transcurrido))
main()   