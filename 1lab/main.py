import random

N, M = 5, 6
field = [[random.randint(0, 1) for _ in range(M)] for _ in range(N)]

print("Поле:")
for row in field:
    print(row)

def find_island(x, y):
    if x < 0 or x >= N or y < 0 or y >= M or field[x][y] == 0:
        return 0
    
    field[x][y] = 0
    size = 1
    
    size += find_island(x+1, y)
    size += find_island(x-1, y) 
    size += find_island(x, y+1)
    size += find_island(x, y-1)
    
    return size

island_sizes = []
for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            island_sizes.append(find_island(i, j))

rows_with_many = 0
for row in field:
    if sum(row) > 3:
        rows_with_many += 1

cols_with_many = 0
for j in range(M):
    col_sum = sum(field[i][j] for i in range(N))
    if col_sum > 3:
        cols_with_many += 1

print(f"\nРазмеры островов: {island_sizes}")
print(f"Строк с >3 единиц: {rows_with_many}")
print(f"Столбцов с >3 единиц: {cols_with_many}") 