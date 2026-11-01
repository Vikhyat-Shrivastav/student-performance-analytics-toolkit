
def add_student(student_id, name, marks):
    if not student_id or not name:
        return None

    if not isinstance(marks, list) or len(marks) == 0:
        return None

    if not all(isinstance(m, (int, float)) and 0 <= m <= 100
               for m in marks):
        return None

    return {
        "name": name,
        "marks": marks
    }


def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)



def get_grade(average):
    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Division"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"


def build_report(student):
    marks = student["marks"]
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)

    return {
        "name": student["name"],
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }


def get_top_students(records):
    return list(filter(
        lambda item: calculate_average(item[1]["marks"]) >= 75,
        records.items()
    ))



def get_student_names(records):
    return list(map(
        lambda item: item[1]["name"],
        records.items()
    ))


def flexible_average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


def class_summary(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)



def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

def scope_demo():
    message = "This is a local variable"
    print(message)



def main():

    students = {}

    students["S101"] = add_student(
        "S101", "Aman", [78, 65, 88]
    )

    students["S102"] = add_student(
        "S102", "Riya", [35, 72, 61]
    )

    students["S103"] = add_student(
        "S103", "Rahul", [90, 85, 95]
    )

    students["S104"] = add_student(
        "S104", "Priya", [45, 50, 55]
    )

    students = {
        sid: student for sid, student in students.items()
        if student is not None
    }

    print("===== STUDENT PERFORMANCE REPORT =====")

    for student_id, student in students.items():
        report = build_report(student)

        print("\nStudent ID:", student_id)
        print("Name:", report["name"])
        print("Marks:", report["marks"])
        print("Total:", report["total"])
        print("Average:", round(report["average"], 2))
        print("Grade:", report["grade"])

    top_students = get_top_students(students)

    print("\nHigh Performers (Average >= 75):")
    print(list(map(lambda item: item[1]["name"], top_students)))


    print("\nAll Student Names:")
    print(get_student_names(students))

    averages = [
        calculate_average(student["marks"])
        for student in students.values()
    ]

    print("\nClass Average:",
          round(flexible_average(*averages), 2))

    print("\nFlexible Average:",
          flexible_average(80, 90, 70))


    print("\nClass Summary:")
    class_summary(
        title="Class Report",
        passing_mark=40,
        total_students=len(students)
    )

    print("\nRecursive Sum:")
    print("Sum from 1 to 5:", recursive_sum(5))
    print("Sum from 1 to 10:", recursive_sum(10))
    print("Sum from 1 to 3:", recursive_sum(3))

    print("\nScope Demonstration:")
    scope_demo()


if __name__ == "__main__":
    main()