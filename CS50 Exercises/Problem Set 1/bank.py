import string

def main():
    greeting = input("Greeting: ")
    print(greeting_reward(greeting))

def greeting_reward(x):
    # Chatgpt helped me create this "translation map" which,
    # 1st argument is what we translate from (here it's nothing), 2nd is what we translate to (here it's nothing), 3rd argument what is to be deleted (all punctation from string library)
    table = str.maketrans('', '', string.punctuation)

    # We first clean the input to remove blank spaces and make all lower case
    # Split turns the input into a list, we want to know about the first word in the input which is the first entry in our list
    x = x.strip().lower().split(" ", maxsplit = 1)[0]
    x = x.translate(table)

    # We then check this first word to see which reward it matches to
    if x == "hello":
        y = "$0"
    elif x.startswith("h"):
        y = "$20"
    else:
        y = "$100"

    return y

main()

