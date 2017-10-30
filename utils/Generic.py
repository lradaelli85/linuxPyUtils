#!/usr/bin/python
# -*- coding: utf-8 -*-.
from utils.linuxOsUtils import LinuxOsUtils

class generic():
    '''class for generic pytnon functions'''
    def __init__(self):
        pass

    def reply_YN(self,message):
        '''Wrapper to check that y or n is replied'''
        reply = None
        while True:
            reply = raw_input('{} [y/n]: '.format(message)).lower().strip()
            if reply == 'y' or reply == 'n':
                break
        return reply

    def file_read(self,file_obj):
        '''Read a file'''
        try:
            with open(file_obj, 'r') as my_file:
                return my_file.read()
        except IOError as error:
            return error

    def file_write_append(self,file_obj,str_to_append):
        '''Append string to a file.If file does not exists,create it'''
        try:
            with open(file_obj, 'ab') as my_file:
                my_file.write(str_to_append)
        except IOError as error:
            return error

    def file_write_new(self,file_obj,str_to_add):
        '''Write a string to a file.If file exists overwrite it'''
        try:
            with open(file_obj, 'w') as my_file:
                my_file.write(str_to_add)
        except IOError as error:
            return error
