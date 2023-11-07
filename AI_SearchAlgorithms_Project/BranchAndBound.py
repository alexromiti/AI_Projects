#Encargado: Angel Esqueda Ochoa
'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene el algoritmo Branch and Bound 

-Pasos a Seguir para Ejecutar el Codigo-
llamar la funcion branch_and_bound en el main
'''''

#---Dependencias---
from Graph import mexDirectedGraph  #Importacion del grafo
from Heuristhic import cities_coordinates, haversine    #Importacion de la heuristica y funcion haversine

#---Funcion Principal---

# Función para implementar el algoritmo Branch and Bound con heurística haversine
def branch_and_bound(graph, coordinates, start, goal, ver_proceso):
    visited = set()  # Conjunto para almacenar los nodos visitados
    queue = [(start, 0)]  # Cola para almacenar los nodos a visitar con su distancia acumulada
    num_of_iteration = 0    #contador para iteraciones

    best_path = None  # Mejor camino encontrado
    best_distance = float('inf')  # Mejor distancia encontrada

    # Loop hasta que la cola esté vacía
    while queue:
        current_node, current_distance = queue.pop(0)  # Obtener el próximo nodo y su distancia acumulada

        if ver_proceso == 'y':  #Visualiza el proceso
            print("\n Nodo actual = {}, Distancia acumulada = {}".format(current_node, current_distance))

        if current_node == goal:
            # Si se llega al nodo objetivo, actualizar el mejor camino y distancia si es necesario
            if current_distance < best_distance:
                best_path = [start] + list(visited) + [current_node]
                best_distance = current_distance

        # Marcar el nodo actual como visitado
        visited.add(current_node)

        # Generar los sucesores del nodo actual y agregarlos a la cola
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # Calcular la distancia haversine acumulada al vecino
                distance = current_distance + haversine(coordinates[current_node], coordinates[neighbor])

                # Calcular la cota inferior con la heurística haversine al nodo objetivo
                heuristic = haversine(coordinates[neighbor], coordinates[goal])

                # Calcular la cota superior sumando la distancia acumulada y la heurística al vecino
                upper_bound = distance + heuristic

                if ver_proceso == 'y':  #Visualiza el proceso
                    print("\n Nodo a procesar = ",neighbor,"Heuristica = ",heuristic,"Upper Bound = ",upper_bound)
                # Si la cota inferior es menor que la mejor distancia encontrada, agregar el vecino a la cola
                if upper_bound < best_distance:
                    queue.append((neighbor, distance))

        num_of_iteration += 1 #Contar el numero de las iteraciones

    print("\nNumero de Iteraciones: ",num_of_iteration,"\n") #Visualiza iteraciones

    return best_path, best_distance

'''''
# Ejemplo de uso
start = 'Cancun'
goal = 'Cabo San Lucas'

shortest_path, shortest_distance = branch_and_bound(mexDirectedGraph, cities_coordinates, start, goal)

if shortest_path:
    print("El camino más corto es:", shortest_path)
    print("La distancia total del camino más corto es:", shortest_distance, "km")
else:
    print("No se encontró un camino desde", start, "hasta", goal)
'''''