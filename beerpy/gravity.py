"""
Functions for converting gravity units. Source:
http://www.mathe-fuer-hobbybrauer.de/bierrezepte/index.html

"""

from scipy.interpolate import interp1d

PL = "pl"  # unit degree plato
PL_UNIT = "°P"
SG = "sg"  # unit specific gravity
SG_UNIT = "kg/m³"
EG = "eg"  # unit extract gravity
EG_UNIT = "g/l"


# list with gravities in °Pl
_pl = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# list with extract gravity in g/l
_eg = [61,  72,  83,  93, 104, 115, 126, 137,
       148, 159, 170, 182, 193, 205, 217]

# list with specific gravity (SG)
_sg = [1024, 1027, 1032, 1036, 1040, 1044, 1048, 1052, 1057,
       1060, 1065, 1070, 1074, 1077, 1083]


def _interpolate(xdata, ydata, xval):
    f = interp1d(xdata, ydata)
    return f(xval)


def pl_to_eg(val):
    """
    Calculate extract gravity from °Pl.

    :param val: gravity in °Pl
    :returns: extract gravity in g/l

    """
    return int(_interpolate(_pl, _eg, val))


def pl_to_sg(val):
    """
    Calculate specific gravity from °Pl.

    :param val: gravity in °Pl
    :returns: specific gravity (SG)

    """
    return int(_interpolate(_pl, _sg, val))


def eg_to_pl(val):
    """
    Calculate °Pl from extract gravity.

    :param val: extract gravity in g/l
    :returns: gravity in °Pl

    """
    return _interpolate(_eg, _pl, val)


def eg_to_sg(val):
    """
    Calculate specific gravity from extract gravity.

    :param val: extract gravity in g/l
    :returns: specific gravity (SG)

    """
    return int(_interpolate(_eg, _sg, val))


def sg_to_pl(val):
    """
    Calculate °Pl from specific gravity.

    :param val: specific gravity (SG)
    :returns: gravity in °Pl

    """
    return _interpolate(_sg, _pl, val)


def sg_to_eg(val):
    """
    Calculate extract gravity from specific gravity.

    :param val: specific gravit (SG)
    :returns: extract gravity in g/l

    """
    return int(_interpolate(_sg, _eg, val))


class Gravity:

    def __init__(self, value, unit=PL):
        self._sg = None
        self._unit = unit

        if unit == SG:
            self.sg = value
        elif unit == PL:
            self.pl = value
        elif unit == EG:
            self.eg = value
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
        elif self._unit == EG:
            val = self.eg
            unit = EG_UNIT
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

    # eg property
    @property
    def eg(self):
        """
        get / set value of the gravity in g/l

        """
        return sg_to_eg(self._sg)

    @eg.setter
    def eg(self, value):
        self._sg = eg_to_sg(value)
