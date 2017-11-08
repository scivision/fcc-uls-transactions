#!/usr/bin/env python
req = ['nose','setuptools','pandas','matplotlib','seaborn']
# %%
import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception:
    pip.main(['install'] + req)
# %%
from setuptools import setup

setup(name='fcctrans',
      packages=['fcctrans'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/fcc-uls-transactions',
      version='0.9.0',
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 3',
      ],
      install_requires = req,
      description='Plot FCC ULS license grants vs. time',
	  )
