#!/usr/bin/env python3

"""
Plot GMRS license applications over time using FCC ULS transactions file
a_gmrs.zip -> HS.dat
"""

from pathlib import Path

from matplotlib.pyplot import show

import fcctrans


url = "http://wireless.fcc.gov/uls/data/complete/a_amat.zip"
datadir = Path("~/fcc_data")

fn = fcctrans.get_fcculs(url, datadir)
dat = fcctrans.parse_fcculs(fn)
fcctrans.plot_fcc_license_apps(dat)

show()
