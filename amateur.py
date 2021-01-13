#!/usr/bin/env python3
"""
Plot GMRS license applications over time using FCC ULS transactions file
a_gmrs.zip -> HS.dat
"""
from matplotlib.pyplot import show
import fcctrans


def main():
    url = "http://wireless.fcc.gov/uls/data/complete/a_amat.zip"

    fn = fcctrans.get_fcculs(url)
    dat = fcctrans.parse_fcculs(fn)
    fcctrans.plot_fcc_license_apps(dat)

    show()


if __name__ == "__main__":
    main()
