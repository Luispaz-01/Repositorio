# Definimos las ciudades, días de la semana y semanas
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Creamos una matriz 3D para almacenar las temperaturas
# Dimensiones: [ciudades][semanas][días de la semana]
temperaturas = [
    [   # Ciudad A
        [72, 75, 78, 74, 76, 79, 80],  # Semana 1
        [70, 73, 77, 75, 78, 81, 82],  # Semana 2
        [68, 71, 74, 72, 75, 78, 79],  # Semana 3
        [69, 72, 76, 74, 77, 80, 81]   # Semana 4
    ],
    [   # Ciudad B
        [60, 62, 65, 64, 67, 70, 72],  # Semana 1
        [61, 63, 66, 65, 68, 71, 73],  # Semana 2
        [59, 61, 64, 63, 66, 69, 71],  # Semana 3
        [62, 64, 67, 66, 69, 72, 74]   # Semana 4
    ],
    [   # Ciudad C
        [85, 87, 90, 88, 89, 91, 92],  # Semana 1
        [84, 86, 89, 87, 88, 90, 91],  # Semana 2
        [83, 85, 88, 86, 87, 89, 90],  # Semana 3
        [82, 84, 87, 85, 86, 88, 89]   # Semana 4
    ]
]

def calcular_promedios(temperaturas):
    """Calcula el promedio de temperaturas para cada ciudad."""
    promedios = []
    for ciudad in temperaturas:
        promedios_ciudad = [sum(semana) / len(semana) for semana in ciudad]
        promedios.append(promedios_ciudad)
    return promedios

def imprimir_promedios(ciudades, promedios):
    """Imprime los promedios de temperaturas para cada ciudad."""
    for ciudad_idx, ciudad in enumerate(ciudades):
        print(f"Promedios de temperaturas para {ciudad}:")
        for semana_idx, promedio in enumerate(promedios[ciudad_idx]):
            print(f"  Semana {semana_idx + 1}: {promedio:.2f} °C")

# Calcular y mostrar los promedios
promedios = calcular_promedios(temperaturas)
imprimir_promedios(ciudades, promedios)