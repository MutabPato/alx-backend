#!/usr/bin/python3
"""Caching
   LRU Caching
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system
    - implements put and get methods
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """

        return self.cache_data.get(key, None)
