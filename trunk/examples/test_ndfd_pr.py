from grib2 import Grib2Decode
from pylab import *
from mpl_toolkits.basemap import Basemap
from numpy import ma
grbs = Grib2Decode('../sampledata/dspr.temp.grb')
g = grbs[3]
data = g.data()
lats, lons = g.grid()
llcrnrlon = lons[0,0]
llcrnrlat = lats[0,0]
urcrnrlon = lons[-1,-1]
urcrnrlat = lats[-1,-1]
rsphere = (g.earthRmajor,g.earthRminor)
lat_ts = g.proj4_lat_ts
lon_0 = g.proj4_lon_0
projection = g.proj4_proj
fig=figure()
ax = fig.add_axes([0.1,0.1,0.75,0.75])
m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,
            urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,rsphere=rsphere,lon_0=lon_0,
            lat_ts=lat_ts,resolution='h',projection=projection)
x,y = m(lons, lats)
cs = m.contourf(x,y,data,20,cmap=cm.jet,colors=None)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.drawmeridians(arange(280,300,1),labels=[0,0,0,1])
m.drawparallels(arange(16,21,1),labels=[1,0,0,0])
# new axis for colorbar.
cax = axes([0.875, 0.10, 0.03, 0.75])
colorbar(cs, cax, format='%g') # draw colorbar
axes(ax)  # make the original axes current again
title('NDFD Temp Puerto Rico '+g.forecast_time,fontsize=12)
show()
