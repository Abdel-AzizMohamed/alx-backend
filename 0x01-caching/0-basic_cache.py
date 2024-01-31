#!/usr/bin/env python3
"""Define BasicCache class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Define basic cache class"""

    def put(self, key, item):
        """Assign the given item to a given key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get the given item From the given key"""
        return self.cache_data.get(key, None)
