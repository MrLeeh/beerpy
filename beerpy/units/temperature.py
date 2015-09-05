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

    def __init__(self, value, unit: str=CELSIUS):
        # unit string
        self._unit = unit

        # safe value in celsius
        assert unit in _units, "unit parameter not in {}".format(_units)

        if unit == CELSIUS:
            self._celsius = value
        elif unit == FAHRENHEIT:
            self._celsius = _fahrenheit_to_celsius(value)

    def __repr__(self):
        if self._unit == CELSIUS:
            val = self.celsius
        elif self._unit == FAHRENHEIT:
            val = self.fahrenheit
        return "Temperature: {}{}".format(val, self._unit)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return _celsius_to_fahrenheit(self._celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = _fahrenheit_to_celsius(value)
