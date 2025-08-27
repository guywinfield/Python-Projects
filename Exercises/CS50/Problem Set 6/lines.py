
import sys


row_counter = 0
docstring_count = 0

try:
    if len(sys.argv[1:]) > 1:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv[1:]) < 1:
        sys.exit("Too few command-line arguments")
    elif sys.argv[-1].endswith(".py") is False:
        sys.exit("Not a Python file")
    else:
        file_name = sys.argv[1]
        with open(file_name) as file:
            for row in file:
                if row.lstrip().startswith("#"):
                    pass
                elif not row.strip():
                    pass
                elif (len(row.strip()) > 3 and row.lstrip()[:3] == '"""' and row.strip()[-3:] == '"""') or (len(row.strip()) > 3 and row.lstrip()[:3] == "'''" and row.strip()[-3:] == "'''"):
                    pass
                elif (row.lstrip()[:3] == '"""' or row.strip()[-3:] == '"""') or (row.lstrip()[:3] == "'''" or row.strip()[-3:] == "'''"):
                    docstring_count +=1
                else:
                    if docstring_count % 2 == 0:
                        row_counter += 1
                    else:
                        pass

        print(row_counter)


except FileNotFoundError:
    sys.exit("File does not exist")
