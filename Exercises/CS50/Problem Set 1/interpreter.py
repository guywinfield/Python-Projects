def main():
    equation = input("Expression: ")
    print(calculate(equation))

def calculate(e):
    # separate expression into separate arguments
    x, y, z = e.split(" ")

    x = int(x)
    z = int(z)

    # Decide what calculation to do based on the symbol inputted
    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    elif y == "/":
        return float(x / z)
    # The user might try something more advanced so let's avoid bugs with this message
    else:
        return("Can't execute too much complexity 🙁")

main()



