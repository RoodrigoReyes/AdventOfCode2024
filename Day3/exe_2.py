import re


def calculate_score_from_regex(file_path):
    """
    Calcula el puntaje (score) basado en la multiplicación de los números extraídos
    mediante una expresión regular.

    El archivo debe contener un string en el que se buscarán los patrones de tipo
    "mul(<número>,<número>)" donde los números tienen entre 1 y 3 dígitos, y las
    instrucciones "do()" y "don't()" para habilitar o deshabilitar las operaciones.

    Args:
        file_path (str): La ruta al archivo de texto que contiene el string de entrada.

    Returns:
        int: El valor del score calculado sumando los productos de los números encontrados
        mientras las instrucciones "mul" están habilitadas.
    """
    # Leer el contenido del archivo
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        content = file.read()

    # Patrón regex para capturar "mul(<número>,<número>)", "do()" y "don't()"
    regex_pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"

    # Encontrar todas las coincidencias
    matches = re.findall(regex_pattern, content)

    # Inicializar estado de habilitación y resultado
    enable = True
    result = 0

    # Procesar coincidencias
    for match in matches:
        if match[0] == "do()":
            enable = True
        elif match[0] == "don't()":
            enable = False
        else:
            if enable:
                result += int(match[1]) * int(match[2])

    return result


if __name__ == "__main__":
    # Ruta del archivo de entrada
    file_path = "Day3/input.txt"

    # Calcular el score usando el archivo dado
    score = calculate_score_from_regex(file_path=file_path)

    # Imprimir el resultado
    print(f"El resultado del ejercicio es: {score}")
