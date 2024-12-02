#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color="black", price="unknown", cobble="false"):
        self._brand = brand
        self._size = size
        self._color = color
        self._price = price
        self._cobble = cobble
        self._condition = "New"  

    def cobble(self):
        self._cobble = "true"
        self._condition = "New"  
        print("Your shoe is as good as new!")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value