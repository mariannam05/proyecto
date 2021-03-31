
from time import *


playtime = set_time()

tiempo_limite = playtime * 60
comenzar_tiempo = time.time() #para comenzar el tiempo
fin_tiempo = comenzar_tiempo + tiempo_limite

print(tiempo_limite)