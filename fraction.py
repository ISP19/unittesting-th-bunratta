import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.

    0/0 form is represented as NaN (short form of Not a Number)
    """
    
    def __init__(self, numerator, denominator=1):
        """Initializes a new fraction with the given numerator
           and denominator (default 1).
        """
        self.is_infinity = False
        gcd = math.gcd(numerator, denominator)
        if denominator is 0 and (numerator is -1 or numerator is 1):
            self.is_infinity = True
        self.numerator = int(numerator / gcd)
        self.denominator = int(denominator / gcd)
        if self.denominator < 0 or self.numerator == 0:
            if self.denominator < 0:
                self.numerator *= -1
                self.denominator *= -1

    def __add__(self, frac):
        """Returns the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)

           Args:
               frac (Fraction): Another fraction to add
           Returns:
               Fraction: The summation of both operated fractions
        """
        numerator_result = (self.numerator*frac.denominator) + (frac.numerator*self.denominator)
        denominator_product = self.denominator*frac.denominator
        return Fraction(numerator_result, denominator_product)

    def __sub__(self, other):
        """Returns the difference of two fractions as a new fraction.
            Args:
                other (Fraction): Another fraction to subtract

            Returns:
                Fraction: The difference result of both operated fractions
        """
        other.numerator *= -1
        return self.__add__(other)

    def __mul__(self, other):
        """Returns the product of two fractions according to multiplication rule of fractions
           A fraction of which denominator of 0 will not be allowed unless it has a numerator of 1.
        Note:
            1/0 denotes a indeterminate form of positive infinity (math.inf).
            -1/0 denotes a indeterminate form of negative infinity (math.inf).
        Args:
            other (Fraction): Another fraction to multiply

        Returns:
            Fraction: The product of both operated fractions
        """
        numerator_result = self.numerator*other.numerator
        denominator_result = self.denominator*other.denominator
        return Fraction(numerator_result, denominator_result)

    def to_decimal(self):
        """Converts this fraction to its decimal equivalent

        Returns:
            float: The decimal representation
        """
        return float(self.numerator/self.denominator)

    # Optional have fun and overload other operators such as
    # __gt__  for f > g
    # __neg__ for -f (negation)

    # TODO
    def __gt__(self, other):
        return self.to_decimal() > other.to_decimal()

    # TODO
    def __lt__(self, other):
        return self.to_decimal() < other.to_decimal()

    # TODO
    def __neg__(self):
        numerator = -self.numerator
        return Fraction(numerator, self.denominator)

    # TODO
    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is the same as 1/2).
        """
        if self.is_infinity:
            return False
        else:
            return self.numerator/self.denominator == frac.numerator/frac.denominator

    def __str__(self):
        """Represents fractions in terms of the numerator over denominator
        The fraction of which denominator of 1 is represented in whole number instead.
        Returns:
            str: A string representation of a Fraction
        """
        if self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"

    def __new__(cls, numerator, denominator=1):
        if denominator is 0:
            if numerator is 0:
                return math.nan
            elif numerator is 1 or numerator is -1:
                return numerator*math.inf
            else:
                raise ValueError("A fraction cannot have a denominator of zero")
        elif denominator is 1:
            return numerator
        else:
            return object.__new__(cls)
