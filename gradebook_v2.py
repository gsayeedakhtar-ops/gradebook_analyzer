def gradebook_v2(**scores):
    total_students = len(scores)
    avg = sum(scores.values()) / total_students
    highest = max(scores.values())
    lowest = min(scores.values())

    result = {}
    for student, mark in scores.items():
        if mark >= 90:
            grade = "A"
        elif mark >= 75:
            grade = "B"
        elif mark >= 50:
            grade = "C"
        else:
          grade = "Fail"
        result[student] = {"score": mark, "grade": grade}
    topper = max(scores.items(), key=lambda x:x[1])
    print("Total students:", total_students)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Topper:", topper[0], "with score", topper[1])
    print("\nDetailed Grades:")
    for student, info in result.items():
        print(f"{student}: {info}")
gradebook_v2(Sayeed=91, Faizan=76, Irshad=84, Sid=54, Nik=32)
          
    
