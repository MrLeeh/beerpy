beerpy package
==============

* **Copyright (c):** 2015 Stefan Lehmann
* **license:** MIT license
* **description:** The beerpy package contains a collection of brewing calculation functions 
to make the brewers life a little bit easier. This collection is intended to grow
in complexety and hopefully in usefulness by time.

Features
--------

### Calculate alcohol from original wort and rest wort

Make a rough calculation given only the original gravity of the wort:

```python
>>> from beerpy.alcohol import alcohol
>>> from beerpy.gravity import Gravity, PL
>>> alcohol(Gravity(12, unit=PL))  # given a gravity of 12 °Pl
Alcohol: 4.5%

```

Make a more exact calculation by measuring the original and final gravity of the
wort:

```python
>>> from beerpy.alcohol import alcohol
>>> from beerpy.gravity import Gravity, PL
>>> alcohol(Gravity(12, unit=PL), Gravity(6, PL))
Alcohol: 3%

```

### Calculate the malt composition for a specific receipe

A receipe should result in 20l of wort with a specific gravity of 18.
The composition should contain 80% of Pilsener malt and 20% of Munich
malt.

```python
>>> malt_composition(20, 20, [(PILSENER_MALT, 0.8), (MUNICH_MALT, 0.2)])
(6.93, [('Pilsener Malz', 5.54), ('Münchener Malz', 1.39)])

```

As result an amount of 6.93kg of malt is needed.
5.54kg of Pilsener malt and 1.39kg of Munich malt.
