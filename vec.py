import sys
import random
import math
from typing import Self

"""
A custom vector class implementation for educational purposes.
"""

class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = []
        else:
            elements = list(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        return Vec([round(x + y, 5) for x, y in zip(self.elements, t.elements)])

    def __mul__(self, t: int | float | Self) -> Self:
    # 1. Handle scalar multiplication (v1 * 2)
        if isinstance(t, (int, float)):
            return Vec([round(x * t, 5) for x in self.elements])

    # 2. Handle vector multiplication (v1 * v2)
        if isinstance(t, Vec):
            if len(self.elements) != len(t):
                raise TypeError("Type error - vectors must be of the same dimensions")
        return Vec([round(x * y, 5) for x, y in zip(self.elements, t.elements)])

    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        #
        return Vec(tuple(round(x * scalar, 5) for x in self.elements))

    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        #for i, val in enumerate(self.elements):
         #   self.elements[i] = round(val * scalar, 5)
        self.elements = tuple(round(scalar*x, 5) for x in self.elements)

        return self

    def __repr__(self) -> str:
        return f"Vector + {self.elements}"

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        return Vec([round(x - y, 5) for x,y in zip(self.elements, t.elements)])

    def __neg__(self) -> Self:
        return Vec([x * (-1) for x in self.elements])


    def __radd__(self, scalar):
        if not isinstance(scalar, (int,float)):
            raise TypeError(f"Vector addition with invalid type: {type(scalar)}")
        return Vec([round(x+scalar, 5) for x in self.elements])


    def __iadd__(self, scalar):
        if not isinstance(scalar, (int,float)):
            raise TypeError(f"Vector addition with invalid type: {type(scalar)}")
        return Vec([round(scalar+x, 5) for x in self.elements])

    # return a vector of @n zeroes. precondition: @n > 0
    @staticmethod
    def zeros(n: int) -> Self:
        if not isinstance(n, int):
          raise TypeError(f"Expected an integer:{type(n)}")
        if n<0:
          raise ValueError("Number should be positive")

        return Vec([0]*n)


    # return a vector of @n. precondition: @n > 0
    @staticmethod
    def ones(n: int) -> Self:
        if not isinstance(n, int):
          raise TypeError(f"Expected an integer:{type(n)}")
        if n<0:
          raise ValueError("Number should be positive")

        return Vec([1]*n)

    # return a vector of @n uniformly distributed numbers in [0, 1]. precondition: @n > 0
    @staticmethod
    def uniform(n: int) -> Self:
        if n<0:
          raise ValueError("Number should be positive")
        return Vec([round(random.uniform(0.0, 1.0), 5) for i in range(n)])

    # Calculates the Euclidean norm (L2 norm) of the vector.
    # sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)
    def norm(self) -> float:
        e_norm = self.elements
        sum_squares = sum(x**2 for x in e_norm)
        result = math.sqrt(sum_squares)

        return round(result, 5)

    def mean(self) -> float:
        if len(self.elements) == 0:
            raise ValueError("Cannot calculate mean of an empty vector")
        return sum(self.elements) / len(self.elements)

    def demean(self) -> Self:
        mean_value = self.mean()
        return Vec([round(x - mean_value, 5) for x in self.elements])

    def std(self) -> float:
        de_meaned = self.demean()
        squared_sum = sum(x**2 for x in de_meaned.elements)
        result = math.sqrt(squared_sum / len(self.elements))
        return round(result, 5)


"""
(1) Understand the basic design of the vector abstraction. Review the implementation.
(2) Document each function.
(3) Implement all unimplemented methods.
(4) Create appropriate tests for this implementation, increasing the confidence about its correctness.
(5) Test this implementation by importing the class in a sepatate python script.

(6) Measure the performance of each of these functions on vectors of varying lengths.
    Try 2k to 64k dimension vectors and time the results.
    How would you do the measurements?
(7) Measure the performance on your machine. Check it on colab.

(8) use numpy and compare the performance.
"""


if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":
    #z1 = Vec.zeros(10)
    v1 = Vec([0, 1, 1.04])
    v2 = Vec([2, 0.6, 4.4])

    print("v1 = ", v1)
    print("v2 = ", v2,"\n")

    print("Vector Addition:", v1+v2)
    print("Vector Subtraction:", v1-v2)
    print("Vector Scalar Additions:", 5+v1, 10+v2,"\n")


    print("Vector Multiplication:", v1*v2)
    print("Vector Scalar Multiplication:",v1*2)
    print("Vector Scalar Multiplication:", 2*v2 ,"\n")

    print("Vector Negation:", -v1,"\n")

    print("Vector of zeros:", Vec.zeros(5))
    print("Vector of ones:", Vec.ones(5),"\n")

    print("Uniform vector:", Vec.uniform(5),"\n")
    print("Euclidean Norm:", v1.norm())

    print("Mean:", v1.mean())
    print("Demeaned Vector:", v1.demean())
    print("Standard Deviation:", v1.std())