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
    ("Madrid",    "Lisboa",     625),
    ("Madrid",    "Barcelona",  622),
    ("Madrid",    "Paris",     1275),
    ("Barcelona", "Paris",     1036),
    ("Barcelona", "Roma",      1358),
    ("Paris",     "Londres",    470),
    ("Paris",     "Bruselas",   312),
    ("Paris",     "Amsterdam",  523),
    ("Paris",     "Zurich",     595),
    ("Londres",   "Amsterdam",  555),
    ("Londres",   "Bruselas",   373),
    ("Bruselas",  "Amsterdam",  225),
    ("Bruselas",  "Berlin",     768),
    ("Amsterdam", "Berlin",     665),
    ("Berlin",    "Varsovia",   572),
    ("Berlin",    "Praga",      347),
    ("Berlin",    "Viena",      639),
    ("Berlin",    "Munich",     585),
    ("Praga",     "Viena",      293),
    ("Praga",     "Varsovia",   641),
    ("Viena",     "Budapest",   245),
    ("Viena",     "Munich",     402),
    ("Munich",    "Zurich",     316),
    ("Munich",    "Roma",       920),
    ("Roma",      "Viena",     1103),
    ("Zurich",    "Roma",       867),
    ("Budapest",  "Varsovia",   698),
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
