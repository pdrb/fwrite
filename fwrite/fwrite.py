#!/usr/bin/python

# fwrite 0.1
# author: Pedro Buteri Gonring
# email: pedro@bigode.net
# date: 07/02/2017

import random
import string
import optparse
import sys


version = '0.1'


# Parse and validate arguments
def get_parsed_args():
    usage = 'usage: %prog filename size [options]'
    # Create the parser
    parser = optparse.OptionParser(
        description='create files of the desired size',
        usage=usage, version=version
    )
    parser.add_option('-u', dest='unit', type='choice', default='kb',
                      choices=['kb', 'mb', 'gb'],
                      help='unit of measurement: kb, mb or gb \
                      (default: %default)')
    parser.add_option('-r', '--random', action='store_true', default=False,
                      help='use random data (very slow)')
    parser.add_option('-n', '--newlines', action='store_true', default=False,
                      help='append new line every 1023 bytes')

    # Print help if no argument is given
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(2)

    # Parse the args
    (options, args) = parser.parse_args()

    # Some args validation
    if len(args) != 2:
        parser.error('filename or size not informed')
    try:
        size = int(args[1])
    except ValueError:
        parser.error('size must be an int')
    if size <= 0:
        parser.error('size must be a positive number')
    args[1] = size
    return (options, args)


# Main CLI
def cli():
    (options, args) = get_parsed_args()

    filename = args[0]
    size = args[1]
    linesize = 1024

    if options.unit == 'mb':
        size = size * 1024
    elif options.unit == 'gb':
        size = size * 1024 * 1024

    if options.newlines:
        line = '0' * (linesize - 1) + '\n'
    else:
        line = '0' * linesize

    newfile = open(filename, 'wb')

    for _ in range(size):
        if options.random and options.newlines:
            line = ''.join(random.choice(string.ascii_letters)
                           for _ in range(linesize - 1)) + '\n'
        elif options.random:
            line = ''.join(random.choice(string.ascii_letters)
                           for _ in range(linesize))
        newfile.write(line)
        newfile.flush()

    newfile.close()


# Run cli function if invoked from shell
if __name__ == '__main__':
    cli()
