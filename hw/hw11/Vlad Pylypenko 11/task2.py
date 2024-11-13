# 2. Write a program that analyzes the entered number and, depending on the number, gives
# the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
# into account cases of entering numbers from 8 and more, as well as cases of entering nonnumerical data.
import logging
import time
from datetime import datetime, timedelta

logging.basicConfig(
    format="%(asctime)s  %(name)s - %(levelname)s  - %(message)s",
    level=logging.INFO
)


def check_weekday():
    while True:
        try:
            weekday = int(input("Enter the number of the weekday (1-7): "))
            if weekday < 1 or weekday > 7:
                raise ValueError("Your number must be from 1 to 7.")
        except ValueError as err:
            logging.error(f"ValueError: {err}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}.")
        else:
            days = {
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
            }
            logging.info(f"The day with number {weekday} is {days[weekday]}.")
            # Or
            # base_date = datetime(1900, 1, 1)
            # day_date = base_date + timedelta(days=weekday - 1)
            # logging.info(f"The day with number {weekday} is {day_date.strftime("%A")}.")
            break
        finally:
            logging.info("Operation completed.")
            time.sleep(0.1)


if __name__ == "__main__":
    check_weekday()
