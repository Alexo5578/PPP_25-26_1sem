results = []
steps_log = []

def permute(arr, start=0):
    if start == len(arr) - 1:
        results.append(arr.copy())
        steps_log.append(f"Нашли перестановку: {arr.copy()}")
    else:
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            steps_log.append(f"Меняем {arr[start]} и {arr[i]}: {arr}")
            permute(arr, start + 1)
            arr[start], arr[i] = arr[i], arr[start]
            steps_log.append(f"Возвращаем обратно: {arr}")

comb_results = []
comb_steps = []

def combine(arr, k, start=0, current=[]):
    if len(current) == k:
        comb_results.append(current.copy())
        comb_steps.append(f"Комбинация: {current.copy()}")
        return
    for i in range(start, len(arr)):
        current.append(arr[i])
        comb_steps.append(f"Добавили {arr[i]}: {current}")
        combine(arr, k, i + 1, current)
        current.pop()
        comb_steps.append(f"Убрали {arr[i]}: {current}")

elements = [1, 2, 3]
print("=== Перестановки ===")
permute(elements)
print("Все перестановки:", results)
print("Количество:", len(results))
print("\nПоследние 3 шага:")
for step in steps_log[-3:]:
    print(step)

print("\n=== Комбинации по 2 ===")
combine(elements, 2)
print("Все комбинации:", comb_results)
print("Количество:", len(comb_results))
print("\nПоследние 3 шага:")
for step in comb_steps[-3:]:
    print(step)