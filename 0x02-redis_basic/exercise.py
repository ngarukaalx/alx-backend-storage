#!/usr/bin/env python3
"""This module contains class cache
"""


import redis
from typing import Union, Callable, Any
import uuid


class Cache():
    """class to perform some redis operation"""
    def __init__(self):
        """store an instance of the Redis client as a private variable
        """
        self._redis = redis.Redis(host='127.0.0.1', port=6379)

        # flush the instance
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key and store input data in redis using
        random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get_int(self, key: str) -> int:
        """convert data in bytes to int"""
        return self.get(key, fn=int)

    def get_str(self, key: str) -> str:
        """converts x to str"""
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get(self, key: str, fn: Callable = None) -> Any:
        """get method"""
        result = self._redis.get(key)

        if result is None:
            return None

        if fn is not None:
            result = fn(result)
        return result
