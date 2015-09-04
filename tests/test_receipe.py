import pytest

from beerpy.receipe import hop_quantity, malt_composition, PILSENER_MALT, \
    MUNICH_MALT
from beerpy.units.gravity import Gravity


def test_malt_composition():
    res = malt_composition(
        22, Gravity(14), [(PILSENER_MALT, 0.8), (MUNICH_MALT, 0.2)]
    )
    assert res[0] == 5.44
    assert res[1][0] == ('Pilsener Malz', 4.35)
    assert res[1][1] == ('Münchener Malz', 1.09)


def test_hop_quantity():
    res = hop_quantity(40, 5.5, 22, 60, Gravity(20))
    assert "{:.2f}".format(res) == "82.84"
