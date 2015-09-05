import pytest
import beerpy.units as units


def test_init_temperature():
    t1 = units.Temperature(20)
    assert repr(t1) == "Temperature: 20°C"
    t2 = units.Temperature(68, units.FAHRENHEIT)
    assert repr(t2) == "Temperature: 68°F"


def test_conversion():
    t = units.Temperature(20)
    assert t.celsius == 20.0
    assert t.fahrenheit == 68.0

    t = units.Temperature(68, units.FAHRENHEIT)
    assert t.fahrenheit == 68.0
    assert t.celsius == 20.0
