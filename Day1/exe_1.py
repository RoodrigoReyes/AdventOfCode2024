def calculate_score(file_path):
    """
    Calcula el puntaje (score) basado en la diferencia absoluta entre los valores
    ordenados de dos columnas en un archivo de texto.

    El archivo debe contener dos columnas de números enteros separados por espacios.

    Args:
        file_path (str): La ruta al archivo de texto que contiene los datos.

    Returns:
        int: El valor del score calculado.
    """
    # Abrir el archivo en modo lectura con codificación UTF-8
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        # Leer el contenido del archivo y dividirlo en líneas
        lines = file.read().split("\n")

    # Dividir las líneas en dos columnas y convertirlas a enteros
    # map(int, line.split()) convierte cada línea en una tupla de dos enteros
    # zip(*[...]) separa las columnas en dos listas independientes
    _left, _right = zip(*[map(int, line.split()) for line in lines])

    # Calcular el score sumando la diferencia absoluta entre los valores
    # ordenados de las dos listas
    score = sum(abs(x - y) for x, y in zip(sorted(_left), sorted(_right)))

    return score


if __name__ == "__main__":

    score = calculate_score(file_path="Day1/input.txt")
    print(f"El resultado del ejercicio es: {score}")
