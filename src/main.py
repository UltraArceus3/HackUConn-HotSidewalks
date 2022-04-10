from Heater import Heater
from WetnessDetection import WetnessDetector
import time


_heater_names = [
    "North",
    "Gampel",
    "South",
    "NorthWest",
    "Whitney",
    "Monteith",
    "Buckley",
    "McHugh",
    "Werth",
    "Putnam",
]

def to_csv(heaters, delta, separator = "|"):
    with open("src/data.txt", "w") as f:
        f.write(str(delta) + separator)
        for i in heaters:
            f.write(str(i.__dict__) + separator)


def main():



    heaters = [Heater("Heater " + str(x) + ": " + _heater_names[x]) for x in range(10)]
    delta = 0

    #while True:
    for _ in range(10000):
        delta += 1
        [x.run() for x in heaters]

        to_csv(heaters, delta)
        time.sleep(1)



if __name__ == '__main__':
    main()
    