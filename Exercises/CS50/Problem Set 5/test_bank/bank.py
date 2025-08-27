def main():
    user = input("Greeting: ")

    output = value(user)
    print(f"${output:.0f}")

def value(response):
    response = response.lower()

    if response.startswith("hello"):
        value = 0

    elif response.startswith("h"):
        value = 20

    else:
        value = 100

    return value

if __name__ == "__main__":
    main()
