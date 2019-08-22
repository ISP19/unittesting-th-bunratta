import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.


     Note:
         0/0 form is represented as NaN (short form of Not a Number)
         1/0 denotes a indeterminate form of positive infinity (math.inf).
         -1/0 denotes a indeterminate form of negative infinity (-math.inf).
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

    @classmethod
    def to_comparable(cls, obj):
        """Convert the given number into its comparable form

        Args:
            obj: The given number

        Returns:
            any: The given object in its comparable form
        """
        if type(obj) != cls:
            return obj
        else:
            return obj.to_decimal()

    @classmethod
    def from_str(cls, frac_str: str):
        """Converts a fraction representation into a Fraction object

        Args:
            frac_str (str): A fraction representation to convert

        Returns:
            Fraction: The parsed result from string representation
        """
        if "/" not in frac_str:
            raise ValueError("Invalid fraction representation")
        numerator, denominator = frac_str.split("/")
        return Fraction(int(numerator), int(denominator))

    # TODO: Add tests for this one
    def __gt__(self, other):
        return self.to_decimal() > Fraction.to_comparable(other)

    # TODO: Add tests for this one
    def __lt__(self, other):
        return self.to_decimal() < Fraction.to_comparable(other)

    # TODO: Add tests for this one
    def __neg__(self):
        numerator = -self.numerator
        return Fraction(numerator, self.denominator)

    # TODO: Add more tests for this one
    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is the same as 1/2).
        """
        if self.is_infinity:
            return False
        else:
            if type(frac) == int:
                return self.numerator == frac
            else:
                return self.to_decimal() == Fraction.to_comparable(frac)

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
