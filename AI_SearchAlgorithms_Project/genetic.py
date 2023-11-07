#Encargado: Alex Romero Mitiaeva

'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene el algoritmo genetico 

-Pasos a Seguir para Ejecutar el Codigo-
llamar la funcion en a_star en el main
'''''

#---Dependencias---
from Graph import mexDirectedGraph  #Importacion del grafo
from Heuristhic import cities_coordinates, haversine    #Importacion de la heuristica y funcion haversine
import math #Importacion de la libreria Math
import random #Importacion de la libreria random

#---Funcion Principal---

mexDirectedGraph = {
    'Cancun':{'Valladolid':90,'Felipe Carrillo Puerto':100},
    'Valladolid':{'Felipe Carrillo Puerto':90},
    'Felipe Carrillo Puerto':{'Campeche':60},
    'Campeche':{'Ciudad del Carmen':90, 'Merida':90, 'Chetumal':100},
    'Merida':{},
    'Chetumal':{'Francisco Escarcega':110},
    'Francisco Escarcega':{},
    'Ciudad del Carmen':{'Villa Hermosa':90, 'Tuxtla':90},
    'Villa Hermosa':{'Acayucan':90},
    'Tuxtla':{'Acayucan':90},
    'Acayucan':{'Alvarado':110,'Tehuantepec':80},
    'Tehuantepec':{},
    'Alvarado':{'Oaxaca':100},
    'Oaxaca':{'Puerto Angel':90,'Tehuacan':80,'Izucar de Matamoros':90},
    'Tehuacan':{},
    'Puerto Angel':{'Pinotepa Nacional':100},
    'Pinotepa Nacional':{'Acapulco':100},
    'Acapulco':{'Chilpancingo':140},
    'Chilpancingo':{'Iguala':90},
    'Izucar de Matamoros':{'Puebla':90,'Cuernavaca':100},
    'Puebla':{'Cordoba':80,'Ciudad de Mexico':90},
    'Cordoba':{'Veracruz':90,},
    'Veracruz':{},  
    'Iguala':{'Cuernavaca':100,'Ciudad Altamirano':110},
    'Ciudad Altamirano':{'Zihuatanejo':90,'Toluca de Lerdo':100, 'Cuernavaca': 100},
    'Cuernavaca':{'Ciudad de Mexico':100},
    'Toluca de Lerdo':{'Ciudad de Mexico':110},
    'Ciudad de Mexico':{'Tlaxcala':100,'Pachuca de Soto':100,'Queretaro':90},    
    'Pachuca de Soto':{'Tuxpan de Rodriguez Cano':110},
    'Tuxpan de Rodriguez Cano':{'Tampico':80},
    'Tlaxcala':{},
    'Queretaro':{'San Luis Potosi':90,'Atlacomulco':90,'Salamanca':90},
    'Atlacomulco':{},
    'Salamanca':{'Guanajuato':90,'Guadalajara':90},
    'Guanajuato':{'Aguascalientes':80},
    'Morelia':{'Colima':90,'Salamanca':90},
    'Colima':{'Guadalajara':50},   
    'Zihuatanejo':{'Playa Azul':100},
    'Playa Azul':{'Manzanillo':100,'Morelia':100,'Colima':100},
    'Manzanillo':{'Colima':100,'Guadalajara':80},
    'Guadalajara':{'Tepic':110,'Aguascalientes':70},
    'Aguascalientes':{'San Luis Potosi':100},
    'San Luis Potosi':{'Zacatecas':90,'Durango':70},
    'Zacatecas':{},
    'Durango':{'Hidalgo del Parral':90},
    'Tepic':{'Mazatlan':110},
    'Mazatlan':{'Durango':90,'Culiacan':90},
    'Tampico':{'Ciudad Victoria':80},
    'Ciudad Victoria':{'Durango':80,'Soto la Marina':80,'Matamoros':80,'Monterrey':80},
    'Soto la Marina':{},
    'Matamoros':{'Reynosa':90},
    'Monterrey':{'Monclova':70,'Nuevo Laredo':110},
    'Reynosa':{'Nuevo Laredo':100},
    'Nuevo Laredo':{'Piedras Negras':100},
    'Piedras Negras':{'Monclova':100},
    'Monclova':{'Torreon':110,'Ojinaga':140},
    'Torreon':{'Durango':110},
    'Culiacan':{'Topolobampo':110,},
    'Hidalgo del Parral':{'Topolobampo':110,'Culiacan':80,'Chihuahua':130},
    'Chihuahua':{'Janos':90,'Juarez':90},
    'Ojinaga':{'Chihuahua':90},
    'Juarez':{},
    'Janos':{'Agua Prieta':110},
    'Agua Prieta':{'Santa Ana':60},
    'Santa Ana':{'Mexicalli':150},
    'Hermosillo':{'Santa Ana':60},
    'Guaymas':{'Hermosillo':80},
    'Ciudad Obregon':{'Guaymas':80},
    'Topolobampo':{'Ciudad Obregon':90},
    'Mexicalli':{'Tijuana':110,'San Felipe':70},
    'San Felipe':{'Ensenada':50},
    'Tijuana':{'Ensenada':50},
    'Ensenada':{'San Quintin':60},
    'San Quintin':{'Santa Rosalia':60},
    'Santa Rosalia':{'Santo Domingo':60},
    'Santo Domingo':{'La Paz':70},
    'La Paz':{'Cabo San Lucas':70},
    'Cabo San Lucas':{}
}


cities_coordinates = {
    'Cancun': (21.1213285,-86.9192738)
    ,'Valladolid': (20.688114,-88.2204456)
    ,'Felipe Carrillo Puerto': (19.5778903,-88.0630853)
    ,'Campeche': (19.8305682,-90.5798365)
    ,'Merida': (20.9800512,-89.7029587)
    ,'Ciudad del Carmen': (18.6118375,-91.8927345)
    ,'Chetumal': (18.5221567,-88.3397982)
    ,'Villahermosa': (17.9925264,-92.9881407)
    ,'Tuxtla': (16.7459857,-93.1996103)
    ,'Francisco Escarcega': (18.6061556,-90.8176486)
    ,'Acayucan': (17.951096,-94.9306961)
    ,'Tehuantepec': (16.320636,-95.27521)
    ,'Alvarado': (18.7760455,-95.7731952)
    ,'Oaxaca': (17.0812951,-96.7707511)
    ,'Puerto Angel': (15.6679974,-96.4933733)
    ,'Izucar de Matamoros': (18.5980563,-98.5076767)
    ,'Tehuacan': (18.462191,-97.4437333)
    ,'Pinotepa Nacional': (16.3442895,-98.1315923)
    ,'Cuernavaca': (18.9318685,-99.3106054)
    ,'Puebla': (19.040034,-98.2630056)
    ,'Acapulco': (16.8354485,-99.9323491)
    ,'Ciudad de Mexico': (19.3898319,-99.7180148)
    ,'Iguala': (18.3444,-99.5652232)
    ,'Ciudad Altamirano': (18.3547491,-100.6817619)
    ,'Cordoba': (18.8901707,-96.9751108)
    ,'Chilpancingo': (17.5477072,-99.5324349)
    ,'Tlaxcala': (19.4167798,-98.4471127)
    ,'Pachuca de Soto': (20.0825056,-98.8268184)
    ,'Queretaro': (20.6121228,-100.4802576)
    ,'Toluca de Lerdo': (19.294109,-99.6662331)
    ,'Zihuatanejo': (17.6405745,-101.5601369)
    ,'Veracruz': (19.1787635,-96.2113357)
    ,'Tuxpan de Rodriguez Cano': (20.9596561,-97.4158767)
    ,'Atlacomulco': (19.7980152,-99.89317)
    ,'Salamanca': (20.5664927,-101.2176511)
    ,'San Luis Potosi': (22.1127046,-101.0261099)
    ,'Playa Azul': (17.9842581,-102.357616)
    ,'Tampico': (22.2662251,-97.939526)
    ,'Guanajuato': (21.0250928,-101.3296402)
    ,'Morelia': (19.7036417,-101.2761644)
    ,'Guadalajara': (20.6737777,-103.4054536)
    ,'Aguascalientes': (21.8857199,-102.36134)
    ,'Zacatecas': (22.7636293,-102.623638)
    ,'Durango': (24.0226824,-104.7177652)
    ,'Colima': (19.2400444,-103.7636273)
    ,'Manzanillo': (19.0775491,-104.4789574)
    ,'Ciudad Victoria': (23.7409928,-99.1783576)
    ,'Tepic': (21.5009822,-104.9119242)
    ,'Hidalgo del Parral': (26.9489283,-105.8211168)
    ,'Mazatlan': (23.2467283,-106.4923175)
    ,'Soto la Marina': (23.7673729,-98.2157573)
    ,'Matamoros': (25.8433787,-97.5849847)
    ,'Monterrey': (25.6487281,-100.4431819)
    ,'Chihuahua': (28.6708592,-106.2047036)
    ,'Topolobampo': (25.6012747,-109.0687891)
    ,'Culiacan': (24.8049008,-107.4933545)
    ,'Reynosa': (26.0312262,-98.3662435)
    ,'Monclova': (26.907775,-101.4940069)
    ,'Ciudad Juarez': (31.6538179,-106.5890206)
    ,'Janos': (30.8898127,-108.208458)
    ,'Ciudad Obregon': (27.4827355,-110.0844111)
    ,'Torreon': (25.548597,-103.4719562)
    ,'Ojinaga': (29.5453292,-104.4305246)
    ,'Nuevo Laredo': (27.4530856,-99.6881218)
    ,'Agua Prieta': (31.3115272,-109.5855873)
    ,'Guaymas': (27.9272572,-110.9779564)
    ,'Piedras Negras': (28.6910517,-100.5801829)
    ,'Santa Ana': (30.5345457,-111.1580567)
    ,'Hermosillo': (29.082137,-111.059027)
    ,'Mexicali': (32.6137391,-115.5203312)
    ,'Tijuana': (32.4966818,-117.087892)
    ,'San Felipe': (31.009535,-114.8727296)
    ,'Ensenada': (31.8423096,-116.6799816)
    ,'San Quintin': (30.5711324,-115.9588544)
    ,'Santa Rosalia': (27.3408761,-112.2825762)
    ,'Santo Domingo': (25.3487297,-111.9975909)
    ,'La Paz': (24.1164209,-110.3727673)
    ,'Cabo San Lucas': (22.8962253,-109.9505077)
}


def haversine(coord1, coord2):
    """
    Calcula la distancia haversine entre dos coordenadas en grados decimales
    """
    lon1, lat1 = coord1
    lon2, lat2 = coord2

    # Convertir las coordenadas de grados decimales a radianes
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Calcular la diferencia de latitud y longitud
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Aplicar la fórmula haversine
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Radio de la Tierra en kilómetros
    r = 6371

    # Calcular la distancia haversine en kilómetros
    distance = c * r

    return distance


class Individual:
    def __init__(self, cities):
        """
        Constructor de la clase Individual

        Args:
        - cities (list): Lista de ciudades en el grafo
        """
        self.cities = cities
        self.fitness = 0  # Valor de aptitud del individuo

    def generate_random(self):
        """
        Genera un individuo aleatorio
        """
        self.cities = random.sample(self.cities, len(self.cities))  # Genera una permutación aleatoria de las ciudades

    def calculate_fitness(self, heuristic_func):
        """
        Calcula la aptitud del individuo utilizando la función heurística

        Args:
        - heuristic_func (function): Función heurística para estimar la distancia entre dos ciudades
        """
        total_distance = 0
        for i in range(len(self.cities)-1):
            city1 = self.cities[i]
            city2 = self.cities[i+1]
            total_distance += heuristic_func(city1, city2)
        self.fitness = total_distance

class GeneticAlgorithm:
    def __init__(self, cities, heuristic_func, population_size=100, crossover_rate=0.8, mutation_rate=0.2):
        """
        Constructor de la clase GeneticAlgorithm

        Args:
        - cities (list): Lista de ciudades en el grafo
        - heuristic_func (function): Función heurística para estimar la distancia entre dos ciudades
        - population_size (int): Tamaño de la población (por defecto: 100)
        - crossover_rate (float): Tasa de cruzamiento (por defecto: 0.8)
        - mutation_rate (float): Tasa de mutación (por defecto: 0.2)
        """
        self.cities = cities
        self.heuristic_func = heuristic_func
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = []
        self.best_individual = None

    def generate_initial_population(self):
        """
        Genera la población inicial de individuos
        """
        for _ in range(self.population_size):
            individual = Individual(self.cities)
            individual.generate_random()
            self.population.append(individual)

    def selection(self):
        """
        Realiza la selección de individuos utilizando el método de selección por torneo
        """
        selected_individuals = []
        for _ in range(self.population_size):
            # Seleccionar dos individuos al azar
            individual1 = random.choice(self.population)
            individual2 = random.choice(self.population)

            # Comparar las aptitudes de los dos individuos
            if individual1.fitness < individual2.fitness:
                selected_individuals.append(individual1)
            else:
                selected_individuals.append(individual2)

        # Reemplazar la población actual con los individuos seleccionados
        self.population = selected_individuals

    def crossover(self):
        """
        Realiza el cruzamiento de individuos utilizando el operador de cruce de orden (OX)
        """
        for i in range(0, self.population_size, 2):
            # Cruzar dos individuos con una tasa de cruzamiento dada
            if random.random() < self.crossover_rate:
                individual1 = self.population[i]
                individual2 = self.population[i+1]

                # Elegir dos puntos de corte al azar
                cutpoint1, cutpoint2 = sorted(random.sample(range(len(self.cities)), 2))

                # Realizar el cruzamiento utilizando el operador de cruce de orden (OX)
                offspring1 = [-1] * len(self.cities)
                offspring2 = [-1] * len(self.cities)

                offspring1[cutpoint1:cutpoint2+1] = individual1.cities[cutpoint1:cutpoint2+1]
                offspring2[cutpoint1:cutpoint2+1] = individual2.cities[cutpoint1:cutpoint2+1]

                idx1 = cutpoint2 + 1
                idx2 = cutpoint2 + 1
                for city in individual2.cities[cutpoint2+1:] + individual2.cities[:cutpoint2+1]:
                    if city not in offspring1:
                        offspring1[idx1 % len(self.cities)] = city
                        idx1 += 1

                    if city not in offspring2:
                        offspring2[idx2 % len(self.cities)] = city
                        idx2 += 1

                # Actualizar la población con los descendientes generados
                self.population[i].cities = offspring1
                self.population[i+1].cities = offspring2

    def mutation(self):
        """
        Realiza la mutación de individuos intercambiando dos ciudades en el camino
        """
        for individual in self.population:
            # Mutar un individuo con una tasa de mutación dada
            if random.random() < self.mutation_rate:
                # Elegir dos ciudades al azar para intercambiar
                city1, city2 = random.sample(range(len(self.cities)), 2)

                # Intercambiar las ciudades en el camino del individuo
                individual.cities[city1], individual.cities[city2] = individual.cities[city2], individual.cities[city1]

    def evaluate_fitness(self):
        """
        Evalúa la aptitud de cada individuo en la población utilizando la función heurística
        """
        for individual in self.population:
            individual.calculate_fitness(self.heuristic_func)

    def get_best_individual(self):
        """
        Obtiene el mejor individuo en la población
        """
        best_individual = min(self.population, key=lambda x: x.fitness)
        return best_individual

    def run(self):
        """
        Ejecuta el algoritmo genético completo
        """
        # Inicializar la población aleatoriamente
        self.initialize_population()

        # Realizar las iteraciones del algoritmo genético
        for _ in range(self.num_generations):
            # Evaluar la aptitud de la población actual
            self.evaluate_fitness()

            # Obtener el mejor individuo en la población actual
            best_individual = self.get_best_individual()

            # Imprimir la información del mejor individuo en esta generación
            print("Generación: {}, Mejor Aptitud: {}".format(_, best_individual.fitness))

            # Realizar la selección de individuos
            self.selection()

            # Realizar el cruzamiento de individuos
            self.crossover()

            # Realizar la mutación de individuos
            self.mutation()

        # Evaluar la aptitud de la población final
        self.evaluate_fitness()

        # Obtener el mejor individuo en la población final
        best_individual = self.get_best_individual()

        # Imprimir la información del mejor individuo en la población final
        print("Generación: {}, Mejor Aptitud: {}".format(self.num_generations, best_individual.fitness))

        # Devolver el mejor individuo como resultado
        return best_individual
    
# Crear una instancia del algoritmo genético
genetic_algorithm = GeneticAlgorithm(cities=['Cancun', 'Valladolid', 'Felipe Carrillo Puerto', 'Campeche'],
                                     cities_coordinates={'Cancun': (21.1213285,-86.9192738),
                                                         'Valladolid': (20.688114,-88.2204456),
                                                         'Felipe Carrillo Puerto': (19.5798833,-88.0452939),
                                                         'Campeche': (19.845438,-90.5349152)},
                                     population_size=100,
                                     num_generations=100,
                                     crossover_rate=0.8,
                                     mutation_rate=0.2)

# Ejecutar el algoritmo genético
best_individual = genetic_algorithm.run()

# Obtener el mejor camino encontrado
best_path = best_individual.path

# Imprimir el mejor camino encontrado
print("Mejor Camino: ", best_path)

