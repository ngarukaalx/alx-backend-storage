#!/usr/bin/env python3
"""This module contains func schools_by_topic()
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of school having a specific topic
    args:mongo_collection - pymongo collection obj
    topic: (string) topic search
    Returns: list of school
    """
    result_school = mongo_collection.find({"topics": topic})
    list_result = list(result_school)
    return list_result

