

import random

def generate_game_field(rows, cols):
    """Генерация игрового поля NxM из 0 и 1"""
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def count_islands_size(field):
    """Подсчет размеров островов из 1 (поиск в глубину)"""
    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or field[i][j] == 0:
            return 0
        
        field[i][j] = 0 
        size = 1
        
        size += dfs(i + 1, j)
        size += dfs(i - 1, j)
        size += dfs(i, j + 1)
        size += dfs(i, j - 1)
        
        return size
    
    rows, cols = len(field), len(field[0])
    island_sizes = []
    
    field_copy = [row[:] for row in field]
    field = field_copy
    
    for i in range(rows):
        for j in range(cols):
            if field[i][j] == 1:
                island_size = dfs(i, j)
                island_sizes.append(island_size)
    
    return island_sizes

def count_rows_cols_with_more_than_three_ones(field):
    """Подсчет строк и столбцов с более чем 3 единицами"""
    rows, cols = len(field), len(field[0])
    
    rows_count = 0
    for row in field:
        if sum(row) > 3:
            rows_count += 1
    
    cols_count = 0
    for j in range(cols):
        col_sum = sum(field[i][j] for i in range(rows))
        if col_sum > 3:
            cols_count += 1
    
    return rows_count, cols_count

def print_field(field):
    """Красивый вывод игрового поля"""
    for row in field:
        print(' '.join(str(cell) for cell in row))

if __name__ == "__main__":
    N, M = 5, 5
    field = generate_game_field(N, M)
    
    print("Игровое поле:")
    print_field(field)
    print()
    
    island_sizes = count_islands_size([row[:] for row in field])  # Работаем с копией
    print(f"Размеры островов: {island_sizes}")
    print(f"Количество островов: {len(island_sizes)}")
    
    rows_count, cols_count = count_rows_cols_with_more_than_three_ones(field)
    print(f"Строк с более чем 3 единицами: {rows_count}")
    print(f"Столбцов с более чем 3 единицами: {cols_count}") = shuffle_array(original)
    for pos, num in enumerate(shuffled):
        positions_count[num][pos] += 1

print("Частота появления чисел на позициях:")
for num in sorted(positions_count.keys()):
    frequencies = [count/num_shuffles for count in positions_count[num]]
    print(f"Число {num}: {[f'{f:.2f}' for f in frequencies]}")