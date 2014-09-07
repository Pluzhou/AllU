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
            self.pc = wmi.WMI()

        self.process_cache = {}

    def __get_localtimestamp(self):
        month_dict = {
                        "Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04",
                        "May":"05", "Jun":"06", "Jul":"07", "Aug":"08",
                        "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12",
                    }

        current = time.asctime().split(" ")

        timestamp = "%s%s%s_%s"%(current[-1], month_dict[current[1]],
                                 current[2], current[3].replace(":",""))
        return timestamp

    def __get_process_info_all(self):
        wql = "SELECT Caption, CommandLine, CreationDate, WorkingSetSize\
               FROM Win32_Process"
        return [process for process in self.pc.query(wql)]

    def info(self):
        print self.__get_localtimestamp()
        for process in self.__get_process_info_all():
            print "Caption: ", process.Caption
            print "\tCMD:\t", process.CommandLine
            print "\tDate:\t", process.CreationDate
            print "\tMemory:\t", process.WorkingSetSize

if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ALu = ALuIn()
    ALu.info()
