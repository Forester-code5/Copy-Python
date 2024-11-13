# Task3. Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)

class Employee:
    """A class representing an employee."""

    employee_count = 0

    def __init__(self, name: str, salary: float):
        """Initialize an employee with a name and salary."""
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self):
        """Display information about the employee."""
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def print_employee_count(cls):
        """Print the total number of employees."""
        print(f"Total number of employees: {cls.employee_count}")

    def __str__(self) -> str:
        """Return a string representation of the Employee."""
        return f"Employee's name: {self.name}, salary: ${self.salary:.2f}"


emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

emp1.display_info()
emp2.display_info()

print(emp1)
print(emp2)

Employee.print_employee_count()

print("Base class:", Employee.__base__)  # Base class: <class 'object'>
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)  # Class name: Employee
print("Module name:", Employee.__module__)  # Module name: __main__
print("Documentation:", Employee.__doc__)  # Documentation: A class representing an employee.
