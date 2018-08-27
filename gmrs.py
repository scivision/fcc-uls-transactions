#!/usr/bin/env python
"""
Plot GMRS license applications over time using FCC ULS transactions file
a_gmrs.zip -> HS.dat
"""
from matplotlib.pyplot import show
try:
    import seaborn as sns
    sns.set_context('talk', font_scale=1.)
except ImportError:
    pass

import fcctrans


def main():
    url = 'https://wireless.fcc.gov/uls/data/complete/a_gmrs.zip'

    fn = fcctrans.get_fcculs(url)
    dat = fcctrans.parse_fcculs(fn)
    fcctrans.plot_fcc_license_apps(dat)

    show()


if __name__ == '__main__':
    main()
