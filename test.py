#!/usr/bin/python
# -*- coding: utf-8 -*-.

#import subprocess
#import shlex
from utils.Apyt import apyt

if __name__ == "__main__":
    #cmd1 = shlex.split('/usr/bin/apt-cache search -n -q vima')
    #cmd2 = shlex.split("awk '($1==\"vima\")'")
    #cmd3 = shlex.split('wc -l')
    #p0 = subprocess.Popen(cmd1,stdout=subprocess.PIPE)
    #p1 = subprocess.Popen(cmd2,stdout=subprocess.PIPE ,stdin=p0.stdout,stderr=subprocess.PIPE)
    #p2 = subprocess.check_output(cmd3,stdin=p1.stdout,stderr=subprocess.PIPE)
    #
    #p1.communicate()
    #p0.wait()
    #print p2
    #print p0.wait()

    pack='vimsdf'
    a = apyt()
    uno = a.search_in_repo(pack)
    if uno:
        print pack,' present in repo'
    else:
        print pack,' is not present in repo'
    due = a.check_if_deb_is_installed(pack)
    if due == True:
        print pack,' is installed'
    elif due == 'Half':
        print pack,' has been removed but config files exist'
    else:
        print pack,' is not installed'
