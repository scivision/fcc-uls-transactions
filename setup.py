#!/usr/bin/env python
req = ['nose','pandas',]

from setuptools import setup,find_packages

setup(name='fcctrans',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/fcc-uls-transactions',
      version='0.9.0',
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 3',
      ],
      install_requires = req,
      python_requires='>=3.6',
      extras_require={'plot':['matplotlib','seaborn']},
      description='Plot FCC ULS license grants vs. time',
	  )
