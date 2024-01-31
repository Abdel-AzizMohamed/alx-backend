#!/usr/bin/env python3
"""Define LIFOCache class"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Define LIFOCache class"""

    def __init__(self):
        """Init a new lifo object"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign the given item to a given key"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Get the given item From the given key"""
        return self.cache_data.get(key, None)
