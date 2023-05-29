#César Pumacayo 1°E Grupo Giovanni
from funciones import *
from menu import *

def dream_team_app():
    while True:
        respuesta = menu_principal()

        if respuesta == 1:
            imprimir_dato(mostrar_nombre_posicion(lista_basquet, "posicion"))
                
        elif respuesta == 2:
            usuario_indice(lista_basquet)
            jugador = int(input("Ingrese el índice del jugador para ver sus estadísticas: "))
            imprimir_dato(busqueda_jugador_por_indice(lista_basquet, jugador))
        elif respuesta == 3:
            estadisticas_guardadas =  seleccionar_estadisticas_jugador(jugador)
            guardar_csv("jugador_estadistica.csv", estadisticas_guardadas)
        elif respuesta == 4:
            nombre_jugador = buscar_jugador_nombre(lista_basquet)
            imprimir_dato(mostrar_logros_jugador_seleccionado(nombre_jugador))
        elif respuesta == 5:
            tipo_estadistica = "promedio_puntos_por_partido"
            mostrar_estadistica_por_jugador_ordenado(lista_basquet, "nombre", tipo_estadistica, condicion=True)
            promedio = calcular_promedio_total(lista_basquet, tipo_estadistica)
            imprimir_dato("\nEl promedio total del equipo de {0}: {1}\n".format(tipo_estadistica.replace("_", " ").capitalize(),promedio))
        elif respuesta == 6:
            imprimir_dato(mostrar_miembros_salon_de_la_fama(lista_basquet))
        elif respuesta == 7:
            imprimir_dato(mostrar_mayor_cantidad_estadisticas(lista_basquet, "maximo", "estadisticas", "rebotes_totales"))
        elif respuesta == 8:
            imprimir_dato(mostrar_mayor_cantidad_estadisticas(lista_basquet, "maximo", "estadisticas", "porcentaje_tiros_de_campo"))
        elif respuesta == 9:
            imprimir_dato(mostrar_mayor_cantidad_estadisticas(lista_basquet, "maximo", "estadisticas", "asistencias_totales"))
        elif respuesta == 10:
            imprimir_dato(mostrar_valor_mayor_que_lo_ingresado(lista_basquet, "estadisticas", "promedio_puntos_por_partido"))
        elif respuesta == 11:
            imprimir_dato(mostrar_valor_mayor_que_lo_ingresado(lista_basquet, "estadisticas", "promedio_rebotes_por_partido"))
        elif respuesta == 12:
            imprimir_dato(mostrar_valor_mayor_que_lo_ingresado(lista_basquet, "estadisticas", "promedio_asistencias_por_partido"))
        elif respuesta == 13:
            imprimir_dato(mostrar_mayor_cantidad_estadisticas(lista_basquet, "maximo", "estadisticas", "robos_totales"))
        elif respuesta == 14:
            imprimir_dato(mostrar_mayor_cantidad_estadisticas(lista_basquet, "maximo", "estadisticas", "bloqueos_totales"))
        elif respuesta == 15:
            imprimir_dato(mostrar_valor_mayor_que_lo_ingresado(lista_basquet, "estadisticas", "porcentaje_tiros_libres"))
        elif respuesta == 16:
            promedio = calcular_promedio_excluyendo_menor(lista_basquet, "promedio_puntos_por_partido")
            imprimir_dato("\nEl promedio total del equipo de {0}: {1}\n".format("promedio_puntos_por_partido".replace("_", " ").capitalize(),promedio))
        elif respuesta == 17:
            imprimir_dato(obtener_jugador_mayor_logros(lista_basquet, clave="logros"))
        elif respuesta == 18:
            imprimir_dato(mostrar_valor_mayor_que_lo_ingresado(lista_basquet, "estadisticas", "porcentaje_tiros_triples"))
        elif respuesta == 19:
            jugadores_mayor_temporadas = obtener_jugadores_mayor_temporadas(lista_basquet)
            mostrar_jugadores_mayor_temporadas(jugadores_mayor_temporadas)
        elif respuesta == 20:
            valor_ingresado = float(input("Ingrese el valor del porcentaje de tiros de campo: "))
            mostrar_jugadores_superior_porcentaje(lista_basquet, valor_ingresado)
        elif respuesta == 21:
            break
        else:
            print("Opción inválida, ingrese una letra con mayuscula")
        input("\nPulse enter para continuar\n")

dream_team_app()