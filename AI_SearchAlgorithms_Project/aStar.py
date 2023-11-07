#Encargado: Leonardo Kenji Minemura Suazo 
'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene el algoritmo A* 

-Pasos a Seguir para Ejecutar el Codigo-
llamar la funcion a_star en el main
'''''

#---Dependencias---
from Graph import mexDirectedGraph  #Importacion del grafo
from Heuristhic import cities_coordinates, haversine    #Importacion de la heuristica y funcion haversine

#---Funcion Principal---

# Función para implementar el algoritmo A*
def a_star(graph, coordinates, start, goal, ver_proceso):
    frontier = [(0, start)]  # Lista para mantener la frontera, donde cada elemento es una tupla (f(n), nodo)
    came_from = {}  # Diccionario para almacenar los nodos visitados y su nodo padre
    g_scores = {node: float('inf') for node in graph.keys()}  # Diccionario para almacenar la distancia acumulada
    g_scores[start] = 0  # La distancia acumulada del nodo inicial es 0
    came_from[start] = None  # El nodo inicial no tiene un nodo padre
    h_value = haversine(coordinates[start], coordinates[goal])  # Calcular la distancia heurística para el nodo inicial
    num_of_iteration = 0    #contador para iteraciones

    while frontier:
        frontier.sort(key=lambda x: x[0])  # Ordenar la frontera por prioridad f(n)
        _, current_node = frontier.pop(0)  # Obtener el siguiente nodo con menor prioridad

        #Visualiza el proceso
        if ver_proceso == 'y':
            print(current_node)
            print(frontier)


        if current_node == goal:
            break  # Si el nodo objetivo es alcanzado, terminar la búsqueda

        for neighbor in graph[current_node].keys():
            # Calcular la distancia acumulada del vecino a través del nodo actual
            tentative_g_score = g_scores[current_node] + graph[current_node][neighbor]
            if ver_proceso == 'y':  #Visualiza el proceso
                ("\n Nodo a procesar: ",neighbor)

            if tentative_g_score < g_scores[neighbor]:
                # Actualizar la distancia acumulada y el nodo padre del vecino
                g_scores[neighbor] = tentative_g_score
                came_from[neighbor] = current_node

                # Calcular la distancia heurística para el vecino
                h_value = haversine(coordinates[neighbor], coordinates[goal])
                f_value = tentative_g_score + h_value  # Calcular el valor f(n) = g(n) + h(n)
                if ver_proceso == 'y':  #visualiza el proceso
                    print("\n Nodo = {}, Valor f(n) = {}".format(neighbor,f_value))
                frontier.append((f_value, neighbor))  # Agregar el vecino a la frontera con su prioridad f(n)

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

shortest_path, shortest_distance = a_star(mexDirectedGraph, cities_coordinates, start, goal)

if shortest_path:
    print("El camino más corto es:", shortest_path)
    print("La distancia total del camino más corto es:", shortest_distance, "km")
else:
    print("No se encontró un camino desde", start, "hasta", goal)
'''''