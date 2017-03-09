import sys
import os
try: from setuptools import setup
except ImportError: from distutils.core import setup
import versioneer

URL = 'https://github.com/kadrlica/toolbelt'

setup(
    name='toolbelt',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url=URL,
    author='Alex Drlica-Wagner',
    author_email='kadrlica@fnal.gov',
    scripts = [],
    install_requires=[],
    packages=['toolbelt'],
    description="A place to hold python tools.",
    long_description=read('README.md'),
    platforms='any',
    keywords='python tools',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
    ]
)
