#!/usr/bin/env python3
"""This module contains func update_topics
"""


def update_topics(mongo_collection, name, topics):
    """This function changes all topics of a school
    args: mongo_collection - pymongo collection obj
    name: school name to update
    topics: list of strings
    """
    # Define the filter to identify the doc to update
    criteria_tofilter = {"name": name}

    # update operations to set new topics
    update_operation = {"$set": {"topics": topics}}

    # update the document that matches the filter
    mongo_collection.update_one(criteria_tofilter, update_operation)
