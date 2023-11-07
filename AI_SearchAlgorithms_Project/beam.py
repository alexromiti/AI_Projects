#Encargado: Angel Esqueda Ochoa
'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene el algoritmo beam search 

-Pasos a Seguir para Ejecutar el Codigo-
llamar la funcion beam search en el main
''''' 

#---Dependencias---
from Graph import mexDirectedGraph  #Importacion del grafo
from Heuristhic import cities_coordinates, haversine    #Importacion de la heuristica y funcion haversine

#---Funcion Principal---

# Función para implementar el algoritmo Beam Search
def beam_search(graph, start, goal, beam_width, ver_proceso):
    frontier = [(start, 0)]  # Lista para mantener la frontera, donde cada elemento es una tupla (nodo, costo acumulado)
    came_from = {}  # Diccionario para almacenar los nodos visitados y su nodo padre
    num_of_iteration = 0    #contador para iteraciones
    current_node = start


    while frontier:
        frontier.sort(key=lambda x: x[1])  # Ordenar la frontera por costo acumulado
        frontier = frontier[:beam_width]  # Limitar la frontera al ancho del beam

        #visualiza el proceso
        if ver_proceso == 'y':
            print(current_node)
            print(frontier)

        new_frontier = []  # Lista para almacenar los sucesores de los nodos en la frontera actual

        for current_node, current_cost in frontier:
            if current_node == goal:
                break  # Si el nodo objetivo es alcanzado, terminar la búsqueda

            for neighbor in graph[current_node].keys():
                if neighbor not in came_from:
                    if ver_proceso == 'y':  #Visualiza el proceso
                        ("\n Nodo a procesar: ",neighbor)
                    # Si el vecino no ha sido visitado, agregarlo a la nueva frontera con su costo acumulado
                    new_cost = current_cost + graph[current_node][neighbor]
                    new_frontier.append((neighbor, new_cost))
                    came_from[neighbor] = current_node
                    if ver_proceso == 'y':  #visualiza el proceso
                        print("\n Nodo = {}, Costo = {}".format(neighbor,new_cost))

        frontier = new_frontier  # Actualizar la frontera con los nuevos sucesores

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
beam_width = 3  # Ancho del beam

shortest_path, shortest_distance = beam_search(mexDirectedGraph, start, goal, beam_width)

if shortest_path:
    print("El camino más corto es:", shortest_path)
    print("La distancia total del camino más corto es:", shortest_distance, "km")
else:
    print("No se encontró un camino desde", start, "hasta", goal)
'''''