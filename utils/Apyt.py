#!/usr/bin/python
# -*- coding: utf-8 -*-.
from utils.RunCommand import Command
from utils.linuxOsUtils import LinuxOsUtils
import sys


class apyt():
    '''wrapper to handle various linux commands'''
    def __init__(self):
        pass

    def search_in_repo(self,package):
        '''Search for the exact package match in repo (Debian based distro)
           return False if is not in repo,or True if it is.
        '''
        is_in_repo = Command("/usr/bin/apt-cache search -n -q {} |awk '($1==\"{}\")'|wc -l".format(package,package)).run(OnlyOutPut=True)
        if int(is_in_repo) == 0:
            return False
        else:
            return True

    def check_if_deb_is_installed(self,package):
        '''Search if a package is installed (Debian based distro)
           return True if it is installed,False if it is not installed and Half
           if it has been removed but configuration file exist
        '''
        is_installed = Command("/usr/bin/dpkg-query -W -f='${Status}' %s" %package).run(OnlyOutPut=True)
        if "install ok installed" in is_installed:
            return True
        elif "deinstall ok config-files" in is_installed:
            return 'Half'
        else:
            return False

    def inst_from_repo(self,package):
        '''Install a package from Linux repo (Debian based distro)'''
        if LinuxOsUtils().who_am_i():
            return Command('/usr/bin/apt-get install --no-install-recommends {}'.format(package)).run()

    def inst_a_deb(self,package):
        '''Install a deb package'''
        if LinuxOsUtils().who_am_i():
            if LinuxOsUtils().file_exists(package):
                cmd = Command('dpkg -i {}'.format(package)).run()
                if cmd != 0:
                    print "forcing dependencies installation"
                    Command('/usr/bin/apt-get --no-install-recommends -f install').run()

    def inst_debs_from_folder(self,folder):
        '''Install debs present in a folder'''
        if LinuxOsUtils().who_am_i():
            if LinuxOsUtils().list_dir_objects(folder):
                debs = LinuxOsUtils().list_dir_objects(folder)
                if debs:
                    for deb in debs:
                        if str(deb).endswith('.deb'):
                            inst_a_deb(package)
                else:
                    print 'empty folder'
