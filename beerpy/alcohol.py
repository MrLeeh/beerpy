"""
Module for calculating the expected alcohol content of a beer.

"""


from .units.gravity import Gravity


class Alcohol:

    def __init__(self, value):
        self.value = value
        self.unit = "%"

    def __repr__(self):
        return "Alcohol: {:.1f}%".format(self.value)


def alcohol(og: Gravity, fg: Gravity=None) -> Alcohol:
    """
    Calculate the alcohol from a given original gravity and / or rest gravity.

    :param og: the original gravity of the wort
    :param fg: the final gravity of the wort after fermentation
    :return: alcohol as an object

    """

    if fg is None:
        return Alcohol(og.pl * 0.75 / 2)
    else:
        return Alcohol((og.pl - fg.pl) / 2)
