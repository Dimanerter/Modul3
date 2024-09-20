import time 

start_time = time.perf_counter()

for _ in range(1_000_000):
    pass
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")