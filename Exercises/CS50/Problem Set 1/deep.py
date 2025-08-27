def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    # is_answer_to_everything() function which checks whether answer is 43
    print(is_answer_to_everything(answer))

def is_answer_to_everything(x):
    #remove blank spaces and lowercase to avoid data quality issues
    x = x.strip().lower()

    match x:
        case "forty-two" | "forty two" | "42":
            y = "Yes"
        case _:
            y = "No"
    return y

main()

