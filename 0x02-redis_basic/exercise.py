#!/usr/bin/env python3
"""This module contains class cache
"""


import redis
from typing import Union, Callable, Any
import uuid
import functools


def count_calls(method: Callable) -> Callable:
    """decorator func"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """wapper func"""
        # implement a system on how many times the method is called
        key_method = method.__qualname__
        # check if the key exists
        if not self._redis.exists(key_method):
            self._redis.set(key_method, 0)
            # increment
        self._redis.incr(key_method)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decoratorn func"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """wapper func"""
        key_inputs = method.__qualname__ + ':inputs'
        # store the method arguments to a list
        inputs = str(args)
        self._redis.rpush(key_inputs, inputs)

        key_outputs = method.__qualname__ + ':outputs'
        result = method(self, *args, **kwargs)
        # store the output to a list
        self._redis.rpush(key_outputs, result)
        return result

    return wrapper


class Cache():
    """class to perform some redis operation"""
    def __init__(self):
        """store an instance of the Redis client as a private variable
        """
        self._redis = redis.Redis(host='127.0.0.1', port=6379)

        # flush the instance
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key and store input data in redis using
        random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    @count_calls
    @call_history
    def get_int(self, key: str) -> int:
        """convert data in bytes to int"""
        return self.get(key, fn=int)

    @count_calls
    @call_history
    def get_str(self, key: str) -> str:
        """converts x to str"""
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    @count_calls
    @call_history
    def get(self, key: str, fn: Callable = None) -> Any:
        """get method"""
        result = self._redis.get(key)

        if result is None:
            return None

        if fn is not None:
            result = fn(result)
        return result

    def replay(self, arg):
        """implements the replay to display history"""

        class_name = arg.__self__.__class__.__name__
        method_name = arg.__name__
        arg_expression = f"{class_name}.{method_name}"

        key_inputs = arg_expression + ':inputs'
        key_outputs = arg_expression + ':outputs'
        outputs = self._redis.lrange(key_outputs, 0, -1)
        inputs = self._redis.lrange(key_inputs, 0, -1)
        print("{} was called {} times:".format(
            arg_expression, self._redis.llen(key_inputs))
            )
        for inp, out in zip(inputs, outputs):
            print(f"{arg_expression}(*{inp.decode('utf-8')}) "
                  f"-> {out.decode('utf-8')}")
