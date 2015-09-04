"""
Routines for calculating receipes. Source:
http://www.mathe-fuer-hobbybrauer.de/bierrezepte/index.html

"""

import os
from collections import namedtuple

import pandas as pd
from scipy.interpolate import interp2d

from .units.gravity import Gravity
from .utilities import datadir


# datafile for hop saturation
_f_hop_saturation = os.path.join(datadir(), "hop_saturation.csv")

# Definition of namedtuple Malt
Malt = namedtuple("Malt", ('name', 'extract_ratio'))


# Different Malts
PILSENER_MALT = Malt("Pilsener Malz", 800)
WIENER_MALT = Malt("Wiener Malz", 800)
MUNICH_MALT = Malt("Münchener Malz", 790)
CARAMALT = Malt("Caramalz", 720)
CARAMALT_DARK = Malt("Caramalz dunkel", 720)
WHEAT_MALT = Malt("Weizenmalz", 800)
ROAST_MALT = Malt("Röstmalz", 700)
CORN = Malt("Mais", 800)
RICE = Malt("Reis", 800)
CEREAL_FLAKES = Malt("Getreideflocke", 650)
SUGAR = Malt("Zucker", 1000)
EXTRACT_DRY = Malt("Malzextrakt trocken", 990)
EXTRACT_FLUID = Malt("Malzextrakt flüssig", 800)
HONEY = Malt("Honig", 680)


def _round(x):
    return round(x, 2)


def _hop_saturation(cooktime, pl):
    df = pd.read_csv(_f_hop_saturation, sep=',', decimal='.', index_col=0)
    x = [float(s.replace(',', '.')) for s in list(df.columns)]
    y = list(df.index)
    z = list([list(l) for l in df.to_records(index=False)])
    f = interp2d(x, y, z)
    return f(pl, cooktime)


def malt_composition(volume: float, gravity: Gravity,
                     composition: '[(Malt, float),...]', efficiency=0.75):
    """
    Calculate the amount of malt needed to achieve a wort with the given
    `volume` and gravity (°Pl).

    :param volume: volume of the wort in liters
    :param gravity: gravity of the wort
    :param composition: malt composition as a list of
        tuples. Each tuple contains the `Malt` and the share of the specific
        malt sort on the overall malt. The sum of all composition parts should
        result in one.
    :return: overall malt weight in kg, weight of each malt sort in kg


    :Example:

        A receipe should result in 20l of wort with a specific gravity of 18.
        The composition should contain 80% of Pilsener malt and 20% of Munich
        malt.

        >>> malt_composition(22, Gravity(14), [(PILSENER_MALT, 0.8), (MUNICH_MALT, 0.2)])
        (5.44, [('Pilsener Malz', 4.35), ('Münchener Malz', 1.09)])

        As result an amount of 6.93kg of malt is needed.
        5.54kg of Pilsener malt and 1.39kg of Munich malt.

    """

    def specific_extract_ratio():
        for malt, ratio in composition:
            yield ratio * malt.extract_ratio

    wort_weight = float(volume) * gravity.sg
    theoretical_extract = wort_weight * gravity.pl * 10.0
    practical_extract = sum(specific_extract_ratio()) * efficiency
    total_weight = theoretical_extract / practical_extract

    return _round(total_weight), [(malt.name, _round(ratio * total_weight))
                                  for malt, ratio in composition]


def hop_quantity(ibu, alpha, wort_volume, cooktime, gravity: Gravity):
    """
    Calculate the amount of hop with a specific `alpha` needed to achieve a
    given bitterness in `ibu`.

    :param ibu: bitterness level in IBU
    :param alpha: amount of alpha acid in %
    :param wort_volume: quantity of wort in liters
    :param cooktime: cooking time in minutes
    :param gravity: gravity of the wort
    :return: amount of hops in grams

    """
    saturation = _hop_saturation(cooktime, gravity.pl)[0]
    return ibu * wort_volume * 10 / (alpha * saturation)
