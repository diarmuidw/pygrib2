from grib2 import Grib2Decode
from pylab import *
from matplotlib.toolkits.basemap import Basemap
grbs = Grib2Decode('../sampledata/dspr.maxt.grb')
lats, lons = grbs[0].grid()
print lats[:,0]
print lons[0,:]
llcrnrlon = lons[0,0]
llcrnrlat = lats[0,0]
urcrnrlon = lons[-1,-1]
urcrnrlat = lats[-1,-1]
rsphere = (grbs[0].earthRmajor,grbs[0].earthRminor)
lat_ts = grbs[0].proj4_lat_ts
lon_0 = grbs[0].proj4_lon_0
projection = grbs[0].proj4_proj
m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,
            urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,rsphere=rsphere,lon_0=lon_0,
            lat_ts=lat_ts,resolution='i',projection=projection)
x,y = m(lons, lats)
m.scatter(x.flat,y.flat,1,marker='o',color='k',zorder=10)
m.drawcoastlines()
m.fillcontinents()
title('Mercator Grid (Puerto Rico)')
show()
