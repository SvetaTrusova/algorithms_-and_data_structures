import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()

with open('input6') as f:
    n = int(f.readline())
    massive = [int(a) for a in f.readline().split()]

def bubblesort(n, data):
    for i in range(n - 1): #не делаем последнюю проходку, потому что останется последний элемент
        for j in range(n):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data

with open('output6', 'w') as f:
    for element in bubblesort(n, massive):
        f.write(str(element))

        f.write(' ')

print(round(tracemalloc.get_traced_memory()[1]/(2**20), 5))
print(time.perf_counter() - t_start)



