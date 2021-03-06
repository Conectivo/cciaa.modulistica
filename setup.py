# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '2.0.3.dev0'

tests_require=['zope.testing', 'Products.PloneTestCase']

setup(name='cciaa.modulistica',
      version=version,
      description="An additional view for Plone folders, for better manage repository of files",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.0',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Communications :: File Sharing',
        'Topic :: Documentation',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='plone plonegov additional view folders form file',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.net',
      url='http://plone.org/products/cciaa.modulistica',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cciaa', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'Products.CMFPlone',
                        'archetypes.schemaextender'
                        ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
