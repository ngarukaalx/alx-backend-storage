#!/usr/bin/env python3
"""This module contains func
list_all() list all doc in a collection
"""


def list_all(mongo_collection):
    """list all docs in a collection
    args: pymongo collection object
    Returns a empty list if no doc else list
    """
    doc_colections = mongo_collection.find()
    doc_list = list(doc_colections)
    return doc_list
