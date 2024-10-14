import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()
def insertion_sort(n, data):
    indexes = [1]
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
                i, j = j, i
        indexes.append(i+1)
    return data, indexes


with open('input2', 'r') as file:
    n = int(file.readline())
    massive = [int(a) for a in file.readline().split()]
file.close()

result_data, result_indexes = insertion_sort(n, massive)

if 1 <= n <= 10**3:
    with open('output2', 'w') as file:
        file.write(' '.join(map(str, result_indexes)))
        file.write('\n')
        file.write(' '.join(map(str, result_data)))
    file.close()
else:
    print('Введенные данные не соответствуют условию')

print(round(tracemalloc.get_traced_memory()[1]/(2**20), 5))
print(time.perf_counter() - t_start)

