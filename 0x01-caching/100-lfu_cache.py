#!/usr/bin/python3
""" LFUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and is a caching system """
    def __init__(self):
        """" Initialize the class """
        super().__init__()
        self.frequency = {}
        self.usage_order = {}
        self.current_time = 0

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order[key] = self.current_time
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = min(self.frequency, key=lambda k: (
                    self.frequency[k], self.usage_order[k]))
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                del self.usage_order[lfu_key]
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = self.current_time

        self.current_time += 1

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order[key] = self.current_time
            self.current_time += 1
            return self.cache_data.get(key)
        return None
