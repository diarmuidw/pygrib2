from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
def removewhite(x):
    try:
        x = x.rstrip().replace('\n',' ')
        x = ' '.join(x.split())
        x = x.replace('&#937;','w')
    except:
        pass
    return x
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
                    parameter = removewhite(parameter)
                    units = ''
                    abbrev = ''
                    print """%s:("%s","%s","%s"),""" % (number,parameter,units,abbrev)
            else:
                number = int(cols[0].find(text=True))
            parameter = cols[1].find(text=True)
            # remove extra whitespace.
            parameter = removewhite(parameter)
            units = cols[2]
            if units is None:
                units = ""
            else:
            # convert <sup> to ^, remove </sup>.
                if units.find('sup') is not None:
                    units = (str(units).replace("<sup>","^")).replace("</sup>","")
                    units = BeautifulSoup(units)
                units = units.find(text=True)
                # remove extra whitespace.
                units = removewhite(units)
            abbrev = cols[3].find(text=True)
            if abbrev is None:
                abbrev = ''
            else:
                abbrev = removewhite(abbrev.rstrip().replace(' ','_'))
            if nrow == 0:
                if n == 0 and ndiscip == 0:
                    print """codetable[2]={0:{%s:{%s:("%s","%s","%s"),""" % (n,number,parameter,units,abbrev)
                else:
                    print """codetable[2][%s][%s]={%s:("%s","%s","%s"),""" % (ndiscip,n,number,parameter,units,abbrev)
            elif number == 255:
                if n == 0:
                    print """%s:("%s","%s","%s")},""" % (number,parameter,units,abbrev)
                else:
                    print """%s:("%s","%s","%s")}""" % (number,parameter,units,abbrev)
            else:
                print """%s:("%s","%s","%s"),""" % (number,parameter,units,abbrev)
            nrow = nrow + 1

m = 10
n = 3
url = \
urlopen("file:///Users/jsw/python/pygrib2/grib2_table4-2-%s-%s.shtml"%(m,n))
soup = BeautifulSoup(url)
print_table(soup.find("table"),m,n)
