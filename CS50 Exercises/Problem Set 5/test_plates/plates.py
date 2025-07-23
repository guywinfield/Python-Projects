
import string

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(text):
    text = text.strip()

    len_counter = 0
    num_counter = 0
    checked_string = ""

    for s in text:
        if s in string.punctuation or s.isspace():
            return False

        elif s.isdigit() and len_counter < 2:
            return False

        elif len_counter >= 6:
            return False

        elif s.isdigit() and num_counter == 0 and s == "0":
            return False

        elif s.isdigit():
            len_counter += 1
            num_counter += 1
            checked_string = checked_string + s

        else:
            len_counter += 1
            checked_string = checked_string + s


    numbered_section = checked_string[2:]

    if num_counter > 0 and checked_string[-1].isalpha() == True:
        return False
    elif len_counter <= 2:
        return False
    elif len_counter > 4 and (numbered_section[0].isdigit() and numbered_section[-1].isdigit()) and (numbered_section[1].isalpha() or numbered_section[2].isalpha()):
        return False
    else:
        return True


if __name__ == "__main__":
    main()








