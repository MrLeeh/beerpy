"""
Functions for converting gravity units. Source:
http://www.brewersfriend.com/plato-to-sg-conversion-chart

"""

import os

import pandas as pd
from scipy.interpolate import interp1d
from ..utilities import datadir


FCT_DATA = "data"
FCT_POLY = "poly"


PLATO = "°P"
SPECIFIC_GRAVITY = "kg/m³"
_units = (PLATO, SPECIFIC_GRAVITY)

_f_gravity = os.path.join(datadir(), "gravity.csv")
_df_gravity = pd.read_csv(_f_gravity, sep=',', decimal='.')

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


def _pl_to_sg(pl, fct=FCT_DATA):
    """
    Calculate specific gravity from °Pl.

    :param pl: gravity in °Pl
    :returns: specific gravity (SPECIFIC_GRAVITY)

    """
    if fct == FCT_DATA:
        return _data_pl_to_sg(pl)
    elif fct == FCT_POLY:
        return _poly_pl_to_sg(pl)
    else:
        raise ValueError("value for parameter fct is not valid.")


def _sg_to_pl(sg, fct=FCT_DATA):
    """
    Calculate °Pl from specific gravity.

    :param sg: specific gravity (SPECIFIC_GRAVITY)
    :returns: gravity in °Pl

    """
    if fct == FCT_DATA:
        return _data_sg_to_pl(sg)
    elif fct == FCT_POLY:
        return _poly_sg_to_pl(sg)
    else:
        raise ValueError("value for parameter fct is not valid.")


class Gravity:

    def __init__(self, value, unit=PLATO):
        self.value = value
        self._unit = unit

        assert unit in _units, "unit parameter not in {}".format(_units)

    def __repr__(self):
        return "Gravity: {}{}".format(self.value, self.unit)

    @property
    def unit(self):
        return self._unit

    # pl property
    @property
    def plato(self):
        """
        get / set value of the gravity in °Pl

        """
        if self.unit == PLATO:
            return self.value
        elif self.unit == SPECIFIC_GRAVITY:
            return _sg_to_pl(self.value)

    @plato.setter
    def plato(self, value):
        if self.unit == PLATO:
            self.value = value
        elif self.unit == SPECIFIC_GRAVITY:
            self.value = _pl_to_sg(value)

    # sg property
    @property
    def specific_gravity(self):
        """
        get / set value of the gravity in kg/m³

        """
        if self.unit == PLATO:
            return _pl_to_sg(self.value)
        elif self.unit == SPECIFIC_GRAVITY:
            return self.value

    @specific_gravity.setter
    def specific_gravity(self, value):
        if self.unit == PLATO:
            self.value = _sg_to_pl(value)
        elif self.unit == SPECIFIC_GRAVITY:
            self.value = value
