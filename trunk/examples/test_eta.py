from pylab import *
from mpl_toolkits.basemap import Basemap
from grib2 import *

grbs = Grib2Decode('../sampledata/eta_wheaders.grb')
for g in grbs:
    if g.parameter_abbrev == 'T_MAX':
        data = g.data()
        lats,lons = g.grid()
        break

llcrnrlat            = lats[0,0]
llcrnrlon            = lons[0,0]
urcrnrlat            = lats[-1,-1]
urcrnrlon            = lons[-1,-1]
lat1    = g.proj4_lat_1 # two parallels
lat2    = g.proj4_lat_2
lon0    = g.proj4_lon_0     # central meridian
rsphere = (g.earthRmajor, g.earthRminor)
projection = g.proj4_proj
print data.shape, data.min(), data.max()
print llcrnrlat,llcrnrlat,urcrnrlat,urcrnrlon
# make a plot using matplotlib basemap toolkit.
# (http://matplotlib.sf.net/toolkits.html)
m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,
            urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,rsphere=rsphere,lon_0=lon0,
            lat_1=lat1,lat_2=lat2,resolution='l',projection=projection)
# setup fig axes so map aspect ratio is preserved.
fig=figure()
ax = fig.add_axes([0.1,0.1,0.75,0.75])
# draw coastlines, state and country boundaries, edge of map.
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.drawmapboundary()
# draw parallels.
delat = 20.0
parallels = arange(0.,90.+delat,delat).tolist()
m.drawparallels(parallels,labels=[1,0,0,0])
# draw meridians
delon = 30.
meridians = arange(0.,360.,delon)
m.drawmeridians(meridians,labels=[0,0,0,1])
x, y = m(lons, lats) # compute map proj coordinates.
# draw filled contours.
cs = m.contourf(x,y,data,20,cmap=cm.jet,colors=None)
# new axis for colorbar.
cax = axes([0.875, 0.10, 0.04, 0.75])
colorbar(cs, cax, format='%d') # draw colorbar
axes(ax)  # make the original axes current again
title('ETA '+g.vertical_level+' '+g.parameter+' ['+g.parameter_units+']')
label = g.forecast_time
text(0.5*(m.xmin+m.xmax), m.ymin-0.1*(m.ymax-m.ymin), label, horizontalalignment='center', fontsize=14)
#savefig('ploteta') # save to png file.
show() # or, display onscreen.

