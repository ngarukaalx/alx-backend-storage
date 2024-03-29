#!/usr/bin/env python3
"""This module contains func get_page"""

import requests
import redis


r = redis.Redis()
def get_page(url: str) -> str:
    """track how many times a particular URL was accessed"""
    url_key = f"count:{url}"
    r.incr(url_key)

    response = request.get(url)
    htm_content = response.text

    key_cached = f"cache:{url}"
    r.setex(key_cached, 10, htm_content)
    return htm_content
