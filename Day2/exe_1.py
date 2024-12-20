def list_validate(report):
    """
    Verifica si un reporte cumple las condiciones para incrementar el puntaje.

    Args:
        report (tuple): Una secuencia de números a evaluar.

    Returns:
        bool: True si el puntaje debe incrementarse, False en caso contrario.
    """
    # Inicializamos las banderas para rastrear el comportamiento de la diferencia
    flag_up, flag_down = False, False

    # Recorremos cada par de elementos consecutivos en el reporte
    for index in range(len(report) - 1):
        # Calculamos la diferencia entre el elemento actual y el siguiente
        diff = report[index + 1] - report[index]

        # Verificamos si la diferencia está dentro del rango permitido
        if 0 < abs(diff) < 4:
            # Actualizamos las banderas según la dirección de la diferencia
            flag_up |= diff > 0  # Marca si hay un incremento
            flag_down |= diff < 0  # Marca si hay un decremento
        else:
            # Si alguna diferencia no cumple la condición, salimos del bucle
            return False

    # Si el bucle termina sin interrupciones, verificamos las banderas
    return flag_up != flag_down


def calculate_score(file_path, score=0):
    """
    Calcula el puntaje basado en diferencias absolutas específicas en un archivo de texto.

    El archivo debe contener líneas con números separados por espacios. Cada línea se trata como una secuencia.

    Args:
        file_path (str): La ruta al archivo de texto que contiene los datos.

    Returns:
        int: El valor del score calculado.
    """
    # Abrir el archivo en modo lectura con codificación UTF-8
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        # Leer el contenido del archivo y dividirlo en líneas, transformándolas en tuplas de enteros
        reports = [
            list(map(int, report_line.strip().split()))
            for report_line in file.readlines()
        ]

    for report in reports:
        # Llama a la función auxiliar para determinar si se suma 1 al puntaje
        if list_validate(report):
            score += 1

    return score


if __name__ == "__main__":
    # Ejecutar la función con un archivo de entrada
    score = calculate_score(file_path="Day2/input.txt")
    print(f"El resultado del ejercicio es: {score}")
