import random
import time
import math

import GUI

x = 300
y = 300

speed = 1  


def coordinatesDeviation(coeff):
    return math.sqrt(speed ** 2 / (1 + coeff ** 2))


k = round(random.uniform(-100, 100), 2)

pm = random.randint(0, 1)


while True:
    x1 = coordinatesDeviation(k)
    y1 = k * x1

    if x >= 600 or x <= 0:
        if pm == 0:
            pm = 1
        else:
            pm = 0

    if y >= 600 or y <= 0:
        k = -k

    if pm == 1:
        x = x + x1
    else:
        x = x - x1

    if k < 0:
        y = y - y1
    else:
        y = y + y1

    print(k, pm)

    GUI.printGUI([x, y])
    time.sleep(0.01)
