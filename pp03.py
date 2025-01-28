# Question: Write a Python program to:
# Create a nested dictionary where keys are department names and values are dictionaries of employees and their salaries.
# Calculate the average salary for each department and store it in a new dictionary.
# Print the department with the highest average salary.

departments = {
    "Finance": {
        "John": 50000,
        "Mary": 65000,
        "Sohpia": 80000
    },
    "Shipping": {
        "Sam": 40000,
        "Tom": 75000,
        "David": 90000
    },
    "IT": {
        "Charlie": 100000,
        "Terry": 95000,
        "Simon": 20000
    },
}

average_salaries = {}

for department, employees in departments.items():
    total_salary = 0
    employee_count = len(employees)
    
    for salary in employees.values():
        total_salary += salary

    average_salaries[department] = total_salary / employee_count

highest_avg_department = max(average_salaries, key=average_salaries.get)

print(f"Average Salaries by Department: {average_salaries}")
print(f"Department with Highest Average Salary: {highest_avg_department}")