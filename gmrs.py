#!/usr/bin/env python
"""
Plot GMRS license applications over time using FCC ULS transactions file
a_gmrs.zip -> HS.dat
"""
import datetime
from pathlib import Path
from pandas import read_csv
from matplotlib.pyplot import gca,show
import seaborn as sns
sns.set_context('talk',font_scale=1.5)

fn = 'data/a_gmrs/HS.dat'
# %%

fn = Path(fn).expanduser()

dat = read_csv(fn, '|',
               names=['App','date','code'],
               usecols=(2,4,5), header=None,
               dtype=str)

dat.dropna(how='any', inplace=True)
dat['date'] = [datetime.date(int(d[6:]), int(d[:2]), int(d[3:5])) for d in dat['date']]

uniq = dat.drop_duplicates(subset='App',keep='last')

uniq['date'].hist(bins=1000)
ax = gca()
ax.set_title('GMRS license grants')
ax.set_xlim((datetime.date(1994,1,1),datetime.date.today()))

show()
