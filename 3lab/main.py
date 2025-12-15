elements = [1, 2, 3]
steps = []        
results = []      

def combinations(index, current):
    steps.append(f"index={index}, current={current}")

    if index == len(elements):
        results.append(current.copy())
        return

    combinations(index + 1, current)

    current.append(elements[index])
    combinations(index + 1, current)
    current.pop()

combinations(0, [])

print("Шаги выполнения:")
for s in steps:
    print(s)

print("\nИтоговые комбинации:")
for r in results:
    print(r)