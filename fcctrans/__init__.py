import urllib.request
from pathlib import Path
import zipfile
import pandas
from datetime import datetime, date
from matplotlib.pyplot import gca


def get_fcculs(url: str, datadir: Path = 'data') -> Path:
    """download FCC GMRS license data if necessary"""

    datadir = Path(datadir).expanduser()

    zipfn = datadir/url.split('/')[-1]
    opath = datadir/zipfn.stem
    fn = opath/'HS.dat'

    if not fn.is_file():
        try:
            zipfile.ZipFile(zipfn)
        except (FileNotFoundError, zipfile.BadZipfile):
            print('downloading, may take several minutes: ', url)
            urllib.request.urlretrieve(url, zipfn)

        with zipfile.ZipFile(zipfn) as z:
            z.extract('HS.dat', opath)

    return fn


def parse_fcculs(fn: Path) -> pandas.DataFrame:
    dat = pandas.read_csv(fn, '|',
                          names=['App', 'date', 'code'],
                          usecols=(2, 4, 5), header=None,
                          dtype=str)

    dat.dropna(how='any', inplace=True)
    dat['date'] = [date(int(d[6:]), int(d[:2]), int(d[3:5])) for d in dat['date']]

    uniq = dat.drop_duplicates(subset='App', keep='last')

    return uniq


def plot_fcc_license_apps(dat: pandas.DataFrame, begin: datetime = None,
                          end: datetime = date.today()):
    """plot license data"""

    dat['date'].hist(bins=1000)
    ax = gca()
    ax.set_title('license grants')
    ax.set_xlim(begin, end)
