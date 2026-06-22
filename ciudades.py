# V = conjunto de vertices (ciudades)
CIUDADES = [
    "Madrid",
    "Paris",
    "Londres",
    "Berlin",
    "Roma",
    "Amsterdam",
    "Bruselas",
    "Viena",
    "Zurich",
    "Barcelona",
    "Lisboa",
    "Praga",
    "Varsovia",
    "Budapest",
    "Munich"
]

# E = conjunto de aristas con peso w = distancia en km
# formato: (ciudad_origen, ciudad_destino, distancia_km)
CONEXIONES = [
    ("Madrid",    "Lisboa",     635),
    ("Madrid",    "Barcelona",  621),
    ("Madrid",    "Paris",     1270),
    ("Barcelona", "Paris",     1038),
    ("Barcelona", "Roma",      1440),
    ("Paris",     "Londres",    461),
    ("Paris",     "Bruselas",   307),
    ("Paris",     "Amsterdam",  503),
    ("Paris",     "Zurich",     618),
    ("Londres",   "Amsterdam",  537),
    ("Londres",   "Bruselas",   370),
    ("Bruselas",  "Amsterdam",  211),
    ("Bruselas",  "Berlin",     783),
    ("Amsterdam", "Berlin",     659),
    ("Berlin",    "Varsovia",   574),
    ("Berlin",    "Praga",      354),
    ("Berlin",    "Viena",     1085),
    ("Berlin",    "Munich",     592),
    ("Praga",     "Viena",      333),
    ("Praga",     "Varsovia",   656),
    ("Viena",     "Budapest",   243),
    ("Viena",     "Munich",     440),
    ("Munich",    "Zurich",     316),
    ("Munich",    "Roma",      1185),
    ("Roma",      "Viena",     1189),
    ("Zurich",    "Roma",       845),
    ("Budapest",  "Varsovia",   549),
]

# posiciones para dibujar el grafo 
POSICIONES = {
    "Madrid":    (-3.7,  40.4),
    "Lisboa":    (-9.1,  38.7),
    "Barcelona": ( 2.2,  41.4),
    "Paris":     ( 2.3,  48.9),
    "Londres":   (-0.1,  51.5),
    "Bruselas":  ( 4.4,  50.8),
    "Amsterdam": ( 4.9,  52.4),
    "Berlin":    (13.4,  52.5),
    "Varsovia":  (21.0,  52.2),
    "Praga":     (14.5,  50.1),
    "Viena":     (16.4,  48.2),
    "Budapest":  (19.0,  47.5),
    "Munich":    (11.6,  48.1),
    "Zurich":    ( 8.5,  47.4),
    "Roma":      (12.5,  41.9),
}
