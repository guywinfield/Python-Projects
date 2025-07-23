import re

def main():
    print(convert(input("Hours: ")))

def convert(string):
    if " to " not in string:
        raise ValueError("Invalid time format")

    time = re.search(r"((?:[0-9]+)(?::[0-9]{2})? (?:[a-z]+)) to ((?:[0-9]+?)(?::[0-9]{2})? (?:[a-z]+))", string.strip(), re.IGNORECASE)
    if time is None:
        raise ValueError("Invalid time format")

    timings = time.groups(1)

    for t in timings:
        minutes = re.search(r"(?:[0-9]+):([0-9]+).+", t.strip(), re.IGNORECASE)
        if minutes is None:
            pass
        else:
            minutes = minutes.groups(1)
            minutes = minutes[0]
            if int(minutes) >= 60:
                raise ValueError("Invalid time format")

    formatted_timings = []

    for t in timings:
        t = t.upper().strip()

        if t[-2:] == "AM" and ":" in t:
            time = re.search(r"([0-9]+):([0-9]+)? (?:[a-z]+)", t, re.IGNORECASE)
            if int(time.group(1)) == 12:
                hours = 0
            elif int(time.group(1)) > 24:
                raise ValueError("Invalid time format")
            else:
                hours = int(time.group(1))

            minutes = int(time.group(2))
            formatted_timings.append(f"{hours:02}:{minutes:02}")

        elif t[-2:] == "PM" and ":" in t:
            time = re.search(r"([0-9]+):([0-9]+)? (?:[a-z]+)", t, re.IGNORECASE)
            if int(time.group(1))+12 == 24:
                hours = 12
            elif int(time.group(1))+12 > 24:
                raise ValueError("Invalid time format")
            else:
                hours = int(time.group(1))+12

            minutes = int(time.group(2))
            formatted_timings.append(f"{hours:02}:{minutes:02}")

        elif t[-2:] == "AM":
            time = re.search(r"([0-9]+).+", t, re.IGNORECASE)
            if int(time.group(1)) == 12:
                hours = 0
            elif int(time.group(1)) > 24:
                raise ValueError("Invalid time format")
            else:
                hours = int(time.group(1))

            formatted_timings.append(f"{hours:02}:00")

        elif t[-2:] == "PM":
            time = re.search(r"([0-9]+).+", t, re.IGNORECASE)
            if int(time.group(1))+12 == 24:
                hours = 12
            elif int(time.group(1))+12 > 24:
                raise ValueError("Invalid time format")
            else:
                hours = int(time.group(1))+12

            formatted_timings.append(f"{hours:02}:00")

    if int(hours) > 24:
        raise ValueError("Invalid time format")


    return f"{formatted_timings[0]} to {formatted_timings[1]}"


if __name__ == "__main__":
    main()
