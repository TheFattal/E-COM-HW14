def day_of_week(number_str: str) -> str:
    try:
        number_int = int(number_str)
    except ValueError:
        raise ValueError("Invalid input: not a number")
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    if number_int < 1 or number_int > 7:
        raise ValueError("Invalid day number")
    return days[number_int]


def make_day_in_letters():
    while True:
        day_number = input("Insert day number between 1 - 7 (-99 to exit): ")
        try:
            if day_number == "-99":
                break
            feedback: str = day_of_week(day_number)
            print(feedback)

        except ValueError as ex:
            print(ex)
