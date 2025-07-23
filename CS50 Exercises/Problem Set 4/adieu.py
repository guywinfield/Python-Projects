import inflect

p = inflect.engine()


def main():
    print(adieu())


def adieu():
    adieu_string = "Adieu, adieu, to "
    name_list = []
    name_count = 0

    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
            name_count += 1

        except EOFError:
            if name_count == 1:
                adieu_string += name
            else:
                adieu_string += p.join(name_list)

            print()
            return adieu_string


main()
