student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

courses = {
    "CS101": "Intro to Programming",
    "CS102": "Data Structures"
}

student["courses_enrolled"] = courses

if not "CS103" in student["courses_enrolled"]:
    student["courses_enrolled"]["CS103"] = "Algorithms"

for code, title in student["courses_enrolled"].items():
    print(f"{code}: {title}")

new_list = {}
for code, title in student["courses_enrolled"].items():
    if "Data" in title:
        new_list[code] = title
print(new_list)

def filter_courses(courses, keyword):
    return {code: title for code, title in courses.items() if keyword in title}
print(filter_courses(student["courses_enrolled"], "Data"))

def filter_courses2(courses, keyword):
    return dict(filter(lambda item: keyword in item[1], courses.items()))
print(filter_courses(student["courses_enrolled"], "Data"))

course_names = []
for course in student["courses_enrolled"].values():
    course_names.append(course)
print(course_names)

new_course_list = []
for course in student["courses_enrolled"].values():
    if "o" in course:
        new_course_list.append(course)
print(new_course_list)

print(list(student["courses_enrolled"].keys()))

new_dict = {}
for code, title in student["courses_enrolled"].items():
    new_dict[code] = len(title)
print(new_dict)

new_dict = {code: len(title) for code, title in student["courses_enrolled"].items()}
print(new_dict)

new_dict = {}
for code, title in student["courses_enrolled"].items():
    if len(title) in new_dict:
        new_dict[len(title)].append(title)
    else:
        new_dict[len(title)] = [title]

def add_new_course(course_name, dict):
    length = len(course_name)
    if length in dict:
        dict[length].append(course_name)
    else:
        dict[length] = [course_name]
    return dict

print(add_new_course("Statistics", new_dict))