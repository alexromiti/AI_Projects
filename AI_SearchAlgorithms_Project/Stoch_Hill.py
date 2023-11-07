#Encargado: Alex Romero Mitiaeva

'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene el algoritmo Stochastic hill climbing 

-Pasos a Seguir para Ejecutar el Codigo-
llamar la funcion stochastic_hill_climbing en el main
'''''

#---Dependencias---
from Graph import mexDirectedGraph  #Importacion del grafo
from Heuristhic import cities_coordinates, haversine    #Importacion de la heuristica y funcion haversine
import random #Importacion del modulo random

#---Funcion Principal---

# Función para implementar el algoritmo de Stochastic Hill Climbing
def stochastic_hill_climbing(graph, coordinates, start, goal, ver_proceso):
    current_node = start
    current_distance = 0
    path = [start]
    num_of_iteration = 0    #contador para iteraciones

    # Loop hasta llegar al nodo objetivo
    while current_node != goal:
        neighbors = list(graph[current_node].keys())

        if ver_proceso == 'y':  #Visualizar proceso
            print(current_node)

        if not neighbors:
            # No hay vecinos alcanzables, terminar la búsqueda
            print("No se encontraron vecinos alcanzables desde el nodo actual:", current_node)
            break

        # Calcular las distancias haversine a los vecinos
        h_values = []
        for neighbor in neighbors:
            if ver_proceso == 'y':  #Visualiza el proceso
                ("\n Nodo a procesar: ",neighbor)
            h_value = haversine(coordinates[current_node], coordinates[neighbor])
            h_values.append(h_value)
            if ver_proceso == 'y':  #visualiza el proceso
                    print("\n Nodo = {}, Heuristica = {}".format(neighbor,h_value))

        # Seleccionar un vecino al azar
        min_h_value = min(h_values)
        best_neighbors = [neighbors[i] for i in range(len(neighbors)) if h_values[i] == min_h_value]
        next_node = random.choice(best_neighbors)

        # Actualizar la distancia y el camino
        current_distance += graph[current_node][next_node]
        path.append(next_node)

        # Moverse al siguiente nodo
        current_node = next_node
        if ver_proceso == 'y': #Visualizar proceso
            print("\n Vecino seleccionado = ",next_node,"Distancia total = ",current_distance)

        num_of_iteration += 1 #Contar el numero de las iteraciones

    print("\nNumero de Iteraciones: ",num_of_iteration,"\n") #Visualiza iteraciones

    return path, current_distance

'''''
# Ejemplo de uso
start = 'Cancun'
goal = 'Cabo San Lucas'

shortest_path, shortest_distance = stochastic_hill_climbing(mexDirectedGraph, cities_coordinates, start, goal)

if shortest_path:
    print("El camino más corto es:", shortest_path)
    print("La distancia total del camino más corto es:", shortest_distance, "km")
'''''





    
   



