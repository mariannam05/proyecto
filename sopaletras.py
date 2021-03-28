# def colporfil(matriz):
#     matriz2 = []
#     for i in range(len(matriz[0])):
#         lista = []
#         for j in range(len(matriz)):
#             lista.append(matriz[j][i])
#         matriz2.append(lista)
#     return matriz2

# def matVer(matriz):
#     b = len(matriz)
#     c = 1
#     matriz2 = []
#     while b>0:
#         lista = []
#         a = 0
#         d = b - 1
#         for j in range(c):
#             lista.append(matriz[d][a])
#             d = d+1
#             a = a+1
#         matriz2.append(lista)
#         c = c+1
#         b = b-1
#     b = 0
#     e=1
#     c= c-2
#     while b <(len(matriz)-1):
#         lista=[]
#         d=0
#         a=e
#         for i in range (c):
#             lista.append(matriz[d][a])
#             d= d+1
#             a= a+1
#         matriz2.append(lista)
#         c= c-1
#         e= e+1
#         b= b+1
#     return matriz2
