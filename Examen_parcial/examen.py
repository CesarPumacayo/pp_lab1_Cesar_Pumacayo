# def ivan_sort_B(lista_original, flag_orden, key):
#     lista = lista_original[:]
#     rango_a = len(lista) - 1
#     flag_swap = True

#     while flag_swap:
#         flag_swap = False

#         for indice_A in range(rango_a):
#             if (flag_orden == False and lista[indice_A][key] < lista[indice_A+1][key]) or \
#                (flag_orden == True and lista[indice_A][key] > lista[indice_A+1][key]):
#                 lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
#                 flag_swap = True

#     return lista

# # Ejemplo de uso
# heroes = [
#     {"nombre": "Superman", "fuerza": 100},
#     {"nombre": "Batman", "fuerza": 80},
#     {"nombre": "Wonder Woman", "fuerza": 95},
#     {"nombre": "Spider-Man", "fuerza": 70},
#     {"nombre": "Hulk", "fuerza": 120},
#     {"nombre": "Thor", "fuerza": 110}
# ]

# sorted_heroes = ivan_sort_B(heroes, True, "fuerza")
# for hero in sorted_heroes:
#     print(f"{hero['nombre']}: {hero['fuerza']}")


'''
def exportar_lista_csv(heroes):
    
    with open('heroes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["nombre", "altura", "fuerza", "inteligencia"])
        for heroe in heroes:
            writer.writerow([heroe["nombre"], heroe["altura"], heroe["fuerza"], heroe["inteligencia"]])

    print("La lista de héroes ha sido exportada a heroes.csv.")
----------------------------------------------
'''

# def quick_sort(lista_original: list, flag_orden: bool) -> list:
#     lista_de = []  # lista derecha
#     lista_iz = []  # lista izquierda
#     if len(lista_original) <= 1:
#         return lista_original
#     else:
#         pivot = lista_original[0]  # puede ser al azar o no
#         for elemento in lista_original[1:]:
#             if elemento["name"] > pivot["name"]:  # Compare based on the "name" key
#                 lista_de.append(elemento)
#             else:
#                 lista_iz.append(elemento)
#     lista_iz = quick_sort(lista_iz, True)
#     lista_iz.append(pivot)
#     lista_de = quick_sort(lista_de, True)
#     lista_iz.extend(lista_de)

#     return lista_iz

#César Pumacayo Grupo Giovanni 1°E
import json
import csv
import re


def leer_archivo(ruta:str)->list:
    with open(ruta , "r") as archivo:
        diccionario_heroes= json.load(archivo)
    return diccionario_heroes["jugadores"]



rutaJSON = "Examen_parcial\\dt.json"
lista_basquet= leer_archivo(rutaJSON)


def mostrar_basquetbolistas(lista_basquet:list):
    lista_jugadores= []
    for i in lista_basquet:
        lista_nueva= i["nombre"] + " - " + i["posicion"]
        lista_jugadores.append(lista_nueva)
    return lista_jugadores

# print(mostrar_basquetbolistas(lista_basquet))

'''
---------------- Parte 2 -------------
'''
def usuario_indice():
    contador=0
    for i in lista_basquet:
        print("{0}° {1} ".format(contador, i["nombre"]),end= " || ")
        contador+=1
    # jugador = int(input("\nIngrese segun el indice las estadisticas del jugador: "))

def busqueda_jugador_por_indice(lista_basquet, jugador):
    for i in lista_basquet:
        jugador_busqueda= lista_basquet[jugador]["estadisticas"]
    return jugador_busqueda

usuario_indice()
print("\n{0}".format("-"*55))
jugador = int(input("Ingrese segun el indice las estadisticas del jugador: "))

print(busqueda_jugador_por_indice(lista_basquet, jugador))

genio = busqueda_jugador_por_indice(lista_basquet, jugador)


lista_genio = genio

'''
-------------------------
'''
# def guardar_csv(lista_usuarios: list, ruta: str):
#     with open(ruta, 'w', newline='') as archivo:
#         escritor = csv.writer(archivo)
    
#         escritor.writerow(['Estadisticas'])  # Escribir encabezado en el archivo CSV
        
#         for usuario in lista_usuarios:
#             escritor.writerow([usuario])
def generar_csv(nombre_archivo:str, lista:list): 
    with open(nombre_archivo, "w") as archivo:
        for video in lista:
            mensaje = "{0},{1},{2},{3},{4},{5}\n"
            #FALTA REMPLAZAR COMAS y SALTOS DE LINEA
            mensaje = mensaje.format(   
                                        video["temporadas"].replace(",","-"),
                                        video["puntos totales"].replace(",","-"),
                                    )
            archivo.write(mensaje)

generar_csv("ruta.csv", lista_genio)


# while True:

#     match(opcion):
#         case 1:
#             pass
#         case 2:
#             pass
#         case 3:
#             pass
#         case 4:
#             pass
#         case 5:
#             pass
#         case 6:
#             pass
#         case 7:
#             pass
#         case 8:
#             pass
#         case 0:
#             break
#         case _:
#             print("opcion incorrecta")






















