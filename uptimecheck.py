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
import smtplib
from email.mime.text import MIMEText

def uptimecheck():
    getStatusPageFromModem()
    getEventPageFromModem()
    return True

def getStatusPageFromModem():
    status_page = urllib.request.urlopen('http://192.168.100.1/cgi-bin/status_cgi')
    soup = BeautifulSoup(status_page)
    tables = soup.findAll('table')
    StatusTable = tables[5]
    uptime = StatusTable.findAll('tr')[0].getText()
    print(uptime)

def getEventPageFromModem():
    event_page = urllib.request.urlopen('http://192.168.100.1/cgi-bin/event_cgi')
    soup = BeautifulSoup(event_page.read())
    tables = soup.findAll('table')
    CMtable = tables[1]
    MTAtable = tables[3]
    CMdate = CMtable.findAll('tr')[-1].findAll('td')[0].getText()
    print('Date of last CM event', CMdate)

    MTAdate = MTAtable.findAll('tr')[-1].findAll('td')[0].getText()
    print('Date of last MTA event', MTAdate)    

if __name__ == '__main__':
    uptimecheck()
