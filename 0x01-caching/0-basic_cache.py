#!/usr/bin/python3
"""Caching"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
                "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
                "get must be implemented in your cache class")


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or self.cache_data.get(key) is None:
            return None

        return self.cache_data.get(key)