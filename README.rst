fwrite
=======

Python script to create files of the desired size.

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

    create files of the desired size

    Options:
    --version       show program's version number and exit
    -h, --help      show this help message and exit
    -u UNIT         unit of measurement: kb, mb or gb
                    (default: kb)
    -r, --random    use random data (very slow)
    -n, --newlines  append new line every 1023 bytes

Examples
--------

Create file "test" with 100KB:

::

    $ fwrite test 100

Create "test" with 1GB:

::

    $ fwrite test 1 -u gb

Create "test" with 10MB of random data with lines:

::

    $ fwrite test 10 -u mb -r -n

Notes
-----

- Works on Python 2
- Tested on Linux and Windows
