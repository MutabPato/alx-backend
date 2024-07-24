#!/usr/bin/python3
""" LRUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and is a caching system """
    def __init__(self):
        """" Initialize the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
