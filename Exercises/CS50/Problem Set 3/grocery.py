

def main():
    shop_aggregate()

def shop_aggregate():
    from collections import Counter
    shopping_list = []

    while True:
        try:
            item = input().upper()
            shopping_list.append(item)
            shopping_list.sort()

        except EOFError:
            shopping_dict = Counter(shopping_list)

            for item in shopping_dict:
                print(f"{shopping_dict[item]} {item}")

            break

main()
