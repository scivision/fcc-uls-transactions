#!/usr/bin/env python
install_requires = ['pandas','numpy','scipy']
tests_require = ['nose','coveralls']

from setuptools import setup,find_packages

setup(name='fcctrans',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/fcc-uls-transactions',
      version='0.9.0',
      classifiers=[
      'Development Status :: 4 - Beta',
      'Programming Language :: Python',
      ],
      install_requires = install_requires,
      extras_require = {'tests':tests_require,'plot':['matplotlib','seaborn']},
      tests_require = tests_require,
      python_requires='>=3.6',
      description='Plot FCC ULS license grants vs. time',
      long_description = open('README.rst').read()
	  )
