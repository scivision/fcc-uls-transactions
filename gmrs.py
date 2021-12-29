#!/usr/bin/env python3

"""
Plot GMRS license applications over time using FCC ULS transactions file
a_gmrs.zip -> HS.dat
"""

import argparse
from pathlib import Path

from matplotlib.pyplot import show

import fcctrans


p = argparse.ArgumentParser()
p.add_argument("datadir", help="path to store data in", default="data")
P = p.parse_args()

datadir = Path(P.datadir).expanduser()

url = "https://wireless.fcc.gov/uls/data/complete/a_gmrs.zip"

fn = fcctrans.get_fcculs(url, datadir)
dat = fcctrans.parse_fcculs(fn)
fcctrans.plot_fcc_license_apps(dat)

show()
