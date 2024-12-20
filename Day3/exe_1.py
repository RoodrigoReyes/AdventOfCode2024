import re


def calculate_score_from_regex(file_path):
    """
    Calcula el puntaje (score) basado en la multiplicación de los números extraídos
    mediante una expresión regular.

    El archivo debe contener un string en el que se buscarán los patrones de tipo
    "mul(<número>,<número>)" donde los números tienen entre 1 y 3 dígitos.

    Args:
        file_path (str): La ruta al archivo de texto que contiene el string de entrada.

    Returns:
        int: El valor del score calculado sumando los productos de los números encontrados.
    """
    # Leer el contenido del archivo
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        content = file.read()

    # Patrón regex para capturar "mul(<número>,<número>)"
    regex_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Encontrar todas las coincidencias
    matches = re.findall(regex_pattern, content)

    # Calcular el score sumando los productos de las parejas de números
    score = sum(int(x) * int(y) for x, y in matches)

    return score


if __name__ == "__main__":
    # Calcular el score usando el archivo dado
    score = calculate_score_from_regex(file_path="Day3/input.txt")

    print(f"El resultado del ejercicio es: {score}")
