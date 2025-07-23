
def main():
    user_word = input("camelCase: ")
    snake_convert(user_word)

def snake_convert(text):
    text = text.strip()

    i = 0
    for t in text:
        if i == 0:
            print(t.lower(), end="")
            i += 1
        elif t.isupper():
            print("_" + t.lower(), end="")
            i += 1
        else:
            print(t, end="")
            i += 1
    print()

main()
