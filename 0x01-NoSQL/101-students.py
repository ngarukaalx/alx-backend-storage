#!/usr/bin/env python3
"""This module contains func to_students
"""
import pymongo


def top_students(mongo_collection):
    """returns all students sorted by average score
    arg: mongo_collection
    Returns all students sorted by average score
    """

    # loop through each doc
    for doc in mongo_collection.find():
        all_scores = [score["score"] for score in doc["topics"]]
        # compute average score
        average_Score = sum(all_scores) / len(all_scores)
        # update each doc by adding averagescore
        mongo_collection.update_one(
                {'_id': doc['_id']},
                {"$set": {"averageScore": average_Score}}
                )

    return mongo_collection.find().sort("averageScore", pymongo.DESCENDING)
