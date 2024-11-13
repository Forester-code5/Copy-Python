# I. Ball-super-ball
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"

# https://www.codewars.com/kata/53f0f358b9cb376eca001079/train/python

class Ball:
    """A class representing a ball with a specific type."""

    def __init__(self, ball_type: str = "regular"):
        """Initialize the ball with a given type, defaulting to 'regular'."""
        self.ball_type = ball_type


ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)  # Output: regular
print(ball2.ball_type)  # Output: super

# II. Color-ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"

# https://www.codewars.com/kata/53f1015fa9fe02cbda00111a/train/python

import random


class Ghost:
    """A class representing a ghost with a random color."""

    def __init__(self):
        """Initialize the ghost with a random color."""
        self.color = random.choice(["white", "yellow", "purple", "red"])


ghost = Ghost()
print(ghost.color)  # Output: "white", "yellow", "purple", or "red"


# III. Basic-subclasses-Adam-and-Eve
# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing
# Adam and Eve). The first object in the array should be an instance of the class Man. The second should be an
# instance of the class Woman. Both objects have to be subclasses of Human. Your job is to implement the Human,
# Man and Woman classes.)

# https://www.codewars.com/kata/547274e24481cfc469000416/train/python

class Human:
    """A base class representing a human being."""

    def __init__(self, name: str):
        self.name = name


class Man(Human):
    """A class representing a male human."""

    def __init__(self, name: str = "Adam"):
        super().__init__(name)


class Woman(Human):
    """A class representing a female human."""

    def __init__(self, name: str = "Eve"):
        super().__init__(name)


def God():
    """Create and return an array of Adam and Eve."""
    return [Man(), Woman()]


humans = God()
print(humans[0].name)
print(humans[1].name)


# IV. Classy-classes
# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number,
# complete the get Info property and getInfo method/Info getter which should return johns age is 34
# Reference: https://docs.python.org/3/tutorial/classes.html

# https://www.codewars.com/kata/55a144eff5124e546400005a/train/python

class Person:
    """A class representing a person with a name and age."""

    def __init__(self, name: str, age: int):
        """Initialize the person with a name and age."""
        self.name = name
        self.age = age

    @property
    def info(self) -> str:
        """Return a string with the person's name and age."""
        return f"{self.name}s age is {self.age}"

    def get_info(self) -> str:
        """Return a string with the person's name and age."""
        return self.info


john = Person("john", 34)
print(john.get_info())

# V. Building Spheres
# Now that we have a Block let's move on to something slightly more complex: a Sphere.
# Arguments for the constructor
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

# https://www.codewars.com/kata/55c1d030da313ed05100005d/train/python

import math


class Sphere:
    """A class representing a sphere with a radius and a mass."""

    def __init__(self, radius: float, mass: float):
        """Initialize the sphere with a radius and a mass."""
        self.radius = radius
        self.mass = mass

    def get_radius(self) -> float:
        """Return the sphere's radius."""
        return self.radius

    def get_mass(self) -> float:
        """Return the sphere's mass."""
        return self.mass

    def get_volume(self) -> float:
        """Return the volume of the sphere, rounded to 5 decimal places."""
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self) -> float:
        """Return the surface area of the sphere, rounded to 5 decimal places."""
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self) -> float:
        """Return the density of the sphere, rounded to 5 decimal places."""
        density = self.mass / self.get_volume()
        return round(density, 5)


sphere = Sphere(3, 10)
print(f"Radius: {sphere.get_radius()}")  # Output: Radius: 3
print(f"Mass: {sphere.get_mass()}")  # Output: Mass: 10
print(f"Volume: {sphere.get_volume()}")  # Output: Volume: 113.09734
print(f"Surface Area: {sphere.get_surface_area()}")  # Output: Surface Area: 113.09734
print(f"Density: {sphere.get_density()}")  # Output: Density: 0.08843


# VI. Dynamic Classes
# Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:
# - Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!
# Tim sighed, he already knew it's gonna be a long day.
# Few hours later, boss came again:
# Much better - he said - but now I want to change that class name to SecondUsefulClass,
# and went off. Although Timmy had no idea why changing name is so important for his boss, he realized,
# that it('s not the end, so he turned to you, his guru, to help him and asked you to prepare some function,
# which could change name of given class.)
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers),
# but starting only with upper case letter. In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases, but let's
# stick with that, that Timmy yet has to learn them.

# https://www.codewars.com/kata/55ddb0ea5a133623b6000043/train/python

class MyClass:
    """A simple class example."""
    pass


def class_name_changer(cls, new_name: str):
    """Rename a given class to a new name if it's valid."""
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name


print("Original class name:", MyClass.__name__)  # Output: MyClass

try:
    class_name_changer(MyClass, "UsefulClass")
    print("Renamed class name:", MyClass.__name__)  # Output: UsefulClass

    class_name_changer(MyClass, "SecondUsefulClass")
    print("Renamed class name:", MyClass.__name__)  # Output: SecondUsefulClass

    class_name_changer(MyClass, "invalidClassName!")  # This will raise an exception
except ValueError as e:
    print(e)  # Output: Class name must start with an uppercase letter and contain only alphanumeric characters.
