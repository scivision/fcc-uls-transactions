#!/usr/bin/python
"""
Plot GMRS license applications over time using FCC ULS transactions file
a_gmrs.zip -> HS.dat

filenames:
http://wireless.fcc.gov/uls/documentation/pa_intro24.pdf

application codes:
http://wireless.fcc.gov/uls/releases/d992205c.pdf

New license order of transactions:
RECNE     New App Received
RDLCOM    Review completed
FVPCNF    Payment Confirmed
RDLCOM    Review completed
APGRT     App Granted
AUTHPR    Auth Printed


APGRT: Application Granted
AUTHGE: Authorization generated (not used after 1998 ?)
"""
import datetime
from pathlib import Path
from pandas import read_csv
from matplotlib.pyplot import figure,show

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

#uniq.plot('date')

show()