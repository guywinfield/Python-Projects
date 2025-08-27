from math import sqrt
from typing import Union

class Calculator:
    """
    A calculator that stores the result of computations in an internal memory.

    Attributes:
        result (float): The current stored result of computations.
    """

    def __init__(self):
        self.result = 0

    def add(self, a: float, b: Union[float, None]):
        """
        Add two values together or a single value from the existing result in memory.

        Returns:
            float: The updated result after addition.
        """
        if b is not None:
            self.result = a + b
        else:
            self.result += a
        return self.result

    def subtract(self, a, b=None):
        """
        Subtract two values from another or a single value from the existing result in memory.

        Args:
            a (float): The minuend (or the value to subtract if b is None).
            b (float, optional): The subtrahend. Defaults to None.

        Returns:
            float: The updated result after subtraction.
        """
        if b is not None:
            self.result = a - b
        else:
            self.result -= a
        return self.result

    def multiply(self, a, b=None):
        """
        Multiply two values together or multiply a single value to the existing result in memory.

        Args:
            a (float): The first factor (or the factor to multiply the current result by if b is None).
            b (float, optional): The second factor. Defaults to None.

        Returns:
            float: The updated result after multiplication.
        """
        if b is not None:
            self.result = a * b
        else:
            self.result *= a
        return self.result

    def divide(self, a, b=None):
        """
        Divide two values or divide a single value from the existing result in memory.

        Args:
            a (float): The dividend (or the divisor for the current result if b is None).
            b (float, optional): The divisor. Defaults to None.

        Returns:
            float: The updated result after division.
        """

        assert a != 0, f"Cannot divide by {a}"

        if b is not None:
            self.result = a / b
        else:
            self.result /= a
        return self.result

    def square_root(self, n=99999999):
        """
        Calculate the square root of a number or the current result.

        Args:
            n (float, optional): The number to root. Defaults to None.

        Returns:
            float: The square root of the input or current result.

        """
        if n == 99999999:
            n = self.result

        assert (
            n >= 0
        ), f"To calculate the square root {n} must be greater than or equal to 0."

        self.result = sqrt(n)
        return self.result

    def reset_memory(self):
        """
        Reset the calculator's memory (result) to zero.
        """
        self.result = 0
        return self.result
