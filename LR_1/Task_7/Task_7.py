import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()

with open('input7') as f:
    n = int(f.readline())
    massive1 = [float(a) for a in f.readline().split()]
    massive = []
    cnt = 0
    for i in massive1:
        cnt += 1
        massive.append([i, cnt])
massive = sorted(massive)

with open('output7', 'w') as f:
    f.write(str(massive[0][1]))
    f.write(' ')
    f.write(str(massive[n // 2][1]))
    f.write(' ')
    f.write(str(massive[-1][1]))

print(round(tracemalloc.get_traced_memory()[1]/(2**20), 5))
print(time.perf_counter() - t_start)
