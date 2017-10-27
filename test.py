#!/usr/bin/python
# -*- coding: utf-8 -*-.


from utils.Apyt import apyt
from utils.linuxOsUtils import LinuxOsUtils
from utils.Generic import generic

if __name__ == "__main__":
    a = generic()
    b = apyt()
    c = LinuxOsUtils()
    c.show_apt_repo()
    #c.list_dir_objects('/etc/apt/sources.list.d/')
