from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
def print_table(table,ndiscip,n):
    nrow = 0
    for row in table.findAll("tr"):
        cols = row.findAll("td")
        if len(cols) == 4:
            if cols[0].find(text=True).find('-') > 0:
                # handle ranges of the for xxx-xxx
                n1 = int(cols[0].find(text=True).split('-')[0])
                n2 = int(cols[0].find(text=True).split('-')[1])
                for number in range(n1,n2+1):
                    parameter = cols[1].find(text=True)
                    parameter = parameter.rstrip().replace('\n',' ')
                    units = ''
                    abbrev = ''
                    print "%s:('%s','%s','%s')," % (number,parameter,units,abbrev)
            else:
                number = int(cols[0].find(text=True))
            parameter = cols[1].find(text=True)
            # remove extra whitespace.
            parameter = parameter.rstrip().replace('\n',' ')
            parameter = ' '.join(parameter.split())
            parameter = parameter.replace('&#937;','w')
            units = cols[2].find(text=True)
            if units is None: 
                units = ''
            else:
                units = units.rstrip().replace('\n',' ')
            abbrev = cols[3].find(text=True)
            if abbrev is None:
                abbrev = ''
            else:
                abbrev = abbrev.rstrip().replace(' ','_')
            if nrow == 0:
                if n == 0 and ndiscip == 0:
                    print "codetable[2]={0:{%s:{%s:('%s','%s','%s')," % (n,number,parameter,units,abbrev)
                else:
                    print "codetable[2][%s][%s]={%s:('%s','%s','%s')," % (ndiscip,n,number,parameter,units,abbrev)
            elif number == 255:
                if n == 0:
                    print "%s:('%s','%s','%s')}," % (number,parameter,units,abbrev)
                else:
                    print "%s:('%s','%s','%s')}" % (number,parameter,units,abbrev)
            else:
                print "%s:('%s','%s','%s')," % (number,parameter,units,abbrev)
            nrow = nrow + 1
# table 4.2-0-n
for n in [0,1,2,3,4,5,6,7,13,14,15,16,17,18,19,190,191,192]:
    url = urlopen("http://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_table4-2-0-%s.shtml" % n)
    soup = BeautifulSoup(url)
    print_table(soup.find("table"),0,n)
    if not n:
        print "1:{},2:{},3:{},4:{},5:{},6:{},7:{},13:{},14:{},15:{},18:{},19:{},190:{},191:{},192:{}},1:{},2:{},3:{},10:{}}"
# table 4.2-1-n
for n in [0,1]:
    url = urlopen("http://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_table4-2-1-%s.shtml" % n)
    soup = BeautifulSoup(url)
    print_table(soup.find("table"),1,n)
# table 4.2-2-n
for n in [0,3]:
    url = urlopen("http://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_table4-2-2-%s.shtml" % n)
    soup = BeautifulSoup(url)
    print_table(soup.find("table"),2,n)
# table 4.2-3-n
for n in [0,1,192]:
    url = urlopen("http://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_table4-2-3-%s.shtml" % n)
    soup = BeautifulSoup(url)
    print_table(soup.find("table"),3,n)
# table 4.2-10-n
for n in [0,1,2,3,4,191]:
    url = urlopen("http://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_table4-2-10-%s.shtml" % n)
    soup = BeautifulSoup(url)
    print_table(soup.find("table"),10,n)
