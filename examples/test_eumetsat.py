from grib2 import Grib2Decode
from pylab import *
from numpy import ma
from matplotlib.toolkits.basemap import Basemap, addcyclic

grbs = Grib2Decode('../sampledata/eumetsat_precip.grb')
fld = grbs[0].data(masked_array=True)
print fld.shape, fld.min(), fld.max()
lats, lons = grbs[0].grid()
# make lons, lats into masked arrays.
lons = ma.masked_values(lons, 1.e30)
lats = ma.masked_values(lats, 1.e30)
print lons.shape, lons.min(), lons.max()
print lats.shape, lats.min(), lats.max()

m = Basemap(llcrnrlon=-180.,llcrnrlat=-90,urcrnrlon=180.,urcrnrlat=90.,\
            resolution='c',area_thresh=10000.,projection='cyl')
# plot every 50th point.
m.scatter(lons[::50,::50].flat,lats[::50,::50].flat,1,marker='o',color='k',zorder=10)
m.drawcoastlines()
m.fillcontinents()
title('EUMETSAT geostationary projection grid')
show()
