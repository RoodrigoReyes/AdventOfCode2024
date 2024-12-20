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
    count = 0

    # Iterar sobre cada celda de la matriz
    for r in range(1, rows):
        for c in range(1, cols):
            if grid[r][c] == "A" and (
                r + 1 < rows
                and r - 1 >= 0  # Verificar límites en filas
                and c + 1 < cols
                and c - 1 >= 0  # Verificar límites en columnas
            ):
                r_up = r + 1
                r_down = r - 1
                c_up = c + 1
                c_down = c - 1

                if grid[r_up][c_up] == "M" and grid[r_down][c_down] == "S":
                    if grid[r_down][c_up] == "M" and grid[r_up][c_down] == "S":
                        count += 1
                    elif grid[r_up][c_down] == "M" and grid[r_down][c_up] == "S":
                        count += 1

                elif grid[r_down][c_down] == "M" and grid[r_up][c_up] == "S":
                    if grid[r_down][c_up] == "M" and grid[r_up][c_down] == "S":
                        count += 1
                    elif grid[r_up][c_down] == "M" and grid[r_down][c_up] == "S":
                        count += 1
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
    word = "MAS"

    # Contar las ocurrencias de la palabra en la matriz
    result = count_word_occurrences(grid, word)

    # Mostrar el resultado
    print(f"La palabra '{word}' aparece {result} veces.")
