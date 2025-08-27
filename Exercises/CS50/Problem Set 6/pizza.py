import sys
import csv
from tabulate import tabulate


def main():
    print(tabulate_pizza())


def tabulate_pizza():
    pizza_list = []
    file_name = get_file_name()

    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)

            if file_name == "regular.csv":
                for row in reader:
                    pizza_list.append(
                        {
                            "Regular Pizza": row["Regular Pizza"],
                            "Small": row["Small"],
                            "Large": row["Large"],
                        }
                    )
            elif file_name == "sicilian.csv":
                for row in reader:
                    pizza_list.append(
                        {
                            "Sicilian Pizza": row["Sicilian Pizza"],
                            "Small": row["Small"],
                            "Large": row["Large"],
                        }
                    )

        table = tabulate(pizza_list, headers="keys", tablefmt="grid")
        return table

    except FileNotFoundError:
        sys.exit("File does not exist")


def get_file_name():
    if len(sys.argv[1:]) < 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv[1:]) > 1:
        sys.exit("Too many command-line arguments")
    elif sys.argv[-1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        file_name = sys.argv[-1]

    return file_name


if __name__ == "__main__":
    main()
