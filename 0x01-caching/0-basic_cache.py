#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    This is a caching system that has no limit.
    """

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache_data dictionary.
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in cache_data linked to key.
        If key is None or doesn't exist in cache_data, returns None.
        """
        return self.cache_data.get(key, None)
