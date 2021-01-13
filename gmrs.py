#!/usr/bin/env python
"""
Plot GMRS license applications over time using FCC ULS transactions file
a_gmrs.zip -> HS.dat
"""

from pathlib import Path
from matplotlib.pyplot import show
import argparse
import fcctrans


def main():
    p = argparse.ArgumentParser()
    p.add_argument("datadir", help="path to store data in", default="data")
    P = p.parse_args()

    datadir = Path(P.datadir).expanduser()

    url = "https://wireless.fcc.gov/uls/data/complete/a_gmrs.zip"

    fn = fcctrans.get_fcculs(url, datadir)
    dat = fcctrans.parse_fcculs(fn)
    fcctrans.plot_fcc_license_apps(dat)

    show()


if __name__ == "__main__":
    main()
