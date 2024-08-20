#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    Implements a FIFO caching system.
    """

    def __init__(self):
        """
        Initialize the class and call the parent constructor.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache_data dictionary.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print(f"DISCARD: {first_key}")
                self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        return self.cache_data.get(key, None)
