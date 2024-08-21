#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
    Implements an LRU caching system.
    """

    def __init__(self):
        """
        Initialize the class and call the parent constructor.
        """
        super().__init__()
        self.lru_order = []  # To keep track of the order of access

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache_data dictionary.
        If the cache exceeds the maximum limit, the least recently used item will be discarded.
        """
        if key is not None and item is not None:
            # If key already exists, update it and move it to the end of lru_order
            if key in self.cache_data:
                self.lru_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item (first in lru_order)
                lru_key = self.lru_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the new key-value pair to cache and update lru_order
            self.cache_data[key] = item
            self.lru_order.append(key)

    def get(self, key):
        """
        Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end of lru_order (most recently used)
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None
