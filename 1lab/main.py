

if __name__ == "__main__":
    def shuffle_array(arr):
    shuffled = arr.copy()
    for i in range(len(shuffled)-1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled

N = 10
original = list(range(1, N+1))

positions_count = {num: [0]*N for num in original}
num_shuffles = 1000

for _ in range(num_shuffles):
    shuffled = shuffle_array(original)
    for pos, num in enumerate(shuffled):
        positions_count[num][pos] += 1

print("Частота появления чисел на позициях:")
for num in sorted(positions_count.keys()):
    frequencies = [count/num_shuffles for count in positions_count[num]]
    print(f"Число {num}: {[f'{f:.2f}' for f in frequencies]}")