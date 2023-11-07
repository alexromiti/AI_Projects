#Encargado: Leonardo Kenji Minemura Suazo 
'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene el algoritmo Greedy best first search 

-Pasos a Seguir para Ejecutar el Codigo-
llamar la funcion greedy_best_first_search en el main
'''''

#---Dependencias---
from Graph import mexDirectedGraph  #Importacion del grafo
from Heuristhic import cities_coordinates, haversine    #Importacion de la heuristica y funcion haversine

#---Funcion Principal---
# Función para implementar el algoritmo Greedy Best-First Search
def greedy_best_first_search(graph, coordinates, start, goal, ver_proceso):
    frontier = [(0, start)]  # Lista para la frontera con tuplas de (prioridad, nodo)
    came_from = {}  # Diccionario para almacenar los nodos visitados y su nodo padre
    came_from[start] = None  # El nodo inicial no tiene un nodo padre
    num_of_iteration = 0    #contador para iteraciones

    while frontier:
        frontier.sort()  # Ordenar la frontera según la prioridad heurística
        _, current_node = frontier.pop(0)  # Obtener el siguiente nodo con mayor prioridad

        #visualiza el proceso
        if ver_proceso == 'y':
            print(current_node)
            print(frontier)

        if current_node == goal:
            break  # Si el nodo objetivo es alcanzado, terminar la búsqueda

        for neighbor in graph[current_node].keys():
            if ver_proceso == 'y':  #Visualiza el proceso
                ("\n Nodo a procesar: ",neighbor)
            if neighbor not in came_from:
                # Calcular la distancia haversine como heurística
                h_value = haversine(coordinates[neighbor], coordinates[goal])
                if ver_proceso == 'y':  #visualiza el proceso
                    print("\n Nodo = {}, Heuristica = {}".format(neighbor,h_value))
                frontier.append((h_value, neighbor))  # Agregar el vecino a la frontera con su prioridad heurística
                came_from[neighbor] = current_node  # Almacenar el nodo padre del vecino en el diccionario
        
        num_of_iteration += 1 #Contar el numero de las iteraciones

    if goal not in came_from:
        return None, None  # Si el nodo objetivo no se alcanza, retornar None para el camino y la distancia

    # Construir el camino desde el nodo inicial hasta el nodo objetivo utilizando el diccionario de nodos padre
    path = [goal]
    current_node = goal
    while current_node != start:
        current_node = came_from[current_node]
        path.append(current_node)
    path.reverse()

    # Calcular la distancia total del camino
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]

    print("\nNumero de Iteraciones: ",num_of_iteration,"\n") #Visualiza iteraciones

    return path, distance

'''''
# Ejemplo de uso
start = 'Cancun'
goal = 'Campeche'

shortest_path, shortest_distance = greedy_best_first_search(mexDirectedGraph, cities_coordinates, start, goal)

if shortest_path:
    print("El camino más corto es:", shortest_path)
    print("La distancia total del camino más corto es:", shortest_distance, "km")
else:
    print("No se encontró un camino desde", start, "hasta", goal)
'''''