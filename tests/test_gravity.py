import pytest
from beerpy.units.gravity import pl_to_sg, sg_to_pl


def test_pl_to_sg():
    assert pl_to_sg(6) == 1.024
    assert pl_to_sg(12) == 1.048
    assert pl_to_sg(20) == 1.083


def test_sg_to_pl():
    assert sg_to_pl(1.024) == 6.
    assert sg_to_pl(1.048) == 12.
    assert sg_to_pl(1.083) == 20.
