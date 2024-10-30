#!/usr/bin/python3
"""Caching
   LFU Caching
"""


from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system
    and implements an LFU caching system
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.cache_data = {}  # Store items
        self.frequency_data = defaultdict(int)  # Store frequencies of items
        self.freq_items = defaultdict(OrderedDict)  # Store items by frequency
        self.min_freq = 0  # Track the minimum frequency in cache

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Updating the existing item and adjust its frequency
            self.cache_data[key] = item
            self._update_frequency(key)

        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict the frequently used item
                self._evict_lfu()

            # Insert the new item with frequency 1
            self.cache_data[key] = item
            self.frequency_data[key] = 1
            self.freq_items[1][key] = None
            self.min_freq = 1  # Reset minimu frequency to 1 for new item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return

        # Update frequency of accessed item and return it
        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """Helper method to update the frequency of an accessed item"""
        freq = self.frequency_data[key]

        # Remove key from current frequency group
        del self.freq_items[freq][key]
        if not self.freq_items[freq]:
            del self.freq_items[freq]
            # If it was the min frequency and now empty, increase min frequency
            if self.min_freq == freq:
                self.min_freq += 1

        # Increase frequency and add key to the new frequency group
        self.frequency_data[key] += 1
        new_freq = freq + 1
        self.freq_items[new_freq][key] = None

    def _evict_lfu(self):
        """Helper method to evict the least frequently used item"""
        # Find the oldest item in the lowest frequency group
        lfu_key, _ = self.freq_items[self.min_freq].popitem(last=False)

        print(f"DISCARD: {lfu_key}")
        # Remove the LFU item from cache and frequency tracking
        del self.cache_data[lfu_key]
        del self.frequency_data[lfu_key]

        # Clean up the frequency group if empty
        if not self.freq_items[self.min_freq]:
            del self.freq_items[self.min_freq]
