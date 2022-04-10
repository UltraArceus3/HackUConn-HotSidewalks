from Heater import Heater
from WetnessDetection import WetnessDetector

heaters = []

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
    "Putnam"
]


def main():
    heaters = [Heater("Heater " + str(x) + ": " + _heater_names[x]) for x in range(10)]
    print(heaters)
    print(heaters[2].__dict__)

if __name__ == '__main__': 
    main()

    input()

