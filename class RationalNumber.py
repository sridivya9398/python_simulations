class RationalNumber:
    """
    Rational Numbers with support for arithmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
        >>> a - b
        1/6
        >>> a * b
        1/6
        >>> a / b
        3/2
    """
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.n = numerator
        self.d = denominator
        self.simplify()

    def simplify(self):
        gcd_value = self.gcd(self.n, self.d)
        self.n //= gcd_value
        self.d //= gcd_value

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2 - n2*d1, d1*d2)

    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*n2, d1*d2)

    def __truediv__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        if n2 == 0:
            raise ZeroDivisionError("Cannot divide by a rational number with numerator zero.")
        return RationalNumber(n1*d2, d1*n2)

    def __lt__(self, other):
        return self.n * other.d < self.d * other.n

    def __eq__(self, other):
        return self.n * other.d == self.d * other.n

    def __gt__(self, other):
        return self.n * other.d > self.d * other.n

    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    __repr__ = __str__
