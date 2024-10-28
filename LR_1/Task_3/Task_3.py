import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()

with open('input3') as f:
    n = int(f.readline())
    massive = [int(a) for a in f.readline().split()]


def insertionsort(data):
    for i in range(1, n+1):
        key = data[i]
        j = i - 1
        while j >= 0 and key > data[j]:
            data[j+1], data[j] = data[j], data[j+1]
            j -= 1
        data[j+1] = key
    return data


with open('output3', 'w') as f:
    for element in insertionsort(massive):
        f.write(str(element))
        f.write(' ')

print(round(tracemalloc.get_traced_memory()[1]/(2**20), 5))
print(time.perf_counter() - t_start)
