from Heater import Heater
from WetnessDetection import WetnessDetector
import time
import json


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

def to_txt(heaters, delta):
    heaters_list = []
    with open("src/frontend/data.txt", "w") as f:
        #f.write(str(delta) + separator)
        for i in heaters:
            heaters_list.append(i.__dict__)
        json_heat = json.dumps(heaters_list)
        f.write(json_heat)


def main():



    heaters = [Heater("Heater " + str(x+1) + ": " + _heater_names[x]) for x in range(8)]
    delta = 0

    #while True:
    for _ in range(10000):
        delta += 1
        [x.run() for x in heaters]

        to_txt(heaters, delta)
        time.sleep(1)



if __name__ == '__main__':
    main()
    