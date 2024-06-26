#!/usr/bin/env python3
""" creat e class BasicCache that inherits from baseCashing
uses self.cache_data dictionary
use def put(self, key, item): prototype
to aasign item values for a key. if item is "none" return nothing
use def get(self, key): prototype to return values linked to key
if key is "None" or non-existend return None
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """_summary_
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
                key (_type_): _description_
                item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)