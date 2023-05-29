#César Pumacayo Grupo Giovanni 1°E
import copy
import json
import csv
import re

from functools import reduce
from copy import deepcopy

def leer_archivo(ruta:str)->dict:
    '''
    Lee y abre el archivo de la ruta en este caso .JSON
    Parametros: 
        ruta: str, la ruta donde se abrira y leera el archivo
    Retorna:
        dict: accede a la clave y valor

    '''
    with open(ruta , "r") as archivo:
        diccionario_jugadores= json.load(archivo)
    return diccionario_jugadores["jugadores"]

rutaJSON = "Examen_parcial\\dt.json"
lista_basquet= leer_archivo(rutaJSON)


def mostrar_nombre_posicion(lista_basquet:list[dict], key:str)->str:
    '''
    Esta funcion muestra todos los jugadores y sus posiciones
    -----------------
    Parametros:
    lista_basquet: list[dict], lista de todos los jugadores , sus estadisticas y etc
    key: str, clave del diccionario
    -----------------
    Retorna: 
    resultado: str, muestra todos los jugadores y sus posiciones concatenados 

    '''
    resultado = ""
    if not lista_basquet:
        print("Lista vacía")
        return False
    else:
        for jugador in lista_basquet:
            nombre = jugador["nombre"]
            valor_key = jugador[key]
            resultado += nombre + " - " + valor_key + "\n"
        return resultado

'''
---------------- 2 -------------
'''
def usuario_indice(lista_basquet:list)->None:
    '''
    Esta funcion muestra el indice de todos los jugadores de la lista de diccionario
    Parametros: 
        lista_basquet: la lista de jugadores
    No retorna
    '''
    contador = 0
    for i in lista_basquet:
        print("\n{0} | {1}".format(contador, i["nombre"]))
        contador += 1
    print("\n{0}".format("-"*55))
    

def busqueda_jugador_por_indice(lista_basquet:list[dict], jugador:int)->list:
    '''
    Muestra las estadisticas del jugador ingresado mediante su indice
    ------------
    Parametros:
    lista_basquet: list[dict], lista de jugadores, incluyendo su nombre, posición y estadísticas
    jugador: int, el numero que ingresaste
    ------------
    Retorna: 
    jugador_busqueda: list ,la lista de estadisticas del indice ingresado

    '''
    if not lista_basquet:
        return False
    else:
        jugador_busqueda= lista_basquet[jugador]["estadisticas"]
        return jugador_busqueda


'''
----------------- 3---------------------
'''

def seleccionar_estadisticas_jugador(indice: int)->list:
    '''
    Extrae información de manera especifica del jugador seleccionado por su índice y ademas se agrega a la lista "datos".
    ------------
    Parametros:
    indice: int, representa el índice del jugador que seleccionaste
    ------------
    Retorna:
    datos: una lista de datos del jugador especifico
    '''
    if not lista_basquet:
        print("La lista de jugadores está vacía.")
    else:
        copia = copy.deepcopy(lista_basquet)
        datos = []

        datos.append(["nombre", lista_basquet[(indice)]["nombre"]])
        datos.append(["posicion", lista_basquet[(indice)]["posicion"]])

        if copia[(indice)]:
            estadisticas = copia[(indice)]["estadisticas"]

            for clave, valor in estadisticas.items():
                datos.append([clave, valor])
            return datos

        else:
            print("La función no devuelve una lista de datos.")

        if lista_basquet == copia:
            print("La lista original no ha sido modificada.")
        else:
            print("La lista original ha sido modificada.")


