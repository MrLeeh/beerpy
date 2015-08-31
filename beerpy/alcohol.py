"""
Module for calculating the expected alcohol content of a beer.

"""


from .gravity import Gravity


class Alcohol:

    def __init__(self, value):
        self.value = value
        self.unit = "%"

    def __repr__(self):
        return "Alcohol: {:.1f}%".format(self.value)


def alcohol(original_gravity: Gravity, rest_gravity=None) -> Alcohol:
    """
    Calculate the alcohol from a given original gravity and / or rest gravity.

    :param original_gravity: the original gravity of the wort
    :param rest_gravity: the remaining gravity of the wort after fermentation
    :return: alcohol as an object

    """

    if rest_gravity is None:
        return Alcohol(original_gravity.pl * 0.75 / 2)
    else:
        return Alcohol((original_gravity.pl - rest_gravity.pl) / 2)
