# -*- coding:utf-8 -*-
#
# AllUProcess provided the method to capture all process's memory, CPULoad
# and CreationDate. 
# 
# Editor: tangys
# Last Modified time: 2014/09/07 0:56

__author__  = 'tangys'
__version__ = '0.1'

import wmi
import time

class ALuIn(object):
    """docstring for ALuIn
    ALuIn Class get process's info and return data.
    """
    def __init__(self, pcname=None, usr=None, pwd=None):
        print "Hello AllU!"
        
        if pcname:
            self.pc = wmi.WMI(pcname, user=usr, password=pwd)
        else:
            self.pc = wmi.WMI() # Monitor Local PC

    def __get_Caption(self, instance):
        """get Win32_Process Caption"""
        return instance.Caption

    def __get_CommandLine(self, instance):
        """get Win32_Process CommandLine"""
        return instance.CommandLine

    def __get_CreationDate(self, instance):
        """get Win32_Process CreationDate"""
        return instance.CreationDate

    def __get_WorkingSetSize(self, instance):
        """get Win32_Process WorkingSetSize"""
        return instance.WorkingSetSize

if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ALu = ALuIn()
