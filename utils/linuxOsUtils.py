#!/usr/bin/python
# -*- coding: utf-8 -*-.
from os import getuid,path,listdir
from platform import architecture,linux_distribution


class LinuxOsUtils():
    '''class that use some linux OS related commands'''
    def __init__(self):
        pass

    def who_am_i(self):
        '''check if user is root or not'''
        if getuid() != 0:
            return False
        else:
            return True

    def get_linux_distro(self):
        '''get Linux distribution code'''
        return linux_distribution()

    def get_linux_arch(self):
        '''get Linux os architecture'''
        return architecture()

    def file_exists(self,obj):
        '''check if a file exist'''
        if path.isfile(obj):
            return True
        else:
            return False

    def list_dir_objects(self,folder):
        '''list objects in a folder'''
        try:
            dir_obj = listdir(folder)
        except OSError as err:
            print err
            return False
        return dir_obj

    def add_repo(repofile,repo):
        '''add a linux APT reportsitory'''
        if self.file_exists(repofile):
            try:
                with open(repofile, 'r') as configfile:
                    if repo in configfile.read():
                        print "repository already present"
                    else:
                        try:
                            with open(repofile, 'ab') as configfile:
                                configfile.write(repo)
                        except IOError as error:
                            print error
            except IOError as error:
                print error
        else:
            try:
                with open(repofile, 'w') as configfile:
                    configfile.write(repo)
            except IOError as error:
                print error

    def add_apt_key(keyserver,key):
        '''add an APT gpg key from from keyservers'''
        return Command('/usr/bin/apt-key adv --keyserver {} --recv-keys {}'.format(keyserver,key)).run()
