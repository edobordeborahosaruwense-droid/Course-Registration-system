courses = []

def register_course():
    course = input("Enter course name: ")
    courses.append(course)
    print("Course registered")

def view_courses():
    if not courses:
        print("No courses registered")
    else:
        for course in courses:
            print(course)

def main():
    while True:
        print("1. Register Course")
        print("2. View Courses")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register_course()
        elif choice == "2":
            view_courses()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
