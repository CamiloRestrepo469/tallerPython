# 1.Inserte valores numéricos en el siguiente vector y ordénelos de forma ascendente, descendente. Muestre el menor valor y el mayor valor.
# datos=[]
# mayor = 0
# menor = 0
# for i in range(0,4):
#     nuevoDato=int(input('Inserte valores numéricos    '  ))
#     datos.append(nuevoDato)

# print('-------------------------------------')

# # vector asendente

# datos.sort()
# print('ascendentes')
# print(datos)

# print('---------------------------------------------')

# # vector desendente
# datos.reverse()
# print('descendente')
# print(datos)

# print('---------------------------------------------')


# # mayor y menor 
# mayor = max(datos)
# menor = min(datos)

# print("este es el mayor")
# print(mayor)
# print('---------------------------------------------')

# print("este es el menor")
# print(menor)




# 2 Se tiene un vector de 20 posiciones donde se desean almacenar marcas de vehículos , y se tiene un segundo vector donde se almacenan los precios del mismo.Un cliente puede seleccionar cualquiera de las marcas que se ofrecen, deberá imprimir el valor de este.

# vehiculo=["Ford", "Volvo", "BMW","mazda","Renault","chevrolt","toyota" , "izusu", "international", "kembort", "daf", "cummis ","paccar ","yamaha " , "kinko", "nmax", "dt", "soldodas" , "kinua","duster"]
# valor=[15000,5000,258,25888888,4563,789,258456,369,147,45688888,2225888,133333,14777777,354777777,15666666,16444444,1777777777,1822222,19000000,200000000000000000]

# print("los vehiculos es incritados segun este orden")
# print("     0 = Ford  ")
# print("     1 = Volvo ")
# print("     2 = BMW ")
# print("     3 = mazda ")
# print("     4 = Renault ")
# print("     5 = chevrolet ")
# print("     6 = toyota ")
# print("     7 = izusu ")
# print("     8 = international ")
# print("     9 = kembort ")
# print("     10 = daf ")
# print("     11 = cummis ")
# print("     12 = paccar ")
# print("     13 = yamaha ")
# print("     14 = kinko ")
# print("     15 = nmax ")
# print("     16 = dt ")
# print("     17 = soldodas ")
# print("     12 = kinua ")
# print("     19 = duster ")

# brand = int(input("indique la marca por numeros del 0 AL 19  :   "))
# if (brand>19):
#     print("este numero no existe ")

# else:

#     cars = vehiculo[brand]
#     precio = valor[brand]


# print('-------------------------------------')

# print(cars, precio)



# 3.Se tiene un vector que almacenara los nombres científicos de hongos, se deberá realizar un algoritmo que permita insertar los nombres en el vector, realizar la búsqueda, realizar la consulta por nombre. Para un total de 10 muestras.

# hongo = []
# for i in range(0,5):
#     nuevoHongo=str(input('insertar los nombres de los Hongos   : '  ))
#     hongo.append(nuevoHongo)


# for i in range(0,5):
#     print(hongo[i])
#     print('-------------------------------------')


# Hongo_buscar = input('cual es el Hongo que deseas buscar  : ')
# for i in range(0,5):

#     if hongo[i]== Hongo_buscar:
#         print(hongo[i],i)
#         print("---------------------------------")

# print("---------------------------------")

# for i in range(len(hongo)):
#     print(hongo[i])



# 4.Se desea realizar un algoritmo que almacene las letras del alfabeto, y debe mostrar las posiciones de las letras donde se encuentran cuando una persona, digita un nombre o una palabra.

# import string
# def listAlphabet():
#   return list(string.ascii_lowercase)
# print(listAlphabet())
# print("------------------------------------------------------------------------------------------------------------")


# Alfabeto_Letra = input('cual es la letra del afebeto que quieres buscar   : ')
# for i in range(0,30):
#     if listAlphabet()[i]== Alfabeto_Letra:
#         print(listAlphabet()[i],i)
#         print("---------------------------------*----------------------------------------------------------")

    
# print(listAlphabet()[i],i)
# print("---------------------------------/-------------------------------------------------------------")



# for i in range(len(listAlphabet())):
#       print(i)

# print("---------------------------------+-----------------------------------------")
    

#  5.Se desea realizar un algoritmo que permita almacenar dos valores que son ingresados en código binario, y se debe de realizar la suma y la resta de estos dos valores.

# def decimal_a_binario(decimal):
#     if decimal <= 0:
#         return "0"
#     binario = ""
#     while decimal > 0:
#         residuo = int(decimal % 2)
#         decimal = int(decimal / 2)
#         binario = str(residuo) + binario
#     return binario

# def decimal_a_binario2(decimal2):
#     if decimal <= 0:
#         return "0"
#     binario2 = ""
#     while decimal2 > 0:
#         residuo2 = int(decimal2 % 2)
#         decimal2 = int(decimal2 / 2)
#         binario2 = str(residuo2) + binario2
#     return binario2


# decimal = int(input("Ingresa un número  : "))
# binario = decimal_a_binario(decimal)

# decimal2 = int(input("Ingresa un segundo número  : "))
# binario2 = decimal_a_binario2(decimal2)
# print("-------este es el resultado de los numeros convertidos en binarios ------------")
# print(f"El número {decimal} es {binario} en binario")
# print("---------------------------------+-----------------------------------------")
# print(f"El número {decimal2} es {binario2} en binario")

# suma = decimal+decimal2
# resta = decimal-decimal2
# print("---------------------------------+-----------------------------------------")
# print(f"Esta es la suma de los número {suma}")
# print("--------------------------------------------------------------------------")
# print(f"Esta es la resta de los número {resta}")



# 6.Se desea almacenar en un vector seis posiciones que corresponde a las caras de un dado, con la formula de valores aleatorios debe de generar un valor de uno a seis, se debe solicitar el numero de lanzamientos a realizar y luego calcular el valor obtenido en cada uno de los lances.

import random
def unico(x,L):
  esUnico=True
  for i in range(len(L)):
    if x==L[i]:
      esUnico=False
      break
  return esUnico
L=[]
j=0
while j<6:
  x=random.randint(1,6)
  if unico(x,L):
    L.append(x)
    j+=1


Lanzar=int(input("numero el cual desea lanzara del 1 al 6  :  "))
esUnico = unico(x, L)
print(f"numero aleatorio como los dados {L}")
print(f"el valor obtenido en cada uno de los lances {j}")











