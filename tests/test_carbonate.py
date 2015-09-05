import pytest
import beerpy.units as units
from beerpy.carbonate import saturation, carbonisation


def test_saturation():
    assert saturation(units.Temperature(0)) == 3.2
    assert saturation(units.Temperature(20)) == 1.65


def test_carbonisation():
    assert carbonisation(5.0, units.Temperature(22)) == 3.4
