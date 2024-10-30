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
            # Updating the existing key by removing and readding it
            self.cache_data.pop(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return

        # Moving the accessed item to the end to mark it as recently used
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
