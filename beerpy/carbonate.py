"""
Module for calculating the beer carbonation.

Typical carbonate concentrations for common beer types are listed in the table
below [1]_.

============= ========== ==========
sort          min. (g/l) max. (g/l)
============= ========== ==========
lager         4.4        5.5
wheat beers   6.5        9.0
british ale   3.0        4.0
porter, stout 3.4        4.6
belgian beer  3.8        4.8
lambic        4.8        5.6
fruit lambic  6.0        9.0
============= ========== ==========

.. [1] Hubert Hanghofer "Gutes Bier selbst brauen", BLV Buchverlag München,
       2014

"""

from os.path import join, dirname
import pandas as pd
from scipy.interpolate import interp1d

from .constants import DATA_DIR


CARBONATE_FILE = join(dirname(__file__), DATA_DIR, "carbonate.csv")


_df = pd.read_csv(CARBONATE_FILE, sep=",", decimal=".")
_temperature = list(_df.temperature)
_carbonate = list(_df.carbonate)


def saturation(temp: float) -> float:
    """
    Calculate the carbonate saturiation concentration for the
    given temperature.

    :param temp: temperature of the concentrate in °C
    :returns: carbonate saturation concentration in g/l

    """
    f = interp1d(_temperature, _carbonate)
    try:
        return f(temp)
    except ValueError as e:
        raise ValueError(
            "The value for temperature must be in range ({:.1f}..{:.1f}°C)"
            .format(min(_temperature), max(_temperature))
        ) from e


def carbonisation(conc: float, temp: float) -> float:
    """
    Calculate the necessary carbonation to achieve the aimed carbonate
    concentration at the given fermentation temperature.

    :param conc: aimed carbonate concentration in g/l
    :param temp: fermentation temperature in °C
    :returns: necessary carbonation in g/l

    """
    sat = saturation(temp)
    return conc - sat
