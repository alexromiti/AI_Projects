'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 3.2
Este proyecto consiste en 9 estrategias de busqueda como, GBFS, A*, Weighted A*, Beam Search, Steepest Hill Climbing Search, Stochastic Hill Climbing Search, Simulated Annealing, Branch and Bound y Algoritmo Genetico
 vistos en la clase de Inteligencia Artificial. Cada estrategia tiene su propia técnica y algoritmo para encontrar soluciones óptimas en problemas de búsqueda, ya sea mediante el uso de heurísticas, algoritmos de optimización o búsqueda en espacios de solución.
 En este proyecto, see puede apreciar una comparacion mas clara de estas estrategias para entender sus fortalezas y debilidades.  

-Pasos a Seguir para Ejecutar el Codigo-
Asegúrese de que todas las dependencias necesarias estén instaladas.
Importe los archivos necesarios.
Se mostrara un mensaje de bienvenida al usuario y proporcione un menú que enumere los ocho algoritmos de búsqueda de rutas disponibles.
Se solicitara al usuario que ingrese la opción de algoritmo que desea utilizar, o "q" para salir.
Si el usuario ingresa una opción válida, muestre un mensaje que indique el algoritmo seleccionado.
Se solicitara al usuario que ingrese el nodo de inicio y el nodo objetivo para la ruta que desea calcular.
Se verificara que los nodos ingresados existan en el grafo.
Se le pregunte al usuario si desea ver el proceso de búsqueda. 'y' para mostrar el proceso, 'n' para no mostrar
Se Llamara a la función correspondiente para ejecutar el algoritmo seleccionado y pasar los parámetros necesarios.
Imprimira el numero de iteraciones, la ruta más corta y la distancia más corta encontrada por el algoritmo.
Si el usuario desea ver el proceso de búsqueda, muestre la información correspondiente.
Una vez que haya finalizado esto, el codigo nos regresa al menu principal y podra seleccionar otro algoritmo de busqueda con nuevos nodo de inicio y objetivo o salir del programa. 
'''''

#Encargados - Todos los integrantes

#---Dependencias---
import aStar, GBFS, wAStar, beam, Steep_Hill, Stoch_Hill, simAnn, BranchAndBound #Importacion de archivos 
from Graph import mexDirectedGraph #Importacion del grafo
from Heuristhic import cities_coordinates, haversine #Importacion de la heuristica y funcion harversine


#---Funcion principal---
node_names = ['Cancun', 'Valladolid', 'Felipe Carrillo Puerto', 'Campeche', 'Merida', 'Ciudad del Carmen', 'Chetumal', 'Villahermosa', 'Tuxtla', 'Francisco Escarcega', 'Acayucan', 'Tehuantepec', 'Alvarado', 'Oaxaca', 'Puerto Angel', 'Izucar de Matamoros', 'Tehuacan', 'Pinotepa Nacional', 'Cuernavaca', 'Puebla', 'Acapulco', 'Ciudad de Mexico', 'Iguala', 'Ciudad Altamirano', 'Cordoba', 'Chilpancingo', 'Tlaxcala', 'Pachuca de Soto', 'Queretaro', 'Toluca de Lerdo', 'Zihuatanejo', 'Veracruz', 'Tuxpan de Rodriguez Cano', 'Atlacomulco', 'Salamanca', 'San Luis Potosi', 'Playa Azul', 'Tampico', 'Guanajuato', 'Morelia', 'Guadalajara', 'Aguascalientes', 'Zacatecas', 'Durango', 'Colima', 'Manzanillo', 'Ciudad Victoria', 'Tepic', 'Hidalgo del Parral', 'Mazatlan', 'Soto la Marina', 'Matamoros', 'Monterrey', 'Chihuahua', 'Topolobampo', 'Culiacan', 'Reynosa', 'Monclova', 'Ciudad Juarez', 'Janos', 'Ciudad Obregon', 'Torreon', 'Ojinaga', 'Nuevo Laredo', 'Agua Prieta', 'Guaymas', 'Piedras Negras', 'Santa Ana', 'Hermosillo', 'Mexicali', 'Tijuana', 'San Felipe', 'Ensenada', 'San Quintin', 'Santa Rosalia', 'Santo Domingo', 'La Paz', 'Cabo San Lucas']
ver_proceso = 'n'   #Variable para ver proceso. Inicializada en 'n'  lk 

print('\n\nBienvenido al programa de recorridos! \n')
print('A continuación se te presentará un menú con los distintos algoritmos ' + 
      'de recorrido para encontrar la ruta que necesites\n\n')
print('1)Greedy best first\n2)A*\n3)Weighted a*\n4)Beam\n5)Steepest Hill climbing\n6)Stochastic Hill Climbing\n7)Simulated Annealing\n8)Branch and Bound\n\n')
while True:
    alghOpt = input('Por favor ingresa la opción del algoritmo que quieres utilizar (1-8), o ingresa "q" para salir: ')
    if alghOpt.isdigit():
        alghOpt = int(alghOpt)
        if 1 <= alghOpt <= 8:

            # Definir el diccionario de opciones
            switch_dict = {
                1: 'Opción 1: GBFS',
                2: 'Opción 2: A*',
                3: 'Opción 3: A* Weoighted',
                4: 'Opción 4: Beam',
                5: 'Opción 5: Steepest Hill Climbing',
                6: 'Opción 6: Stochastic Hill Climbing',
                7: 'Opción 7: Simulated Annealing',
                8: 'Opcion 8: Branch and Bound'
            }

            # Obtener la opción del diccionario
            option = switch_dict.get(alghOpt)

            if option:
                print(option)

                while True:
                    # Aqui se solicita el nodod Inicial y Objetivo
                    start = input("Digite el nodo Inicial: ")
                    goal = input("Digite el nodo Objetivo: ")

                    #Estandarizar Nombre de los nodos 
                    start = start.title()
                    goal = goal.title()

                    #checar si el nodo ingresado existe 
                    if start and goal in node_names:
                        break
                    else:
                        print("El Nodo digitado no exite")

                # Aqui se le pregunta al usuario se desea ver el proceso o no 
                while True:
                    ver_proceso = input("Deseas ver el proceso ?[y/n]: ")
                    if ver_proceso == 'y' or 'n':
                        break
                    else:
                        print("Digita y para YES y n para NO")

                # Aquí puedes llamar a la función correspondiente para ejecutar el algoritmo seleccionado
                # por ejemplo: ejecutar_algoritmo(alghOpt)

                if alghOpt == 1:
                    #Parametro a ingresar: Grapho, Heuristica, Nodo inicial, Nodo objetivo, Mostrar el proceso o no. 
                    # Regresa: camino mas corto y su distancia 
                    shortest_path, shortest_distance = GBFS.greedy_best_first_search(mexDirectedGraph, cities_coordinates, start, goal, ver_proceso)

                elif alghOpt == 2:
                    #Parametro a ingresar: Grapho, Heuristica, Nodo inicial, Nodo objetivo, Mostrar el proceso o no. 
                    # Regresa: camino mas corto y su distancia 
                    shortest_path, shortest_distance = aStar.a_star(mexDirectedGraph, cities_coordinates, start, goal, ver_proceso)

                elif alghOpt == 3:
                    #Parametro a ingresar: Grapho, Heuristica, Nodo inicial, Nodo objetivo, Peso, Mostrar el proceso o no. 
                    # Regresa: camino mas corto y su distancia 
                    weight = int (input("Digite el Peso: "))
                    shortest_path, shortest_distance = wAStar.weighted_a_star(mexDirectedGraph, cities_coordinates, start, goal, weight, ver_proceso)

                elif alghOpt == 4:
                    #Parametro a ingresar: Grapho, Heuristica, Nodo inicial, Nodo objetivo, Anchura del beam, Mostrar el proceso o no. 
                    # Regresa: camino mas corto y su distancia 
                    beam_w = int(input("Digite la anchura del BEAM: "))
                    shortest_path, shortest_distance = beam.beam_search(mexDirectedGraph, start, goal, beam_w, ver_proceso)

                elif alghOpt == 5:
                    #Parametro a ingresar: Grapho, Heuristica, Nodo inicial, Nodo objetivo, Mostrar el proceso o no. 
                    # Regresa: camino mas corto y su distancia 
                    shortest_path, shortest_distance = Steep_Hill.steepest_hill_climbing(mexDirectedGraph, cities_coordinates, start, goal, ver_proceso)

                elif alghOpt == 6:
                    #Parametro a ingresar: Grapho, Heuristica, Nodo inicial, Nodo objetivo, Mostrar el proceso o no. 
                    # Regresa: camino mas corto y su distancia 
                    shortest_path, shortest_distance = Stoch_Hill.stochastic_hill_climbing(mexDirectedGraph, cities_coordinates, start, goal, ver_proceso)

                elif alghOpt == 7:
                    #Parametro a ingresar: Grapho, Heuristica, Nodo inicial, Nodo objetivo, Temperatura inicial, Cooling rate, Mostrar el proceso o no. 
                    # Regresa: camino mas corto y su distancia 
                    initial_temp = float(input("Digite la temperatura Inicial: "))
                    cooling_rate = float(input("Digite el cooling rate: "))
                    shortest_path, shortest_distance = simAnn.simulated_annealing(mexDirectedGraph, cities_coordinates, start, goal, initial_temp, cooling_rate, ver_proceso)

                elif alghOpt == 8:
                    #Parametro a ingresar: Grapho, Heuristica, Nodo inicial, Nodo objetivo, Mostrar el proceso o no. 
                    # Regresa: camino mas corto y su distancia 
                    shortest_path, shortest_distance = BranchAndBound.branch_and_bound(mexDirectedGraph, cities_coordinates, start, goal, ver_proceso)

                
                if shortest_path:
                    print("El camino más corto es:", shortest_path)
                    print("La distancia total del camino más corto es:", shortest_distance, "km")
                else:
                    print("No se encontró un camino desde", start, "hasta", goal)

            else:
                print('Opción inválida')
        else:
            print('Por favor ingresa un número entre 1 y 8\n')
    elif alghOpt.lower() == 'q':
        print('Saliendo del programa...')
        break
    else:
        print('Por favor ingresa un número válido o "q" para salir del programa\n')



        



