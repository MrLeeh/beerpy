import pytest

from beerpy.units import Concentration


def test_init():
    c = Concentration(5)
    assert repr(c) == "Concentration: 5g/l"


def test_value_and_unit():
    c = Concentration(5)
    assert c.value == 5
    assert c.unit == "g/l"
