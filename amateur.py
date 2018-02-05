#!/usr/bin/env python
"""
Plot GMRS license applications over time using FCC ULS transactions file
a_gmrs.zip -> HS.dat
"""
from matplotlib.pyplot import show
import seaborn as sns
sns.set_context('talk', font_scale=1.)
#
import fcctrans


if __name__ == '__main__':
    url = 'http://wireless.fcc.gov/uls/data/complete/a_amat.zip'

    fn = fcctrans.get_fcculs(url)
    dat = fcctrans.parse_fcculs(fn)
    fcctrans.plot_fcc_license_apps(dat)

    show()
