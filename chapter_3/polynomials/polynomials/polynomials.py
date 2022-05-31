from numbers import Number

class Polynomial:

  def __init__(self, coefs):
      self.coefficients = coefs

  def degree(self):
    return len(self.coefficients) - 1
  
  def __str__(self):

    coefs = self.coefficients
    terms = []

    # Degree 0 and 1 terms conventionally have different representations.
    if coefs[0]:
      terms.append(str(coefs[0]))
    if self.degree() > 0 and coefs[1]:
      # f-string terminology, lookup if necessary
      terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

    # Remaining terms look like cx^d, with factors of 1 dropped.
    # Difference between append and += is that append just adds one term
    # whereas += concatenantes two lists.
    terms += [f"{'' if c == 1 else c}x^{d}"
    # Enumerate is a built-in function which yields a list of pairs containing a count
    # and value yielded by iterable argument (you can tell it at what point to start at).
    # eg: ((0, seq[0]), (1, seq[1]), (2, seq[2]), ...)
    # The code below works because d is really the degree of the x-term we're considering
    # (which is just the count of the iterable argument coefs), and c is the coefficient
    # term of the x-term, which is the value of the iterable argument coefs.
    # We are also counting coefs from position 2 onwards (since position 0 and 1 were dealt
    # with in previous lines of code).
              for d, c in enumerate(coefs[2:], start = 2) if c]

    # Sum polynomial terms from high to low exponent.
    # The join method takes a sequence of strings as arguments (in this case, the reversed 
    # sequence of terms, to fit mathematical convention of descending order of power),
    # with " + " in between the sequence of strings passed to the join method.
    # Code deals with zero polynomial because if passed a zero polynomial, all the if statements
    # are essentially false and join is passed an empty sequence of strings; so we pass a "0".
    return " + ".join(reversed(terms)) or "0"

  def __repr__(self):
    return type(self).__name__ + "(" + repr(self.coefficients) + ")"

  def __eq__(self, other):
    # isinstance() checks if other is a Polynomial class (which we want)
    # and then checks if the coefficients are equal between self and other
    return isinstance(other, Polynomial) and \
        self.coefficients == other.coefficients

  def __add__(self, other):
    # Checks if other is a Number or Polynomial class
    if isinstance(other, Number):
      return Polynomial((self.coefficients[0] + other,)
                        + self.coefficients[1:])
    elif isinstance(other, Polynomial):
      # Work out how many coefficient places the two polynomials have in
      # common.
      common = min(self.degree(), other.degree()) + 1
      # Sum the common coefficient positions.
      coefs = tuple(a + b for a, b in zip(self.coefficients[:common],
                                          other.coefficients[:common]))
      
      # Append the high degree coefficients from the higher degree
      # summand
      coefs += self.coefficients[common:] + other.coefficients[common:]

      return Polynomial(coefs)
    else:
      return NotImplemented
      
  def __radd__(self, other):
    return self + other