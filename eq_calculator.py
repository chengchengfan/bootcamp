import pytest
import numpy as np

def eq_conc(Kd, ca0, cb0):
    """To calculated equilibrium conventrations."""

    # Define the variables

    cab = 0.5 * (ca0 + cb0 + Kd - np.sqrt((ca0 + cb0 + Kd) **2 - 4 * ca0 * cb0))
    ca = ca0 - cab
    cb = cb0 - cab

    Kd_calc = ca * cb / cab
    ca0_calc = ca + cab
    cb0_calc = cb + cab

    #  return cab, ca, cb, Kd_calc, ca0_calc, cb0_calc

    # np.isclose([Kd, ca0, cb0], [Kd_calc, ca0_calc, cb0_calc])
