#!/usr/bin/env python3
"""Define BasicCache class"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Define FIFOCache class"""

    def __init__(self):
        """Init a new fifo object"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign the given item to a given key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Get the given item From the given key"""
        return self.cache_data.get(key, None)
