
def main():
    user_time = input("What time is it? ")
    decimal_time = convert(user_time)
    meal_result = meal_checker(user_time, decimal_time)

    if meal_result == None:
        pass
    else:
        print(meal_result)


def convert(time):
    time = time.strip().lower().translate(str.maketrans("", "", ".apm"))
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(round((float(minutes) / 60) * 100,0))

    decimal_time = str(hours) + "." + str(minutes)
    decimal_time = float(decimal_time)

    return decimal_time

def meal_checker(user_time, decimal_time):
    if user_time.endswith(("am","a.m")):
        if 7 <= decimal_time <= 8:
            return "breakfast time"
        else:
            pass

    elif user_time.endswith(("pm","p.m")):
        if 12 <= decimal_time <= 13 or 0 <= decimal_time <= 1:
            return "lunch time"
        elif 18 <= decimal_time <= 19 or 6 <= decimal_time <= 7:
            return "dinner time"
        else:
            pass

    else:
        if 7 <= decimal_time <= 8:
            return "breakfast time"
        elif 12 <= decimal_time <= 13:
            return "lunch time"
        elif 18 <= decimal_time <= 19:
            return "dinner time"
        else:
            pass

if __name__ == "__main__":
    main()

