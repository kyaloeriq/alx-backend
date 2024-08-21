#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching
    Implements a LIFO caching system.
    """

    def __init__(self):
        """
        Initialize the class and call the parent constructor.
        """
        super().__init__()
        self.last_key = None  # To keep track of the last added key

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache_data dictionary.
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                # Discard the last added item (LIFO)
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.cache_data[key] = item
            self.last_key = key  # Update the last added key

    def get(self, key):
        """
        Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        return self.cache_data.get(key, None)
