#!/usr/bin/env python3
"""This module contains class cache
"""


import redis
from typing import Union
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
