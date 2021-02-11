#!/usr/bin/env python3

from pathlib import Path
import pathlib
import argparse
from termcolor import colored

parser = argparse.ArgumentParser(description='List directory tree')
parser.add_argument('-p', '--path', help='Specify relative path', metavar='', required=False, type=str, dest='path')

args = parser.parse_args()
path = args.path

# Tree components
space = '    '
branch = '│   '
tee = '├── '
last = '└── '


def tree(path: Path, prefix='', is_dir=None):
    files = list(path.iterdir())  # Iterate over the files and dirs in directory.
    if not is_dir:
        tree_symbols = [tee] * (len(files) - 1) + [last]
    if is_dir:
        tree_symbols = [colored(tee, 'red')] * (len(files) - 1) + [colored(last, 'red')]
    for tree_symbol, file in zip(tree_symbols, files):
        # print(tree_symbol, file)
        yield prefix + tree_symbol + colored(file.name, 'blue')
        if file.is_dir():  # Also print out the contents of directories with correct symbols
            if tree_symbol == tee:
                symbol = colored(branch, 'red')
                tree_symbol = colored(tree_symbol, 'red')
            else:  # Without tree looks like: │   │   │   │   └── origin
                symbol = space
            yield from tree(file, prefix=prefix + symbol, is_dir=True)







if path:
    for line in tree(path=pathlib.Path(__file__).parent.absolute() / path):
        print(line)
else:
    for line in tree(path=pathlib.Path(__file__).parent.absolute()):
        print(line)
