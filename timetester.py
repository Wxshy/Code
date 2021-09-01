import time
from random import randint

nums = []

for _ in range(1_000_000):
    nums.append(randint(0,1000))

print('Started')

start = time.perf_counter()

nums.sort()

end = time.perf_counter()
print('Done')

print(f'Time Taken: {end-start}'