#!/usr/bin/python
# -*- coding: utf-8 -*-.


from utils.Apyt import apyt
from utils.linuxOsUtils import LinuxOsUtils

if __name__ == "__main__":
    a = apyt()
    a.check_deb_dependencies('/home/luke/Downloads/google-chrome-stable_current_amd64.deb')
    #print a.check_if_deb_is_installed('google-chrome-stable',check_version=True)
