# Task2. Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message.

class Human:
    species = "Homosapiens"

    def __init__(self, name: str):
        """Initialize a new Human instance with a name."""
        self.name = name

    def welcome(self) -> None:
        """Display a welcome message to the person."""
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls) -> str:
        """Return information about the species."""
        return f"This is a species of '{cls.species}'."

    @staticmethod
    def random_message() -> str:
        """Return a random arbitrary message."""
        return "Have a great day!"


person = Human("Alice")
person.welcome()
print(Human.get_species())
print(Human.random_message())
