# Abstract course
class Course:

    def __init__(self):
        self.fee = None
        self.batches = None
        self.set_fee()
        self.set_available_batches()

    def set_fee(self):
        raise NotImplementedError("Subclasses must implement set_fee method.")

    def set_available_batches(self):
        raise NotImplementedError("Subclasses must implement set_available_batches method.")

    def __repr__(self):
        return 'Fee : {} | Batches Available : {}'.format(self.fee, self.batches)


# Concrete course
class DSA(Course):

    """Class for Data Structures and Algorithms"""

    def set_fee(self):
        self.fee = 8000

    def set_available_batches(self):
        self.batches = 5

    def __str__(self):
        return "DSA"


# Concrete course
class SDE(Course):

    """Class for Software Development Engineer"""

    def set_fee(self):
        self.fee = 10000

    def set_available_batches(self):
        self.batches = 4

    def __str__(self):
        return "SDE"


# Concrete course
class STL(Course):

    """Class for Standard Template Library"""

    def set_fee(self):
        self.fee = 5000

    def set_available_batches(self):
        self.batches = 7

    def __str__(self):
        return "STL"


# Complex Course
class ComplexCourse:

    def __repr__(self):
        return 'Fee : {} | available_batches: {}'.format(self.fee, self.batches)


# Complex course
class ComplexCourseImpl(ComplexCourse):

    def set_fee(self):
        self.fee = 7000

    def set_available_batches(self):
        self.batches = 6


# Construct course
def construct_course(cls):
    course = cls()
    course.set_fee()
    course.set_available_batches()
    return course  # return the course object


# Main method
if __name__ == "__main__":

    dsa = DSA()  # object for DSA course
    sde = SDE()  # object for SDE course
    stl = STL()  # object for STL course

    complex_course = construct_course(ComplexCourseImpl)
    print(complex_course)
