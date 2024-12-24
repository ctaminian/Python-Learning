students = {}

def main():
    add_student("Charlie", {"Math": 85, "Science": 90, "History": 60})
    add_student("Rob", {"Math": 50, "Science": 70, "History": 20})
    add_student("Jenny", {"Math": 50, "Science": 50, "History": 50})
    update_score("Rob", "History", 10)
    boost_scores("Charlie")
    print(filter_passed_students(students))
    print_students(students)

def add_student(name, subjects):
    students[name] = {"subjects": subjects}
    pass_or_fail(name)

def update_score(name, subject, score):
    if name not in students:
        print(f"Student {name} does not exist.")
        return
    if subject not in students[name]["subjects"]:
        print(f"Subject {subject} does not exist for student {name}.")
        return
    students[name]["subjects"][subject] = score
    pass_or_fail(name)

def filter_passed_students(students):
    return {student: students[student] for student in students if students[student]["status"] == "Pass"}

def boost_scores(name):
    if name in students:
        subjects = students[name]["subjects"]
        boosted_scores = dict(map(lambda item: (item[0], item[1] + 10), subjects.items()))
        students[name]["subjects"] = boosted_scores
        pass_or_fail(name)
    else:
        print(f"Student {name} not found.")

def pass_or_fail(name):
    grades = list(students[name]["subjects"].values())
    average = sum(grades) / len(grades)
    students[name]["status"] = "Pass" if average >= 50 else "Fail"

def print_students(students):
    for student, details in students.items():
        print(f"Student: {student}")
        print(f"  Subjects: {details['subjects']}")
        print(f"  Status: {details['status']}")
        print()

if __name__ == "__main__":
    main()