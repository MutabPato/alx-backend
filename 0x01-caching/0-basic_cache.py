#!/usr/bin/python3
"""Caching"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching and is a caching system
    - implements put and get methods
    """
    def __init__(self):
        """Initialize
        """
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if key is None or self.cache_data.get(key) is None:
            return None

        return self.cache_data.get(key)
