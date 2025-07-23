
def main():
    starting_amount = 50
    insert_coin(starting_amount)


def insert_coin(balance):
    valid_coins = [5, 10, 25]

    while True:
        print("Amount Due: ",balance)
        coin = int(input("Insert Coin: "))

        if (coin in valid_coins) and (balance - coin > 0):
            balance -= coin
        elif (coin in valid_coins):
            print("Change Owed:",(balance - coin) * -1)
            break

main()

