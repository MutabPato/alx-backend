#!/usr/bin/python3
"""Caching
   Basic dictionary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching and is a caching system
    - implements put and get methods
    """

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """

        return self.cache_data.get(key, None)
