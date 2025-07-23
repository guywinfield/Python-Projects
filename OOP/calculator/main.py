from calculator import Calculator


def main():
    cal = Calculator()

    a = 20
    b = 30
    print(f"Let's start with an addition: {a} + {b} =", cal.add(a, b))
    n = 80
    print(f"Subtract {n}:", cal.subtract(n))
    n = -10
    print(f"Multiply by {n}:", cal.multiply(n))
    n = 2
    print(f"Divide by {n}:", cal.divide(n))
    print(f"Square Root of {cal.result}:", cal.square_root(cal.result))
    print(f"Now wipe our calculator clean:", cal.reset_memory())


if __name__ == "__main__":
    main()
