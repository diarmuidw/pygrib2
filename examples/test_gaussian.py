from grib2 import Grib2Decode
from pylab import *
from matplotlib.toolkits.basemap import Basemap
grbs = Grib2Decode('../sampledata/flux.grb')
lats, lons = grbs[0].grid()
print lats[:,0]
print lons[0,:]
llcrnrlon = lons[0,0]
llcrnrlat = lats[-1,-1]
urcrnrlon = lons[-1,-1]
urcrnrlat = lats[0,0]
print llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat
m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,
            urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,
            resolution='c',projection='cyl')
m.scatter(lons.flat,lats.flat,1,marker='o',color='k',zorder=10)
m.drawcoastlines()
m.fillcontinents()
title('Global Gaussian Grid')
show()
