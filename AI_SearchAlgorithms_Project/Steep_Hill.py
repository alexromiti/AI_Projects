#Encargado: Alex Romero Mitiaeva

'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene el algoritmo Steepest hill climbing

-Pasos a Seguir para Ejecutar el Codigo-
llamar la funcion steepest_hill_climbing en el main
'''''

#---Dependencias---
from Graph import mexDirectedGraph  #Importacion del grafo
from Heuristhic import cities_coordinates, haversine    #Importacion de la heuristica y funcion haversine

#---Funcion Principal---

# Función para implementar el algoritmo Steepest Hill Climbing
def steepest_hill_climbing(graph, coordinates, start, goal, ver_proceso):
    current_node = start  # Iniciar desde el nodo inicial
    current_distance = 0  # Variable para almacenar la distancia actual del camino
    path = [start]  # Lista para almacenar el camino
    num_of_iteration = 0    #contador para iteraciones


    # Loop hasta llegar al nodo objetivo
    while current_node != goal:
        neighbors = list(graph[current_node].keys())  # Obtener los vecinos del nodo actual

        if ver_proceso == 'y':  #Visualiza el proceso
            print(current_node)

        if not neighbors:
            # No hay vecinos alcanzables, terminar la búsqueda
            print("No se encontraron vecinos alcanzables desde el nodo actual:", current_node)
            break

        best_neighbor = None  # Inicializar el mejor vecino como None
        best_distance = float('inf')  # Inicializar la mejor distancia como infinito

        # Buscar el vecino con la menor distancia al nodo objetivo
        for neighbor in neighbors:
            # Calcular la distancia haversine al vecino desde el nodo objetivo
            h_value = haversine(coordinates[neighbor], coordinates[goal])
            if h_value < best_distance:
                best_neighbor = neighbor
                best_distance = h_value

                if ver_proceso =='y':   #Visualizar proceso
                    print("\nBest Neighbor = {}, Best Distance = {}".format(best_neighbor,best_distance))

        if best_neighbor is None:
            return None, None  # Si no hay vecinos disponibles, retornar None para el camino y la distancia

        current_distance += graph[current_node][best_neighbor]  # Actualizar la distancia actual del camino
        current_node = best_neighbor  # Moverse al mejor vecino encontrado
        path.append(current_node)  # Agregar el vecino al camino

        if ver_proceso == 'y':  #Visualizar proceso
            print("\nDistancia actual: ",current_distance)
        
        num_of_iteration += 1 #Contar el numero de las iteraciones


    print("\nNumero de Iteraciones: ",num_of_iteration,"\n") #Visualiza iteraciones
    return path, current_distance

'''''
# Ejemplo de uso
start = 'Cancun'
goal = 'Campeche'

shortest_path, shortest_distance = steepest_hill_climbing(mexDirectedGraph, cities_coordinates, start, goal)

if shortest_path:
    print("El camino más corto es:", shortest_path)
    print("La distancia total del camino más corto es:", shortest_distance, "km")
else:
    print("No se encontró un camino desde", start, "hasta", goal)
'''''
