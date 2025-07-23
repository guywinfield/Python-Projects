def main():
    text = input("Input: ")
    print(remove_vowels(text))

def remove_vowels(text):
    vowels = ["a","e","i","o","u"]
    new_text = ""

    for c in text:
        if c.lower() in vowels:
            pass
        else:
            new_text += c

    return new_text

main()
