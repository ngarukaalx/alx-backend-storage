#!/usr/bin/env python3
"""This module contains func insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection based on Kwargs
    args: mongo_collection - pymongo collection object
    args: kwargs -
    returns new _id
    """

    insert_doc = mongo_collection.insert_one(kwargs)
    return insert_doc.inserted_id
