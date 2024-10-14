import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()

with open('input5') as f:
    n = int(f.readline())
    massive = [int(a) for a in f.readline().split()]


def selectionsort(data):
    for i in range(n - 1):
        minim = i
        for j in range(i+1, n):
            if data[minim] > data[j]:
                minim = j
        data[minim], data[i] = data[i], data[minim]
    return data


with open('output5', 'w') as f:
    for element in selectionsort(massive):
        f.write(str(element))
        f.write(' ')

print(round(tracemalloc.get_traced_memory()[1]/(2**20), 5))
print(time.perf_counter() - t_start)
