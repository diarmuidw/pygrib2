from pylab import *
from matplotlib.toolkits.basemap import Basemap
from numpy import ma
from grib2 import Grib2Decode, dump

grbs = Grib2Decode('../sampledata/ecmwf_tigge.grb')
for g in grbs:
    if g.parameter == 'Volumetric soil moisture':
        fld = g.data(masked_array=True)
        lats, lons = g.grid()
        break
# stack grids side-by-side (in longitiudinal direction), so
# any range of longitudes (between -360 and 360) may be plotted on a world map.
lons = concatenate((lons-360,lons),1)
lats = concatenate((lats,lats),1)
fld = ma.concatenate((fld,fld),1)
# setup miller cylindrical map projection.
m = Basemap(llcrnrlon=-180.,llcrnrlat=-90,urcrnrlon=180.,urcrnrlat=90.,\
            resolution='l',area_thresh=10000.,projection='mill')
x, y = m(lons,lats)
CS = m.contourf(x,y,fld,15,cmap=cm.jet)
#im = m.pcolor(x,y,fld,cmap=cm.jet,shading='flat')
ax = gca()
l,b,w,h=ax.get_position()
cax = axes([l+w+0.025, b, 0.025, h]) # setup colorbar axes
colorbar(drawedges=True, cax=cax) # draw colorbar
axes(ax)  # make the original axes current again
m.drawcoastlines()
# draw parallels
delat = 30.
circles = arange(-90.,90.+delat,delat)
m.drawparallels(circles,labels=[1,0,0,0])
# draw meridians
delon = 60.
meridians = arange(-180,180,delon)
m.drawmeridians(meridians,labels=[0,0,0,1])
title(g.parameter+' on ECMWF Reduced Gaussian Grid')
show()
