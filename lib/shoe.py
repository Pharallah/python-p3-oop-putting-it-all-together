#!/usr/bin/env python3
import ipdb

class Shoe:
    def __init__(self, brand, size, condition=None):
        self.brand = brand
        self.size = size
        self.condition = condition

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"



        

stan_smith = Shoe("Adidas", 9)

