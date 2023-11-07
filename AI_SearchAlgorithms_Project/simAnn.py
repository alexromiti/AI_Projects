#Encargado: Alex Romero Mitiaeva

'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene el algoritmo Simulated Annealing

-Pasos a Seguir para Ejecutar el Codigo-
llamar la funcion simulated_aneealing en el main
'''''

#---Dependencias---
from Graph import mexDirectedGraph  #Importacion del grafo
from Heuristhic import cities_coordinates, haversine    #Importacion de la heuristica y funcion haversine
import random #Importacion de la libreria random
import math #Importacion de la libreria math

#---Funcion Principal---


# Función para implementar el algoritmo Simulated Annealing
def simulated_annealing(graph, coordinates, start, goal, initial_temperature, cooling_rate, ver_proceso):
    current_node = start  # Iniciar desde el nodo inicial
    current_distance = 0  # Variable para almacenar la distancia actual del camino
    path = [start]  # Lista para almacenar el camino
    num_of_iteration = 0    #contador para iteraciones


    # Loop hasta llegar al nodo objetivo
    while current_node != goal:
        neighbors = list(graph[current_node].keys())  # Obtener los vecinos del nodo actual
       
        if ver_proceso == 'y':  #Visualizar proceso
            print("\n Nodo actual = ", current_node)
            print("\n Vecinos = ",neighbors)

        if not neighbors:
            # No hay vecinos alcanzables, terminar la búsqueda
            print("No se encontraron vecinos alcanzables desde el nodo actual:", current_node)
            break

        # Seleccionar un vecino al azar
        next_node = random.choice(neighbors)
        if ver_proceso == 'y':  #Visualizar proceso
            print("\n Nodo a Expandir = ", next_node)

        # Calcular la diferencia de distancia al moverse al vecino
        delta_distance = graph[current_node][next_node]

        # Calcular la probabilidad de aceptación según la diferencia de distancia y la temperatura actual
        probability = math.exp(-delta_distance / initial_temperature)

        # Si se acepta el movimiento, actualizar la distancia y el camino
        if random.random() < probability:
            current_distance += delta_distance
            current_node = next_node
            path.append(current_node)

            if ver_proceso == 'y':  #Visualizar proceso
                print("\n Distancia actual = ", current_distance)

        # Disminuir la temperatura según la tasa de enfriamiento
        initial_temperature *= cooling_rate
        if ver_proceso == 'y':  #Visualizar proceso
            print("\n Temperatura = {}, Probabilidad = {}".format(initial_temperature,probability))
            
        num_of_iteration += 1 #Contar el numero de las iteraciones

    print("\nNumero de Iteraciones: ",num_of_iteration,"\n") #Visualiza iteraciones

    return path, current_distance

'''''
# Ejemplo de uso
start = 'Cancun'
goal = 'Campeche'
initial_temperature = 1000
cooling_rate = 0.99

shortest_path, shortest_distance = simulated_annealing(mexDirectedGraph, cities_coordinates, start, goal,
                                                        initial_temperature, cooling_rate)

if shortest_path:
    print("El camino más corto es:", shortest_path)
    print("La distancia total del camino más corto es:", shortest_distance, "km")
else:
    print("No se encontró un camino desde", start, "hasta", goal)
'''''