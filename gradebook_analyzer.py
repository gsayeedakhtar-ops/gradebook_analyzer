scores = [85, 42, 77, 90, 66, 38, 59, 82, 48]
students = ["Aayan", "Zara", "Ilhan", "Imad", "Saud", "Aditya", "Dhruv", "Aman", "Ishan"] 
def gradebook_analyzer(students,scores):
    if not scores:
        return {
            "Total": 0,
            "Average": 0,
            "Highest": None,
            "Lowest": None,
            "Above_average": [],
            "Topper": None,
            "Failures": []
        }

    total = sum(scores)
    avg = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    student_scores = list(zip(students,scores))
    topper = max(student_scores, key=lambda x: x[1])
    above_avg = [(name,score) for name, score in student_scores if score > avg]
    below_avg = [(name,score) for name, score in student_scores if score < avg]
    failures = [(name,score) for name, score in student_scores if score < 40]

    return {
        "Total": total,
        "Average": avg,
        "Highest": topper[1],
        "Lowest": min(scores),
        "Above Average": above_avg,
        "Below Average": below_avg,
        "Failures": failures,
        "Topper": topper[0]
    }
report = gradebook_analyzer(students,scores)
from pprint import pprint
pprint(report)
    
