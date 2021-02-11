# tree_generator
Generate a tree to view the directory and file structure.

Installation requirements:

```pip3 install -r requirements.txt```


Example usage:

```python3 main.py```

```python3 main.py -p files```

```python3 main.py -p /home/user/Desktop```


```
usage: main.py [-h] [-p]

List directory tree

optional arguments:
  -h, --help    show this help message and exit
  -p , --path   Specify relative path
```

Example output:

```
└── a3
    ├── old1
    ├── old2
    ├── old3
    ├── old4
    ├── old5
    └── new_dir
        ├── file1
        ├── file2
        ├── file3

```

Python version used is python3.9
