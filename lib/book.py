#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count, brand="Unknown", size="Unknown"):
        self.title = title
        self._page_count = page_count
        self._brand=brand
        self._size=size

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

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
        self._size = value
        
        