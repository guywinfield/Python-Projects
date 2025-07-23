def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(text):
    text = text.lower()
    vowels = ["a","e","i","o","u"]
    new_text = ""

    for c in text:
        if c.lower() in vowels:
            pass
        else:
            new_text += c

    return new_text

if __name__ == "__main__":
    main()


