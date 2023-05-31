#César Pumacayo 1°E Grupo Giovanni

import re


def imprimir_dato(texto:str):
    print(texto)

def menu_principal()->str:
    '''
    Muestra el menu de opciones y valida el caracter que ingreso el usuario con un rango
    No recibe nada
    Retorna un int
    '''
    imprimir_menu_parcial_1()
    entrada = input("Ingrese una opción del menú (1-20): ")
    if re.match(r"^[1-9]|1[0-9]|2[0-6]$", entrada):
        return int(entrada)
    else:
        return -1


def imprimir_menu_parcial_1()->None:
    '''
    Imprime el desafio 5 de la parte 1 stark
    No recibe nada
    No retorna
    '''
    imprimir_dato(
                    "1 - Mostrar nombre y posición de todos los jugadores.\n"
                    "2 - Seleccionar por indice a un jugador y mostrar sus estadisticas completas.\n" 
                    "3 - Guardar en csv: Nombre, posicion y el anterior punto(2).\n"
                    "4 - Buscar por nombre y mostrar sus logros.\n"
                    "5 - Mostrar el promedio puntos por partido del 'Dream Team', ordenado por nombre(ascendente).\n"
                    "6 - Buscar por nombre y mostrar si es miembro del Salón de la Fama del Baloncesto.\n"
                    "7 - Mostrar el jugador con la mayor cantidad de rebotes totales.\n"
                    "8 - Mostrar el jugador con la mayor porcentaje de tiros de campo.\n"
                    "9 - Mostrar el jugador con la mayor cantidad de asistencias totales.\n"
                    "10 - Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.\n"
                    "11 - Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n"
                    "12 - Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.\n"
                    "13 - Mostrar el jugador con la mayor cantidad de robos totales.\n"
                    "14 - Mostrar el jugador con la mayor cantidad de bloqueos totales.\n"
                    "15 - Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.\n"
                    "16 - Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n"
                    "17 - Mostrar el jugador con la mayor cantidad de logros obtenidos.\n"
                    "18 - Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n"
                    "19 - Mostrar el jugador con la mayor cantidad de temporadas jugadas.\n"
                    "20 - Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n"
                    "21 -  la cantidad de jugadores que hay por cada posición (1)\n"
                    "22 - Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente\n"
                    "23 . Bonus Rankings Jugadores\n"
                    "24 - Jugadores que tienen las mejores estadísticas en cada valor\n"
                    "25 - Jugador tiene las mejores estadísticas de todos\n"
                    "26 - Salir \n"

                    "O- Salir\n"
    )


