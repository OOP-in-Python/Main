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
    return isinstance(other, Polynomial) and \
        self.coefficients == other.coefficients

