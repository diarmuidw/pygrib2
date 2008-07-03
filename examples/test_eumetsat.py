from grib2 import Grib2Decode
from pylab import *
from numpy import ma
from mpl_toolkits.basemap import Basemap, cm

grbs = Grib2Decode('../sampledata/eumetsat_precip.grb')
g = grbs[0]
fld = g.data(masked_array=True)
print fld.shape, fld.min(), fld.max()
print g.proj4_lon_0,g.proj4_h,g.earthRmajor,g.earthRminor
lats, lons = g.grid()

m = Basemap(lon_0=g.proj4_lon_0,satellite_height=g.proj4_h,\
            rsphere = (g.earthRmajor,g.earthRminor),\
            resolution='l',area_thresh=10000.,projection='geos')
# plot every 50th point.
x, y = m(lons,lats)
m.scatter(x[::50,::50].flat,y[::50,::50].flat,1,marker='o',color='k',zorder=10)
m.drawcoastlines()
m.fillcontinents(color='coral')
m.drawparallels(arange(-80,81,20))
m.drawmeridians(arange(-90,90,20))
m.drawmapboundary()
title('EUMETSAT geostationary projection grid')
show()
