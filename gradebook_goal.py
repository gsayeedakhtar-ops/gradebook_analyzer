def goal_based_gradebook(passing_score=40, **scores):
    result = {}
    for student, mark in scores.items():
        if mark >= passing_score:
            status = "Pass"
        else:
            needed = passing_score - mark
            status = f"Fail (needs +{needed} to pass)"
        result[student] = {"score": mark, "status": status}

    return result

# Example run
report = goal_based_gradebook(Sayeed=91, Faizan=30, Irshad=55, Sid=22)
from pprint import pprint
pprint(report)
