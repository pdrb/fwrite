fwrite
=======

Create files of the desired size.

Install
-------

Install using pip:

::

    pip install fwrite

or

Download and set executable permission on the script file:

::

    chmod +x fwrite.py

or

Download and run using the python interpreter:

::

    python fwrite.py

Usage
-----

::

    Usage: fwrite filename size [options]

    create files of the desired size, e.g., 'fwrite test 10M'

    Options:
    --version       show program's version number and exit
    -h, --help      show this help message and exit
    -r, --random    use random data (very slow)
    -n, --newlines  append new line every 1023 bytes

Examples
--------

Create file "test" with 100KB:

::

    $ fwrite test 100K

Create "test" with 1GB:

::

    $ fwrite test 1G

Create "test" with 10MB of random data with lines:

::

    $ fwrite test 10M -r -n

Notes
-----

- Works on Python 2
- Tested on Linux and Windows
