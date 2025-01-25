employees = [
    {"name": "Alice", "age": 30, "department": "HR"},
    {"name": "Bob", "age": 25, "department": "Engineering"},
    {"name": "Charlie", "age": 35, "department": "Sales"},
    {"name": "David", "age": 28, "department": "Engineering"},
]

def main():
    print(return_department_staff(employees))

def return_department_staff(employee_list):
    department_dict = {}
    for employee in employee_list:
        department_dict.setdefault(employee["department"], []).append(employee["name"])
    return department_dict

if __name__ == "__main__":
    main()