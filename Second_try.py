from pathlib import Path
import argparse

# Tree components
space = '    '
branch = '│   '
tee = '├── '
last = '└── '


def tree(dir=Path, prefix=''):
    files = list(dir.iterdir())  # Iterate over the files in this directory.
    tree_symbols = [tee] * (len(files) - 1) + [last]
    for tree_symbol, file in zip(tree_symbols, files):
        print(tree_symbol, file)



tree(dir=Path.home() / 'projects/tree_generator/files')