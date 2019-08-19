class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        #TODO write this (and remove this TODO comment)
        self.numerator = numerator
        self.denominator = denominator
        pass

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator_result = (self.numerator*frac.denominator) + (frac.numerator*self.denominator)
        denominator_product = self.denominator*frac.denominator
        return Fraction(numerator_result, denominator_product)

    def __sub__(self, other):
        other.numerator *= -1
        return self.__add__(other)

    #TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    #Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is the same as 1/2).
        """
        return self.numerator/self.denominator == frac.numerator/frac.denominator
