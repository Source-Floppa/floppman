# Source Floppa package manager
# written in python
#!/usr/bin/env python

import sys
import os
from os import system

packagesAllowed = "qemu" #place holder until mirrors exist

if sys.argv[0] == "floppman.py":
    
    # make directories
    print(f"MKD /tmp/cache/{sys.argv[1]}")
    system(f"mkdir -p /tmp/cache/{sys.argv[1]}")
    
    #cd into that dir
    print(f"CD /tmp/cache/{sys.argv[1]}")
    system(f"cd /tmp/cache/{sys.argv[1]}")


    # check for packages
    if sys.argv[1] == packagesAllowed:
        print("Downloading source.")
        system(f"wget wget https://download.qemu.org/qemu-2.11.0.tar.xz")
else:
    print("????")
