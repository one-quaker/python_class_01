import random
import time


while True:
    time.sleep(0.5)
    val = random.randint(0, 10)
    print(val)

    if val == 10:
        print('Value == 10')
        break

    if val == 5:
        print('while continue')
        continue

    print('next iteration')
