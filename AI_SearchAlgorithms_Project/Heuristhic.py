'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene la heuristica

-Pasos a Seguir para Ejecutar el Codigo-
Importar el archivo cuando se requiera
'''''
#---Dependencia---
import math #para realizar operaciones

cities_coordinates = {
    'Cancun': (21.1213285,-86.9192738)
    ,'Valladolid': (20.688114,-88.2204456)
    ,'Felipe Carrillo Puerto': (19.5778903,-88.0630853)
    ,'Campeche': (19.8305682,-90.5798365)
    ,'Merida': (20.9800512,-89.7029587)
    ,'Ciudad del Carmen': (18.6118375,-91.8927345)
    ,'Chetumal': (18.5221567,-88.3397982)
    ,'Villa Hermosa': (17.9925264,-92.9881407)
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
    ,'Mexicalli': (32.6137391,-115.5203312)
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

