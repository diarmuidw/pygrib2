from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
url = urlopen("http://www.nco.ncep.noaa.gov/pmb/docs/on388/table0.html")
soup = BeautifulSoup(url)
table = soup.find("table")
for row in table.findAll("tr"):
    cols = row.findAll("td")
    if len(cols) == 2:
        if cols[0].find(text=True).find('-') > 0:
            # handle ranges of the for xxx-xxx
            n1 = int(cols[0].find(text=True).split('-')[0])
            n2 = int(cols[0].find(text=True).split('-')[1])
            for number in range(n1,n2+1):
                parameter = cols[1].find(text=True)
                print "%s:'%s'," % (number,parameter)
            continue
        else:
            number = cols[0].find(text=True)
            if number.rstrip() == '':
                number = cols[0].find("center").find(text=True)
            parameter = cols[1].find(text=True)
        # remove extra whitespace.
        parameter = parameter.rstrip().replace('\n',' ')
        parameter = ' '.join(parameter.split())
        print "%s:'%s'," % (number,parameter)
