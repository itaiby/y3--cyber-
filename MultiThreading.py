import random
import threading
import math

HITS = 0
TRYS = 0

def RandomPointGenerator():
    return (random.random(),random.random())

def IsRandomPointInsideCircle():
    global HITS, TRYS
    point = RandomPointGenerator()
    TRYS += 1
    if (point[0] ** 2 + point[1] ** 2) < 1:
        HITS += 1

numberOfBatches = int(input("Enter number of batches: "))
for i in range(numberOfBatches):
    for _ in range(10000):
        thread = threading.Thread(target=IsRandomPointInsideCircle)
        thread.start()
    astimatedPi = (HITS / TRYS)*4
    print(f"#{i+1} -", f"{astimatedPi:.10f}", f"/// {math.pi}", f"({abs(math.pi - astimatedPi)})")