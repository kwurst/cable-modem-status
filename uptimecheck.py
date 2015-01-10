# Copyright (C) 2015 Karl R. Wurst
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA

import urllib.request
from bs4 import BeautifulSoup

class Modem():
    
    def __init__(self, IPaddress):
        self.statusPageSoup = BeautifulSoup(urllib.request.urlopen('http://' + IPaddress + '/cgi-bin/status_cgi'))
        self.statusPageTables = self.statusPageSoup.findAll('table')
        self.eventPageSoup = BeautifulSoup(urllib.request.urlopen('http://' + IPaddress + '/cgi-bin/event_cgi'))
        self.eventPageTables = self.eventPageSoup.findAll('table')
        
    def getUptime(self):
        StatusTable = self.statusPageTables[5]
        uptime = StatusTable.findAll('tr')[0].getText()
        return uptime
    
    def getLastCMeventDate(self):
        CMtable = self.eventPageTables[1]
        CMdate = self.firstCell(self.lastRow(CMtable)).getText()
        return CMdate
    
    def getLastMTAeventDate(self):
        MTAtable = self.eventPageTables[3]
        MTAdate = self.firstCell(self.lastRow(MTAtable)).getText()
        return MTAdate  
    
    def lastRow(self, table):
        return table.findAll('tr')[-1]
    
    def firstCell(self, row):
        return row.findAll('td')[0]
    
def modemStatusCheck():
    modem = Modem('192.168.100.1')
    print(modem.getUptime())
    print(modem.getLastCMeventDate())
    print(modem.getLastMTAeventDate())
    return True

if __name__ == '__main__':
    modemStatusCheck()
