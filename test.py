#!/usr/bin/python
# -*- coding: utf-8 -*-.


from utils.Apyt import apyt
from utils.linuxOsUtils import LinuxOsUtils
from utils.Generic import generic

if __name__ == "__main__":
    a = generic()
    b = apyt()
    c = LinuxOsUtils()
    #a.reply_YN('asdsdsad')
    #print a.file_read('LICENSES')
    print a.file_write_append('LICENSES','asdasd')
    print a.file_write_new('LICENSES','asdasd')
    #c.show_apt_repo()
    #c.list_dir_objects('/etc/apt/sources.list.d/')
