# encoding=utf8

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

import sys

def exception():
    print("Usage :")
    print("sync dir1 dir2")
    sys.exit(0)


# UTILITY FUNCTIONS

def copy(filepath1, filepath2):
    with open(filepath1) as f1:
        with open(filepath2, "w") as f2:
            for line in f1:
                f2.write(line)
