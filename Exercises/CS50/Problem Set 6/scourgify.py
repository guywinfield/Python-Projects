
import sys
import csv
import re


def main():
    create_new_file()


def get_file_names():
    if len(sys.argv[1:]) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv[1:]) > 2:
        sys.exit("Too many command-line arguments")
    else:
        before = sys.argv[1]
        after = sys.argv[-1]

    return before, after


def _clean(string):
    return re.sub(r'\s+', '', string).replace('"', '').rstrip('\n')

def create_new_file():
    before, after = get_file_names()

    before_list = []

    with open(before, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            before_list.append({
                "name": _clean(row["name"]),
                "house": _clean(row["house"])
            })

    after_list = []
    for entry in before_list:
        last_name, first_name = entry["name"].split(',',1)
        after_list.append({
            "first_name": first_name,
            "last_name": last_name,
            "house": row["house"]
        })

    with open(after, 'w', newline='') as file:
        field_names = ["first_name","last_name","house"]
        writer = csv.DictWriter(file, fieldnames=field_names,lineterminator='\n')

        writer.writeheader()
        writer.writerows(after_list)

    return after_list


if __name__ == "__main__":
    main()

