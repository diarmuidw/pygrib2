from grib2 import Grib2Decode
from pylab import *
from mpl_toolkits.basemap import Basemap
grbs = Grib2Decode('../sampledata/gfs.grb')
for g in grbs:
    if g.parameter_abbrev == 'PRES' and g.vertical_level_descriptor == 'Ground or Water Surface':
        data = g.data()
        lats,lons = g.grid()
        break
print lats[:,0]
print lons[0,:]
llcrnrlon = lons[0,0]
llcrnrlat = lats[0,0]
urcrnrlon = lons[-1,-1]
urcrnrlat = lats[-1,-1]
print llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat
m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,
            urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,
            resolution='c',projection='cyl')
m.scatter(lons.flat,lats.flat,1,marker='o',color='k',zorder=10)
m.drawcoastlines()
x,y = m(lons,lats)
m.contourf(x,y,data,15)
#m.fillcontinents()
title('Global Lat/Lon Grid')
show()
