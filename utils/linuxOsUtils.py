#!/usr/bin/python
# -*- coding: utf-8 -*-.
from os import getuid,path,listdir
from platform import architecture,linux_distribution
from RunCommand import Command


class LinuxOsUtils():
    '''class that use some linux OS related commands'''
    def __init__(self):
        pass

    def am_i_root(self):
        '''check if user is root or not.
           return false if it is not root,otherwsie return true
        '''
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
        '''check if a file exist
           return true if file exists otherwise return false
        '''
        if path.isfile(obj):
            return True
        else:
            return False

    def list_dir_objects(self,folder):
        '''list objects in a folder
           if an exception is raised a tuple is returned (False,error message),
           otherwise return the objects in the folder
        '''
        try:
            dir_obj = listdir(folder)
        except OSError as err:
            return False,err
        return dir_obj

    def add_repo(self,repofile,repo):
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

    def add_apt_key(self,keyserver,key):
        '''add an APT gpg key from from keyservers'''
        return Command('/usr/bin/apt-key adv --keyserver {} --recv-keys {}'.format(keyserver,key)).run()

    def show_apt_repo(self):
        '''list all repo present on system'''
        def_apt_file = '/etc/apt/sources.list'
        apt_repo_folder = '/etc/apt/sources.list.d/'
        print Command('grep deb {} |grep -v "^#"'.format(def_apt_file)).run(OnlyOutPut=True)
        files = self.list_dir_objects(apt_repo_folder)
        for f in files:
            if '.list' in f:
                print Command('grep deb {} |grep -v "^#"'.format(apt_repo_folder+f)).run(OnlyOutPut=True)


    def search_in_file(self,pattern,file_path):
        '''search for a pattern in a file
           return True if pattern is found otherwise return False.
           If an error occurred  a tuple is returned (False,error message)
        '''
        pattern_exist = Command('grep {} {}'.format(pattern,file_path)).run()
        if pattern_exist[1] == 0:
            return True
        else:
            if pattern_exist[0][1]:
                return False, pattern_exist[0][1]
            else:
                return False

    def search_pattern_in_folder(self,pattern,folder_path):
        '''search for a pattern in a folder
           return True if pattern is found otherwise return False
           If an error occurred  a tuple is returned (False,error message)
        '''
        pattern_exist = Command('grep -r {} {}'.format(pattern,folder_path)).run()
        if pattern_exist[1] == 0:
            return True
        else:
            if pattern_exist[0][1]:
                return False, pattern_exist[0][1]
            else:
                return False
