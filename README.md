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
    └── new_dir
        ├── file1
        ├── file2
        ├── file3
        ├── file4
        ├── file5
        ├── file6
        └── other
            ├── file1
            ├── file2
            └── file3
```

Python version used is python3.9
