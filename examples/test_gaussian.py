from grib2 import Grib2Decode
from pylab import *
from mpl_toolkits.basemap import Basemap
grbs = Grib2Decode('../sampledata/flux.grb')
lats, lons = grbs[1].grid()
data = grbs[1].data()
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
x,y = m(lons,lats)
m.drawcoastlines()
m.contourf(x,y,data,15)
#m.fillcontinents()
title('Global Gaussian Grid')
show()
