#!/bin/python3

import os, json, sys

try:
    tree = json.load( open( sys.argv[1], "r") )
except:
    _ = f"Usage: {sys.argv[0]} <config_file>\nGenerate a tree of directories\n"
    print(_ + "Config files should look like this:\n{ 'folder_name': { 'other_folder_in_folder': { } }, { 'some_folder': { } } }")
    exit()

def make_dirs(x, root = "."):
    for k, v in x.items():
        k = f"{root}/{k}"
        os.mkdir( k )
        make_dirs(v, root = k)

try:
    make_dirs( tree )
except FileExistsError:
    pass
