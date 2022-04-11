import time 
import random

def clamp(n, smallest, largest): return max(smallest, min(n, largest))
class Heater: 
    def __init__(self, name: str, min_temp: float = 0): 
        self.name = name
        self.temp = 1 # Temperature measured in celsius
        self.hum = 0
        #self.wetness = None # Wetness based water-height in milimeters)
        self.state = False
        self.min_temp = min_temp
    
    def __str__(self): 
        print(f"temperature: {self.temp}\nwetness: {self.wetness}")
    
    def get_temp(self): 
        return self.temp

    def set_temp(self, temperature): 
        self.temp = temperature

    def get_hum(self):
        return self.hum

    def set_hum(self, humidity):
        self.hum = clamp(humidity, 0, 100)

    def run(self):
        self.state = self.temp < self.min_temp
        if self.state and random.randint(0, 1) != 0: 
            self.temp += 1
        else: 
            self.temp += random.randint(-1, 1)
        
        self.set_hum(self.hum + random.randint(-1, 1))


if __name__ == '__main__': 

    h = Heater()
    while True: 
        temperature = float(random.randint(0, 75))
        print(temperature)
        h.set_temp(temperature)
        time.sleep(1)
