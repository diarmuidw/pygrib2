from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
# table 4.5
n = 5
url = urlopen("http://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_table4-%s.shtml" % n)
soup = BeautifulSoup(url)
table = soup.find("table")
for row in table.findAll("tr"):
    cols = row.findAll("td")
    if len(cols) == 3:
        if cols[0].find(text=True).find('-') > 0:
            # handle ranges of the for xxx-xxx
            n1 = int(cols[0].find(text=True).split('-')[0])
            n2 = int(cols[0].find(text=True).split('-')[1])
            for number in range(n1,n2+1):
                parameter = cols[1].find(text=True)
                units = ''
                print "%s:('%s','%s')," % (number,parameter,units)
        else:
            number = int(cols[0].find(text=True))
        parameter = cols[1].find(text=True)
        # remove extra whitespace.
        parameter = parameter.rstrip().replace('\n',' ')
        parameter = ' '.join(parameter.split())
        units = cols[2].find(text=True)
        if units is None: 
            units = ''
        else:
            units = units.rstrip().replace('\n',' ')
        if number == 0:
            print "codetable[5]={%s:('%s','%s')," % (number,parameter,units)
        elif number == 255:
            print "%s:('%s','%s')}" % (number,parameter,units)
        else:
            print "%s:('%s','%s')," % (number,parameter,units)
