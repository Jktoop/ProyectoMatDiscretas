**Proyecto Matemáticas Discretas**
Ingeniería Civil en Informática - Sección 2

## Integrantes
- Sakin Contreras
- Joaquín Carrillo
- Kevin Inalaf

## Descripción del proyecto

Este proyecto modela una red de 15 ciudades europeas como un grafo ponderado
`G = (V, E, W)` donde:
- `V` = ciudades (vértices)
- `E` = conexiones reales entre ciudades (aristas)
- `W(e)` = distancia en km de cada conexión (peso)

La aplicación permite seleccionar una ciudad de origen yuna de destino, y calcula la "ruta optima" (de menor distancia total ) usando el algoritmo de Dijkstra.

## Ciudades incluidas

Madrid, Lisboa, Barcelona, Paris, Londres, Bruselas, Amsterdam, Berlin, Varsovia,
Praga, Viena, Budapest, Munich, Zúrich, Roma.

## Algoritmo utilizado

"Dijkstra" fue seleccionado porque el grafo tiene pesos positivos y es conexo.
Implementando a mano sin el uso de librerías externas, en cada itineracion se recorre la lista de ciudades no visitadas para encontrar la de menor distancia acumulada.

## Estructura del repositorio

ProyectoMatDisrcetas
-Main.py          # Aplicación con interfaz gráfica
-dijkstra.py       # Implementación del algoritmo de Dijkstra
-ciudades.py        # Datos del grafo (ciudades y conexiones)
-README.md            # Este archivo
-requerimientos.txt     # Dependencias del proyecto
## Instruciones de ejecución

### 1. Ejecutar la aplicación

python Main.py

### 2. Uso de la interfaz
1. Seleccionar la ciudad de origen en el menú.
2. Seleccionar la ciudad de destino en el menú.
3. Hacer clic en Calcular Ruta Optima.
4. La ruta se destacará en el grafo y el panel mostrará la secuencia de ciudades y el total de km.

## Librerías utilizadas 

| Librería      |   Uso    |
|---------------|----------|
| `tkinter`     | Interfaz gráfica de python |
| `matplotlib`  | Renderizado del grafo |

## Fuente de los datos

Las distancias entre ciudades son distancias aproximadas por carretera obtenidas de 
Google Maps y Rome2Rio para cada par de ciudades conectadas.