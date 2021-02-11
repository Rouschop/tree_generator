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
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
color = 0


def tree(dir_path: Path, prefix='', is_dir=None):
    global tree_symbols
    global color
    files = list(dir_path.iterdir())  # Iterate over the files and dirs in directory.
    if not is_dir:
        tree_symbols = [tee] * (len(files) - 1) + [last]
    if is_dir:
        color += 1
        if color == 6:
            color = 0
        tree_symbols = [colored(tee, colors[color])] * (len(files) - 1) + [colored(last, colors[color])]
    for tree_symbol, file in zip(tree_symbols, files):
        if not is_dir:
            yield prefix + tree_symbol + file.name
        if is_dir:
            yield prefix + tree_symbol + colored(file.name, 'blue')
        if file.is_dir():  # Also print out the contents of directories with correct symbols
            if tree_symbol == tee:
                symbol = colored(branch, 'red')
            else:  # Without tree looks like: │   │   │   │   └── origin
                symbol = space
            yield from tree(file, prefix=prefix + symbol, is_dir=True)


if path:
    for line in tree(dir_path=pathlib.Path(__file__).parent.absolute() / path):
        print(line)
else:
    for line in tree(dir_path=pathlib.Path(__file__).parent.absolute()):
        print(line)
