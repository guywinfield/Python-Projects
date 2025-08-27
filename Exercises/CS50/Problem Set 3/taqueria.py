
def main():
    order_total("Item: ")


def order_total(prompt):
    felipe = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }


    order_total = 0

    while True:
        try:
            order = input(prompt)
            order = order.title()

            order_total += felipe[order]
            print(f"Total: ${order_total:.2f}")

        except KeyError:
            pass

        except EOFError:
            break


main()
