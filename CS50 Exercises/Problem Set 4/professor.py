import random


def main():
    level = get_level()
    maths_game(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if 0 < level <=3:
                return level
            else:
                pass

        except ValueError:
            pass
        except EOFError:
            break


def generate_integer(level):
    x = 0
    y = 0

    if level == 1:
        x = random.randint(1,9)
        y = random.randint(1,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x,y


def maths_game(level):
    score = 0
    counter = 0

    while counter != 10:
        x,y = generate_integer(level)
        equation_string =  str(x) + " + " + str(y) + " = "
        guess = int(input(equation_string))

        if guess == x + y:
            score +=1
            counter += 1

        elif guess != x + y:
            print("EEE")
            incorrect_guesses = 1

            while incorrect_guesses < 3:
                equation_string =  str(x) + " + " + str(y) + " = "
                guess = int(input(equation_string))

                if guess == x + y:
                    score +=1

                else:
                    print("EEE")
                    incorrect_guesses += 1
                    pass

            correct_answer = x + y
            print(str(x),"+",str(y),"=",correct_answer)
            pass

    return print("Score:",score)


if __name__ == "__main__":
    main()



