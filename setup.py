from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


version = '0.2'


setup(
    name='fwrite',
    version=version,
    description='Create files of the desired size',
    long_description=long_description,
    author='Pedro Buteri Gonring',
    author_email='pedro@bigode.net',
    url='https://github.com/pdrb/fwrite',
    license='MIT',
    classifiers=[],
    keywords='create file write filewrite fwrite',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    entry_points={
        'console_scripts': ['fwrite=fwrite.fwrite:cli'],
    },
)
