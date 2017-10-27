#!/usr/bin/python
# -*- coding: utf-8 -*-.

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
