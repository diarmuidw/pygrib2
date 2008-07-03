from grib2 import Grib2Decode
from pylab import *
from mpl_toolkits.basemap import Basemap
from numpy import ma
grbs = Grib2Decode('../sampledata/ds.temp.grb')
g = grbs[0]
lats, lons = g.grid()
data = g.data(masked_array=False)
data = ma.masked_values(data,g.missing_value)
print data.dtype
print data.shape, lons.shape, lats.shape
print data.min(), data.max()
llcrnrlon = lons[0,0]
llcrnrlat = lats[0,0]
urcrnrlon = lons[-1,-1]
urcrnrlat = lats[-1,-1]
rsphere = (grbs[0].earthRmajor,grbs[0].earthRminor)
lat_1 = grbs[0].proj4_lat_1
lat_2 = grbs[0].proj4_lat_2
lon_0 = grbs[0].proj4_lon_0
projection = grbs[0].proj4_proj
fig=figure()
ax = fig.add_axes([0.1,0.1,0.75,0.75])
m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,
            urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,rsphere=rsphere,lon_0=lon_0,
            lat_1=lat_1,lat_2=lat_2,resolution='l',projection=projection,area_thresh=10000)
x,y = m(lons, lats)
cs = m.contourf(x,y,data,20,cmap=cm.jet,colors=None)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
# new axis for colorbar.
cax = axes([0.875, 0.15, 0.03, 0.65])
colorbar(cs, cax, format='%d') # draw colorbar
axes(ax)  # make the original axes current again
title('NDFD Temp CONUS '+g.forecast_time,fontsize=12)
show()
