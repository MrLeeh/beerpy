"""
Concentration unit

"""

GRAMS_PER_LITER = "g/l"
_units = (GRAMS_PER_LITER)


class Concentration:

    def __init__(self, value: float):
        self.value = value
        self._unit = GRAMS_PER_LITER

    def __repr__(self):
        return "Concentration: {}{}".format(self.value, self.unit)

    @property
    def unit(self):
        return self._unit
