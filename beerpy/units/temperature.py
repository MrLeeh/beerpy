"""
Temperature unit

"""


CELSIUS = "°C"
FAHRENHEIT = "°F"
_units = (CELSIUS, FAHRENHEIT)


def _fahrenheit_to_celsius(fahrenheit: float):
    return (fahrenheit - 32.0) / 1.8


def _celsius_to_fahrenheit(celsius: float):
    return celsius * 1.8 + 32.0


class Temperature:

    def __init__(self, value: float, unit: str=CELSIUS):
        # unit string
        self.value = value
        self._unit = unit

        # safe value in celsius
        assert unit in _units, "unit parameter not in {}".format(_units)

    def __repr__(self):
        return "Temperature: {}{}".format(self.value, self.unit)

    @property
    def unit(self):
        return self._unit

    @property
    def celsius(self):
        if self.unit == CELSIUS:
            return self.value
        elif self.unit == FAHRENHEIT:
            return _fahrenheit_to_celsius(self.value)

    @celsius.setter
    def celsius(self, value):
        if self.unit == CELSIUS:
            self.value = value
        elif self.unit == FAHRENHEIT:
            self.value = _celsius_to_fahrenheit(value)

    @property
    def fahrenheit(self):
        if self.unit == CELSIUS:
            return _celsius_to_fahrenheit(self.value)
        elif self.unit == FAHRENHEIT:
            return self.value

    @fahrenheit.setter
    def fahrenheit(self, value):
        if self.unit == CELSIUS:
            self.value = _fahrenheit_to_celsius(value)
        elif self.unit == FAHRENHEIT:
            self.value = value
