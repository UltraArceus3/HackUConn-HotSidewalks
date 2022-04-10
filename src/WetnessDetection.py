'''
Source: Road Surface Wetness Variations.
    Based on the sensor developed by Haavasoja et al. 
    The RCM411 road condition monitor sensor could 
    measure water layer thickness from 0 to 3 milimeter. 
'''

import time

class WetnessDetector:
    def __init__(self):
        self.height = 0 # Height of water measured in milimeters
    
    def __str__(self): 
        print(self.get_layer)

    def get_layer(self): 
        return self.height

    def set_layer(self, height): # Updates the height value. 
        if type(height) is not float:
            raise TypeError("Invalid value type, can only be a floating value or an integer value\nWetness detector has stopped running.")
        if height < 0: 
            raise Exception("Invalid height, can not be a negative value\nWetness detector has stopped running.") 
        self.height = height 

    def run(self): # Continuously updates height value.
        while True:
            height = input()
            self.set_layer(height)
            time.sleep(30)


if __name__ == '__main__': 
    import random 
    
    w = WetnessDetector()
    while True: 
        height = float(random.randint(0, 10))
        print(height)
        w.set_layer(height)
        time.sleep(1)


        
