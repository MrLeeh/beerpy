import pytest
from beerpy.units.gravity import _pl_to_sg, _sg_to_pl, Gravity, PLATO, \
    SPECIFIC_GRAVITY


def test_pl_to_sg():
    assert _pl_to_sg(6) == 1.024
    assert _pl_to_sg(12) == 1.048
    assert _pl_to_sg(20) == 1.083


def test_sg_to_pl():
    assert _sg_to_pl(1.024) == 6.
    assert _sg_to_pl(1.048) == 12.
    assert _sg_to_pl(1.083) == 20.


def test_init():
    g = Gravity(20)
    assert g.unit == PLATO
    assert g.value == 20


def test_plato():
    g = Gravity(20)
    assert g.plato == 20
    assert g.specific_gravity == 1.083


def test_specific_gravity():
    g = Gravity(1.083, unit=SPECIFIC_GRAVITY)
    assert g.plato == 20
    assert g.specific_gravity == 1.083
