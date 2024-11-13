# 1. Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code
# should call a function that processes the information entered.
import logging
import time

logging.basicConfig(
    format="%(asctime)s  %(name)s - %(levelname)s  - %(message)s",
    level=logging.INFO
)


def check_age():
    """Prompts the user for their age and determines if it's even or odd."""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("Your age must be a positive number.")
        except ValueError as err:
            logging.error(f"ValueError: {err}")
        except Exception as e:
            logging.exception(f"An unexpected error occurred: {e}.")
        else:
            if age % 2:
                logging.info(f"The age {age} is odd.")
            else:
                logging.info(f"The age {age} is even.")
            break
        finally:
            logging.info("Operation completed.")
            time.sleep(0.1)


if __name__ == "__main__":
    check_age()


# Or
def check_age():
    """Prompts the user for their age and determines if it's even or odd."""
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            if age % 2 == 0:
                print(f"The age {age} is even.")
            else:
                print(f"The age {age} is odd.")
            break
        except ValueError as err:
            print(f"Error: {err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    check_age()
