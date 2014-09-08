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
    def __init__(self, pcname=None, usr=None, pwd=None, keyword=None):
        print "Hello AllU!"
             
        if pcname:
            self.pc = wmi.WMI(pcname, user=usr, password=pwd)
        else:
            self.pc = wmi.WMI()

        self.process_cache = {}
        self.keyword = keyword
        self.cur = self.__get_localtimestamp()
        self.indx = 1

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
        wql = "SELECT Caption, CommandLine, CreationDate,            \
                      WorkingSetSize, VirtualSize, PeakWorkingSetSize\
               FROM Win32_Process"
        if self.keyword == None:
            return [process for process in self.pc.query(wql)]
        else:
            return [process for process in self.pc.query(wql)   \
                     if self.keyword in str(process.CommandLine)\
                     or self.keyword in str(process.Caption)]

    def __process_info_to_dict(self):
        self.cur = self.__get_localtimestamp()
        for p in self.__get_process_info_all():
            pinfo = (p.Caption, p.CommandLine, p.CreationDate)
            if self.process_cache.has_key(pinfo):
                idx = self.process_cache[pinfo]["idx"]
            else:
                idx = self.indx
                self.indx += 1
            self.process_cache[pinfo] = {
                self.cur: (p.WorkingSetSize, 
                           p.VirtualSize, 
                           p.PeakWorkingSetSize),
                "idx": idx
                }

        return self.process_cache

    def get_current_status(self):
        return self.__process_info_to_dict()

    def stdout_current_status(self):
        info = self.__process_info_to_dict()
        for caption, cmd, date in info.keys():
            key = (caption, cmd, date)
            print "Caption:\t", caption
            print "\tCMD:\t", cmd
            print "\tDate:\t", date
            print "MemoryUsing:"
            print "\tWorkingSetSize:\t", info[key][self.cur][0]
            print "\tVirtualSize:\t", info[key][self.cur][1]
            print "\tVirtualSize:\t", info[key][self.cur][2]
            print "\tProcess Idx:\t", info[key]["idx"]

    def fileout_current_status(self, path):
        with open(path, "w") as f:
            pass

if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ALu = ALuIn()
    print ALu.stdout_current_status()
