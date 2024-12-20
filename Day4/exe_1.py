def count_word_occurrences(grid, word):
    """Cuenta las ocurrencias de una palabra en una matriz de caracteres en todas las direcciones posibles.

    La palabra puede aparecer en las siguientes direcciones:
    - Derecha, izquierda, arriba, abajo
    - Diagonales (hacia arriba y hacia abajo, en ambas direcciones)

    Args:
        grid (list[list[str]]): Matriz de caracteres.
        word (str): Palabra a buscar.

    Returns:
        int: Número total de veces que la palabra aparece en la matriz.
    """
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    def search_direction(r, c, dr, dc):
        """Busca la palabra en una dirección específica desde una posición inicial.

        Args:
            r (int): Fila inicial.
            c (int): Columna inicial.
            dr (int): Incremento en la fila por cada paso.
            dc (int): Incremento en la columna por cada paso.

        Returns:
            int: 1 si la palabra se encuentra en la dirección especificada, de lo contrario 0.
        """
        word_temp = ""
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return 0
            else:
                word_temp += word[i]
        return 1

    # Direcciones posibles: (dr, dc)
    directions = [
        (0, 1),  # Derecha
        (1, 0),  # Abajo
        (1, 1),  # Diagonal hacia abajo derecha
        (-1, 0),  # Arriba
        (0, -1),  # Izquierda
        (-1, -1),  # Diagonal hacia arriba izquierda
        (1, -1),  # Diagonal hacia abajo izquierda
        (-1, 1),  # Diagonal hacia arriba derecha
    ]

    # Iterar sobre cada celda de la matriz
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                count += search_direction(r, c, dr, dc)

    return count


def read_grid_from_file(file_path):
    """Lee una matriz de caracteres desde un archivo.

    Args:
        file_path (str): Ruta del archivo a leer.

    Returns:
        list[list[str]]: Matriz de caracteres.
    """
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        content = file.readlines()
    return [list(row.strip()) for row in content]


if __name__ == "__main__":
    # Ruta del archivo de entrada
    file_path = "Day4/input.txt"

    # Leer la matriz desde el archivo
    grid = read_grid_from_file(file_path)

    # Palabra a buscar
    word = "XMAS"

    # Contar las ocurrencias de la palabra en la matriz
    result = count_word_occurrences(grid, word)

    # Mostrar el resultado
    print(f"La palabra '{word}' aparece {result} veces.")
