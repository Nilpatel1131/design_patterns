class Course_At_My_Institute:
    """ My Institute portal for courses """

    def __init__(self, courses_factory=None):
        """course factory is our abstract factory"""
        self.course_factory = courses_factory

    def show_courses_list(self):
        """shows the list of available courses"""
        print("Available Courses:")
        for course_class in self.course_factory:
            course = course_class()
            print(f'- {course}')

    def show_course_details(self, course_name):
        """shows details of the selected course"""
        for course_class in self.course_factory:
            course = course_class()
            if course_name.lower() == str(course).lower():
                print(f'We have a course named {course}')
                print(f'its price is {course.fee()}')
                break
        else:
            print("Invalid course name. Please select a course from the list.")


class Python:
    """Class for Python"""

    def fee(self):
        return 11000

    def __str__(self):
        return "Python"


class Java:
    """Class for Java"""

    def fee(self):
        return 8000

    def __str__(self):
        return "Java"


class React:
    """Class for React"""

    def fee(self):
        return 15000

    def __str__(self):
        return "React"


def specific_courses():
    """A specific class for choosing the course"""
    return [Python, Java, React]


if __name__ == "__main__":
    course_classes = specific_courses()
    course_portal = Course_At_My_Institute(course_classes)

    course_portal.show_courses_list()

    while True:
        selected_course = input("Enter the name of the course you are interested in: ")
        course_portal.show_course_details(selected_course)
        choice = input("Do you want to inquire about another course? (yes/no): ")
        if choice.lower() != 'yes':
            break
