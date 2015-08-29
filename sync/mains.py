# encoding=utf8

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

from .utils import *
import os
import sys
import hashlib
import time, datetime

# MAIN

def main():

    if len(sys.argv) < 3:
        exception()
        return
    
    path1 = sys.argv[1]
    path2 = sys.argv[2]

    if path1.endswith('/'):
            path1 = path1[:-1]
    if path2.endswith('/'):
            path2 = path2[:-1]

    for filename in os.listdir(path1):
            
        filepath1 = path1 + '/' + filename
        filepath2 = path2 + '/' + filename
        
        sha = hashlib.sha1()
        with open(filepath1, 'rb') as f:
            for line in f:
                sha.update(line)
        sha1 = sha.hexdigest()
        
        sha = hashlib.sha1()
        with open(filepath2, 'rb') as f:
            for line in f:
                sha.update(line)
        sha2 = sha.hexdigest()

        t1 = int(os.stat(filepath1).st_mtime)
        t2 = int(os.stat(filepath2).st_mtime)

        if sha1 != sha2 :
            if t1 > t2 :
                copy(filepath1, filepath2)
            else :
                copy(filepath2, filepath1)

if __name__ == '__main__':
    main()
