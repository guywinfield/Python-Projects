import random

def main():
    print(guess_random("Level: "))

def guess_random(prompt):

    level = input_is_positive_int(prompt)
    answer = random.randint(1,level)

    while True:
        try:
            guess = input_is_positive_int("Guess: ")

            if guess > answer:
                print("Too large!")
            elif guess < answer:
                print("Too small!")
            else:
                return "Just right!"

        except (ValueError,TypeError):
            pass
        except EOFError:
            break


def input_is_positive_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x > 0:
                return x
            else:
                pass
        except (ValueError,TypeError):
            pass
        except EOFError:
            break

main()
