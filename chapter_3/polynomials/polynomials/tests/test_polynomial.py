from polynomials import Polynomial


def test_print():

    p = Polynomial((2, 1, 0, 9))

    assert str(p) == "9x^3 + x + 2"