def guardar_csv(nombre_archivo: str, lista_jugador: list)->bool:
    '''
    Guarda el csv de manera que nosotros podamos leerlo y sobreescribirlo "w"
    ------------
    Parametros: 
    nombre_archivo: str, el nombre del archivo
    lista_jugador es la lista del jugador seleccionado anteriormente con su informacion 
    ------------
    Retorna:
    True o False
    '''
    if not lista_jugador:
        print("ERROR, {0} no se guardo correctamente...".format(nombre_archivo))
        return False
    else:
        with open(nombre_archivo, 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerows(lista_jugador)
            print("El archivo {0} se guardó correctamente".format(nombre_archivo))
            return True



'''
----------------------Parte 4 ----------------
'''

def buscar_jugador_nombre(lista_basquet: list[dict])->list:
    '''
    Esta funcion permite al usuario ingresar un nombre para buscar en dicha lista. La función utiliza expresiones regulares para realizar la búsqueda del nombre ingresado en los nombres de los jugadores.   
    ------------
    Parametros:
    lista_basquet: list[dict] 
    ------------
    Retorna:
    False: bool, en caso que no coincida con la búsqueda
    jugadores_encontrados: list, la lista de nombre que coincidan con nombre ingresado
    '''
    if not lista_basquet:
        print("Lista vacía")
        return False
    else:
        nombre_busqueda = input("Ingrese el nombre que desea buscar: ")
        jugadores_encontrados = []
        
        for jugador in lista_basquet:
                if re.search(fr"^\b{nombre_busqueda}", jugador["nombre"], flags=re.IGNORECASE):
                    jugadores_encontrados.append(jugador)
            
        if jugadores_encontrados:
            return jugadores_encontrados

        else:
            print("No se ha encontrado ningún jugador que coincida con la búsqueda.")
            return False
            

def mostrar_logros_jugador_seleccionado(jugadores_encontrados: list) -> str:
    '''
    Esta función muestra al jugador seleccionado y sus logros.
    ------------
    Parámetros:
    jugadores_encontrados: list - La lista de jugadores encontrados.
    ------------
    Retorna:
    texto: str - El texto que muestra al jugador y sus logros.
    '''
    if jugadores_encontrados:
        texto = ""
        for jugador in jugadores_encontrados:
            logros = ", ".join(jugador.get("logros", []))
            texto += "{0}, logros: {1}\n".format(jugador["nombre"], logros)
    else:
        texto = "No se ha encontrado ningún jugador que coincida con la búsqueda."

    return texto


'''
---------------------Parte 5 ----------------
'''
def calcular_promedio_total(lista_basquet: list[dict], estadistica: str)->float:
    '''
    Esta función calcula el promedio total de la estadística seleccionada.
    ------------
    Parámetros:
    lista_basquet: tipo list[dict] -> la lista original que se importó del JSON.
    estadistica: tipo string -> la key de la estadística para calcular el promedio.
    ------------
    Retorna:
    promedio: tipo float -> el promedio calculado.
    '''
    acumulador=0
    contador=0
    
    for indice in lista_basquet:
        if type(indice["estadisticas"][estadistica]) == type(int()) or type(indice["estadisticas"][estadistica]) == type(float()):
            acumulador+= indice["estadisticas"][estadistica]
            contador+=1
    if contador > 0:
        promedio = float(acumulador / contador)
    else:
        print("Error, estadística inexistente")


    return promedio

# def ordenar_lista_segun_key(lista_original: list, key_a_ordenar: str, flag_estadistica=False, orden_asc=True) -> list:
#     '''
#     Esta función genera una lista ordenada según el param "key_a_ordenar" a través de un método de ordenamiento.
#     -----------
#     Parámetros:
#     lista_original: tipo list[dict] -> la lista original 
#     key_a_ordenar: tipo string -> la key cuyo valor se va a utilizar como el parámetro del ordenamiento.
#     flag_estadistica: tipo bool - definido en False -> flag que determina si la key a ordenar se encuentra dentro de "estadisticas" o no.
#     orden_asc: tipo bool - definido en True -> variable que determina si el orden es ascendente(True) o descendente(False)
#     -----------
#     Retorna:
#     False: en caso de que lista_original se encuentre vacía. 
#     lista: tipo list -> la lista ordenada.
#     '''
#     if len(lista_original) == 0:
#         print("Lista vacía.")
#         return False
#     lista = lista_original[:]
#     rango_a = len(lista)
#     flag_swap = True
#     while (flag_swap):
#         flag_swap = False
#         rango_a = rango_a - 1
#         for indice_A in range(rango_a):
#             if flag_estadistica == False:
#                 if orden_asc == True:
#                     if lista[indice_A][key_a_ordenar] > lista[indice_A+1][key_a_ordenar]:
#                         lista[indice_A], lista[indice_A +
#                                                1] = lista[indice_A+1], lista[indice_A]
#                         flag_swap = True
#                 elif orden_asc == False:
#                     if lista[indice_A][key_a_ordenar] < lista[indice_A+1][key_a_ordenar]:
#                         lista[indice_A], lista[indice_A +
#                                                1] = lista[indice_A+1], lista[indice_A]
#                         flag_swap = True
#             elif flag_estadistica == True:
#                 if orden_asc == True:
#                     if lista[indice_A]["estadisticas"][key_a_ordenar] > lista[indice_A+1]["estadisticas"][key_a_ordenar]:
#                         lista[indice_A], lista[indice_A +
#                                                1] = lista[indice_A+1], lista[indice_A]
#                         flag_swap = True
#                 elif orden_asc == False:
#                     if lista[indice_A]["estadisticas"][key_a_ordenar] < lista[indice_A+1]["estadisticas"][key_a_ordenar]:
#                         lista[indice_A], lista[indice_A +
#                                                1] = lista[indice_A+1], lista[indice_A]
#                         flag_swap = True
#     return lista

def ordenar_lista_por_atributo(lista_original:list, atributo: str, condicion: str):
    '''
    Genera una lista de heroes ordenada, según su atributo, con el orden solicitado(asc o desc).
    ----------
    Parámetros:
    lista_orginal: tipo list[dict] - La lista de la cual se trabajará, primero generando una copia.
    atributo: tipo string - La key que se utilizará de parámetro para el ordenamiento.
    orden: tipo string - el tipo de ordenamiento que se solicita. (asc o desc)
    ----------
    Devuelve:
    -1: en caso de error, ya sea que la lista está vacía.
    lista: la lista ordenada, ascendente o descendente, según el atributo pedido por parámetro.
    '''
    rango = len(lista_original)
    for indice in range(rango - 1):
        for indice in range(rango - indice - 1):
            if  condicion == False and lista_original[indice][atributo] < lista_original[indice+1][atributo] or condicion == True and lista_original[indice][atributo] > lista_original[indice+1][atributo]:
                lista_original[indice],lista_original[indice+1] = lista_original[indice+1],lista_original[indice]
    return [heroe for heroe in lista_original]



def mostrar_estadistica_por_jugador_ordenado(lista_original: list[dict], key_orden: str, estadistica: str , condicion):
    '''
    Esta función muestra un listado ordenado según "key_orden", del nombre de los jugadores 
    junto a la estadística pasada por param.
    -----------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    key_orden: tipo string -> la key cuyo valor se va a utilizar como el parámetro del ordenamiento.
    estadistica: tipo string -> la key cuyo valor se quiere mostrar en el listado.
    condicion: tipo bool -> True si es ascendente o False descendente
    -----------
    Retorna:
    False: en caso de que lista_original se encuentre vacía. 
    str: tipo str -> una cadena de texto.  
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    lista_aux = lista_original[:]
    lista = ordenar_lista_por_atributo(lista_aux, key_orden, condicion)
    for i in lista:
        estadistica_str = estadistica.replace("_", " ").capitalize()
        mensaje = "Jugador: {0}\n{1}: {2}\n".format(i["nombre"],estadistica_str,i["estadisticas"][estadistica])
        print(mensaje)
    return mensaje


'''
---------------Parte 6------------
'''
def mostrar_miembros_salon_de_la_fama(lista_basquet:list[dict])->list:
    '''
    Esta funcion muestra a los miembros de la fama de la list[dict]
    ----------------
    Parametros: 
    lista_basquet: tipo list[dict] -> La lista de diccionario importado del JSON
    ----------------
    Retorna:
    resultados: tipo list -> retorna una lista
    '''
    jugadores_encontrados = buscar_jugador_nombre(lista_basquet)
    
    resultados = []
    
    for jugador in jugadores_encontrados:
        logros = jugador["logros"]
        if "Miembro del Salon de la Fama del Baloncesto" in logros:
            resultado = "{0} enhorabuena!!, es miembro del Salon de la Fama del Baloncesto".format(jugador["nombre"])
        else:
            resultado = "{0} Lo lamento...no es miembro del Salon de la Fama del Baloncesto".format(jugador["nombre"])
        
        resultados.append(resultado)
    
    return '\n'.join(resultados)

'''
---------------------Parte 7----------------
'''

def calcular_max(lista_heroes:list, key:str, clave2)->str:
    '''
    Calcular máximo de la lista según el key
    Recibe lista_heroes y key (str)
    Retorna el jugador con el mayor dato
    '''
    valor = lista_heroes[0]

    for i in lista_heroes:
        if float(i[key][clave2]) > float(valor[key][clave2]):
            valor = i

    return valor

def calcular_min(lista_heroes:list, key:str, clave2)->str:
    '''
    Calcular minimo de la lista segun el key
    Recibe lista_heroes y key(str)
    Retorna el heroe del dato menos alto
    '''
    valor = lista_heroes[0]

    for i in lista_heroes:
        if float(i[key][clave2]) < float(valor[key][clave2]):
            valor = i

    return valor

def calcular_max_min_dato(lista_heroes:list, string:str, string_clave:str , clave2):
    '''
    Calcular maximo y minimo en una sola funcion
    Recibe lista_heroes , string (maximo o minimo) y string_clave
    Retorna str
    '''
    if string=="maximo":
        dato_maximo= calcular_max(lista_heroes, string_clave, clave2)
        return dato_maximo 
    elif string=="minimo":
        dato_minimo=calcular_min(lista_heroes,string_clave, clave2)
        return dato_minimo

def mostrar_mayor_cantidad_estadisticas(valor, max_min , key, clave2 ):
    valor = calcular_max_min_dato(lista_basquet, max_min , key, clave2)
    clave =clave2.replace("_", " ").capitalize()

    texto = f"Nombre: {valor['nombre']}\n{clave}: {valor[key][clave2]}"
    return texto



def filtrar_por_promedio(lista_original: list, key: str, clave2: str, numero):
    if len(lista_original) == 0:
        return -1
    lista_filtrada = []
    for heroe in lista_original:
        promedio = heroe[key][clave2]
        if promedio > numero:
            lista_filtrada.append(heroe)
    return lista_filtrada


def mostrar_valor_mayor_que_lo_ingresado(lista, key, clave2):
    numero = int(input("Ingresa un valor: "))
    lista_filtrada = filtrar_por_promedio(lista, key, clave2, numero)
    texto = ""
    if not lista_filtrada:
        texto = "No se ha encontrado ningun valor que supere al valor ingresado"
    for heroe in lista_filtrada:
        nombre = heroe['nombre']
        valor = heroe[key][clave2]
        clave = clave2.replace("_", " ").capitalize()

        texto += f"Nombre: {nombre}\n{clave}: {valor}\n\n"
    return texto

    
def calcular_promedio_excluyendo_menor(lista_original: list[dict], estadistica: str):
    '''
    Esta función calcula el promedio total de la estadística seleccionada.
    ------------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    estadistica: tipo string -> la key de la estadística para calcular el promedio.
    ------------
    Retorna:
    False: en caso de que lista_original se encuentre vacía. 
    promedio: tipo float -> el promedio calculado.
    '''
    minimo = calcular_max_min_dato(lista_basquet, "minimo", "estadisticas", "promedio_puntos_por_partido")

    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    lista = lista_original[:]
    if len(lista) <= 1:
        return lista
    contador = 0
    acumulador = 0
    if estadistica in lista[0]["estadisticas"].keys():
        for jugador in lista:
            acumulador += jugador["estadisticas"][estadistica]
            contador += 1
            
        acumulador= float(acumulador - minimo["estadisticas"][estadistica])
        contador= contador - 1
        promedio = float(acumulador / contador)
        return promedio
    else:
        print("Estadística inexistente.")

# promedio = calcular_promedio_excluyendo_menor(lista_basquet, "promedio_puntos_por_partido", minimo)

# print("\nEl promedio total del equipo de {0}: {1}\n".format("promedio_puntos_por_partido".replace("_", " ").capitalize(),promedio))

'''
---------------------------Parte 17------------
'''
# print(mostrar_mayor_cantidad_estadisticas(lista_basquet, "maximo", "estadisticas", "logros"))

def obtener_jugador_mayor_logros(lista_jugadores, clave)->str:
    jugador_mayor_logros = None
    mayor_cantidad_logros = 0
    # menor_cantidad_logros = float('inf')


    for jugador in lista_jugadores:
        cantidad_logros = len(jugador[clave])
        if cantidad_logros > mayor_cantidad_logros:
            mayor_cantidad_logros = cantidad_logros
            jugador_mayor_logros = jugador
            texto= "El jugador con la mayor cantidad de logros obtenidos es: {0}\nlos logros son: {1}\nCantidad de logros: {2}".format(jugador_mayor_logros['nombre'], jugador_mayor_logros["logros"], len(jugador_mayor_logros["logros"]))

    return texto

# mayor = obtener_jugador_mayor_logros(lista_basquet, clave="logros")
# print("El jugador con la mayor cantidad de logros obtenidos es:", mayor['nombre'])
# print("Cantidad de logros:", mayor["logros"])

'''
---------------------Parte 18-------------------
'''
# print(mostrar_valor_mayor_que_lo_ingresado(lista_basquet, "estadisticas", "porcentaje_tiros_triples"))

'''
------------------Parte 19-----------------------
'''

def obtener_jugadores_mayor_temporadas(lista_jugadores):
    jugadores_mayor_temporadas = []
    mayor_cantidad_temporadas = 0

    for jugador in lista_jugadores:
        cantidad_temporadas = jugador['estadisticas']['temporadas']
        if cantidad_temporadas > mayor_cantidad_temporadas:
            mayor_cantidad_temporadas = cantidad_temporadas
            jugadores_mayor_temporadas = [jugador]
        elif cantidad_temporadas == mayor_cantidad_temporadas:
            jugadores_mayor_temporadas.append(jugador)

    return jugadores_mayor_temporadas

def mostrar_jugadores_mayor_temporadas(jugadores_mayor_temporadas):
    if jugadores_mayor_temporadas:
        print("Jugadores con la mayor cantidad de temporadas jugadas:")
        for jugador in jugadores_mayor_temporadas:
            print("Nombre:", jugador['nombre'])
            print("Cantidad de temporadas jugadas:", jugador['estadisticas']['temporadas'])
            print("---")
    else:
        print("No se encontraron jugadores en la lista.")


# jugadores_mayor_temporadas = obtener_jugadores_mayor_temporadas(lista_basquet)
# mostrar_jugadores_mayor_temporadas(jugadores_mayor_temporadas)


'''
----------Parte 20-----------
'''
    
def mostrar_jugadores_superior_porcentaje(lista_jugadores, porcentaje):
    jugadores_filtrados = []

    for jugador in lista_jugadores:
        porcentaje_tiros_campo = jugador['estadisticas']['porcentaje_tiros_de_campo']
        if porcentaje_tiros_campo > porcentaje:
            jugadores_filtrados.append(jugador)

    n = len(jugadores_filtrados)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if jugadores_filtrados[j]['posicion'] < jugadores_filtrados[min_index]['posicion']:
                min_index = j
        jugadores_filtrados[i], jugadores_filtrados[min_index] = jugadores_filtrados[min_index], jugadores_filtrados[i]

    if jugadores_filtrados:
        print("Jugadores con porcentaje de tiros de campo superior a", porcentaje)
        for jugador in jugadores_filtrados:
            print("Nombre:", jugador['nombre'])
            print("Posición:", jugador['posicion'])
            print("Porcentaje de tiros de campo:", jugador['estadisticas']['porcentaje_tiros_de_campo'])
            print("---")
    else:
        print("No se encontraron jugadores con porcentaje de tiros de campo superior a", porcentaje)


# valor_ingresado = float(input("Ingrese el valor del porcentaje de tiros de campo: "))
# mostrar_jugadores_superior_porcentaje(lista_basquet, valor_ingresado)

'''
-------------------------BONUS-----------------------
'''
# def calcular_ranking_posicion(lista_basquet):
#     if not lista_basquet:
#         print("Lista vacía")
#         return -1
#     else:
#         for i in lista_basquet:

        

# def ordenar_por_nombre(lista_basquet):
#     lista= []
#     for indice in range(len(lista_basquet)):
#         lista = print(lista_basquet[indice]["nombre"])

    
#     return lista

# ordenar_por_nombre(lista_basquet)
# def calcular_lista_ranking_jugadores_stats(lista_original: list[dict]):
#     '''
#     Esta función genera una lista que contiene a los jugadores, con la posición que rankearían según distíntas estadísticas.
#     ------------
#     Parámetros:
#     lista_original: tipo list[dict] -> la lista original que se importó del JSON.
#     ------------
#     Retorna:
#     False: en caso de que lista_original se encuentre vacía.
#     lista_ranking: tipo list[list] -> la lista que posee, en formato de lista, a los jugadores junto a la posición de ranking de las estadísticas.
#     '''
#     if len(lista_original) == 0:
#         print("Lista vacía.")
#         return False
#     lista_aux = lista_original[:]
#     lista_ranking = []
#     contador = 0
#     lista_puntos = ordenar_lista_segun_key(
#         lista_aux, "puntos_totales", True, False)
#     lista_rebotes = ordenar_lista_segun_key(
#         lista_aux, "rebotes_totales", True, False)
#     lista_asistencias = ordenar_lista_segun_key(
#         lista_aux, "asistencias_totales", True, False)
#     lista_robos = ordenar_lista_segun_key(
#         lista_aux, "robos_totales", True, False)
#     while contador <= len(lista_aux):
#         for indice_aux in range(len(lista_aux)):
#             lista_ranking_jugador = []
#             for indice_puntos in range(len(lista_aux)):
#                 if lista_aux[indice_aux]["nombre"] == lista_puntos[indice_puntos]["nombre"]:
#                     lista_ranking_jugador.extend(
#                         [lista_aux[indice_aux]["nombre"], str(indice_puntos + 1)])
#             for indice_rebotes in range(len(lista_aux)):
#                 if lista_aux[indice_aux]["nombre"] == lista_rebotes[indice_rebotes]["nombre"]:
#                     lista_ranking_jugador.extend([str(indice_rebotes + 1)])
#             for indice_asistencias in range(len(lista_aux)):
#                 if lista_aux[indice_aux]["nombre"] == lista_asistencias[indice_asistencias]["nombre"]:
#                     lista_ranking_jugador.extend([str(indice_asistencias + 1)])
#             for indice_robos in range(len(lista_aux)):
#                 if lista_aux[indice_aux]["nombre"] == lista_robos[indice_robos]["nombre"]:
#                     lista_ranking_jugador.extend([str(indice_robos + 1)])
#             contador += 1
#             lista_ranking.append(lista_ranking_jugador)
#     return lista_ranking

# lista_ranking = calcular_lista_ranking_jugadores_stats(lista_basquet)
# print(lista_ranking)
# def exportar_ranking_csv(lista_original: list[dict], path: str):
#     '''
#     Esta función exporta un archivo .csv con el formato para generar una tabla con la posiciones de las estadísticas.
#     ------------
#     Parámetros:
#     lista_original: tipo list[dict] -> la lista original que se importó del JSON.
#     path: tipo string -> la ruta del directorio donde se quiere generar el archivo .csv.
#     ------------
#     Retorna:
#     False: en caso de que lista_original se encuentre vacía.
#     '''
#     if len(lista_original) == 0:
#         print("Lista vacía.")
#         return False
#     lista_keys = ["Jugador", "Puntos", "Rebotes", "Asistencias", "Robos"]
#     string_keys = ",".join(lista_keys)
#     mensaje = string_keys + "\n"
#     for jugador in lista_ranking:
#         mensaje += ",".join(jugador) + "\n"
#     with open(path, "w") as archivo:
#         archivo.writelines([mensaje])
#     print("el archivo fue creado en {0}".format(path))



# exportar_ranking_csv(lista_ranking, 'ranking_jugadores.csv')


'''
----------- FIN -----------------
'''






















