

def main():
    print(fuel_pct_calculator("Fraction: "))

def fuel_pct_calculator(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split("/")

            x = int(x)
            y = int(y)

            result = (x / y)

            if result <= 0.01:
                return "E"
            elif 0.99 <= result <= 1:
                return "F"
            elif result > 1:
                pass
            else:
                return  f"{result:.0%}"

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()
