import emoji


def main():
    return_emoji("Input: ")


def return_emoji(prompt):
    text = input(prompt).strip()
    return print("Output: " + emoji.emojize(text, language="alias"))


main()
