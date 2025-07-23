# Calculator
A simple Python calculator class that maintains stateful memory and supports basic arithmetic operations.

### Description
Calculator is a lightweight class that stores a running total in its internal result attribute and provides methods for basic arithmetic:
- Addition (add) of one or two values
- Subtraction (subtract) of one or two values
- Multiplication (multiply) of one or two values
- Division (divide) of one or two values, with zero-division checks
- Square Root (square_root) of a value or the current result, with non-negative validation
- Memory Reset (reset_memory) to clear the stored result

You can perform operations on standalone inputs or chain them by relying on the stored memory.


## Getting Started

### Prerequisites
- Python 3.6 or later
- pytest (for running the unit tests)

_No additional external packages are required._


### Installation
- Clone the repository
```
git clone https://github.com/TuringCollegeSubmissions/gwinfi-DS.v3.1.2.5.git
cd calculator
```
- Install dependencies
```pip install pytest```

### Executing program
Import and use Calculator in your code or an interactive shell:
```
from calculator import Calculator

calc = Calculator()
print(calc.add(2, 3))        # 5
print(calc.subtract(10, 4))  # 6
print(calc.multiply(3, 7))   # 21
print(calc.divide(20, 5))    # 4.0
```

Chaining operations from the existing result:
```
calc.reset_memory()          # result = 0
calc.add(5)                  # result = 5
calc.multiply(2)             # result = 10
print(calc.square_root())    # result = sqrt(10)
```

Alternatively I've also included a main.py to run an existing template: 
`python main.py` 

### Running Tests
Unit tests are written with pytest. To run all tests (albeit there is only 1 test file):
`pytest`


## Help
There are 2 built in assertion errors to avoid mathmatical impossibilities:

`square_root`
- AssertionError: To calculate the square root -1 must be greater than or equal to 0.

`divide`
- AssertionError: Cannot divide by 0

## Authors
Contributors names and contact info:

Guy Winfield

Discord: @guyw7698

## Version History
0.1
Initial Release