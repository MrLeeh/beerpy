"""
Functions for converting gravity units. Source:
http://www.brewersfriend.com/plato-to-sg-conversion-chart

"""

from os.path import join, dirname

import pandas as pd
from scipy.interpolate import interp1d
from .constants import DATA_DIR


GRAVITY_FILE = join(dirname(__file__), DATA_DIR, "gravity.csv")
FCT_DATA = "data"
FCT_POLY = "poly"

PL = "pl"  # unit degree plato
PL_UNIT = "°P"
SG = "sg"  # unit specific gravity
SG_UNIT = "kg/m³"


_df_gravity = pd.read_csv(GRAVITY_FILE, sep=',', decimal='.')
_plato = list(_df_gravity.Plato)
_sg = list(_df_gravity.SG)


# polynomical functions
def _poly_pl_to_sg(pl):
    """
    Polynom for calculating sg from pl.

    """
    return 1.0 + (pl / (258.6 - ((pl / 258.2) * 227.1)))


def _poly_sg_to_pl(sg):
    """
    Polynom for calculating pl from sg.

    """
    return -616.868 + 1111.14 * sg - 630.272 * sg**2 + 135.997 * sg ** 3


def _data_pl_to_sg(pl):
    """
    Use data table and linear interpolation for calculating sg from pl.

    """
    f = interp1d(_plato, _sg)
    return float(f(pl))


def _data_sg_to_pl(sg):
    """
    Use data table and linear interpolation for calculating pl from sg.

    """
    f = interp1d(_sg, _plato)
    return float(f(sg))


def _interpolate(xdata, ydata, xval):
    """
    Interpolate between given points.

    """
    f = interp1d(xdata, ydata)
    return f(xval)


def pl_to_sg(pl, fct=FCT_DATA):
    """
    Calculate specific gravity from °Pl.

    :param pl: gravity in °Pl
    :returns: specific gravity (SG)

    """
    if fct == FCT_DATA:
        return _data_pl_to_sg(pl)
    elif fct == FCT_POLY:
        return _poly_pl_to_sg(pl)
    else:
        raise ValueError("value for parameter fct is not valid.")


def sg_to_pl(sg, fct=FCT_DATA):
    """
    Calculate °Pl from specific gravity.

    :param sg: specific gravity (SG)
    :returns: gravity in °Pl

    """
    if fct == FCT_DATA:
        return _data_sg_to_pl(sg)
    elif fct == FCT_POLY:
        return _poly_sg_to_pl(sg)
    else:
        raise ValueError("value for parameter fct is not valid.")


class Gravity:

    def __init__(self, value, unit=PL):
        self._sg = None
        self._unit = unit

        if unit == SG:
            self.sg = value
        elif unit == PL:
            self.pl = value
        else:
            raise TypeError("unit must have value PL, SG or"
                            "EG")

    def __repr__(self):
        if self._unit == SG:
            val = self.sg
            unit = SG_UNIT
        elif self._unit == PL:
            val = self.pl
            unit = PL_UNIT
        else:
            return "Gravity: None"
        return "Gravity: {}{}".format(val, unit)

    # pl property
    @property
    def pl(self):
        """
        get / set value of the gravity in °Pl

        """
        return sg_to_pl(self._sg)

    @pl.setter
    def pl(self, value):
        self._sg = pl_to_sg(value)

    # sg property
    @property
    def sg(self):
        """
        get / set value of the gravity in kg/m³

        """
        return self._sg

    @sg.setter
    def sg(self, value):
        self._sg = value
