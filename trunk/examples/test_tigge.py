from pylab import *
from mpl_toolkits.basemap import Basemap
from numpy import ma
from grib2 import Grib2Decode, dump

grbs = Grib2Decode('../sampledata/tigge.grb')
for grb in grbs:
    fld = 0.01*grb.data() # convert to hPa
    lats,lons = grb.grid()
    print grb.originating_center, fld.shape, fld.min(), fld.max()
    fig=figure(figsize=(10,5))
    fig.add_axes([0.1,0.1,0.8,0.8])
    # setup robinson world map projection.
    m = Basemap(projection='robin',lon_0=180)
    x, y = m(lons,lats)
    levels = arange(475,1101,25)
    CS = m.contourf(x,y,fld,levels,cmap=cm.jet)
    colorbar(drawedges=True, shrink=0.8) # draw colorbar
    m.drawcoastlines()
    m.drawparallels(arange(-80,81,20),labels=[1,0,0,0])
    m.drawmeridians(arange(0,360,60),labels=[0,0,0,1])
    m.drawmapboundary()
    title(grb.parameter+' '+grb.originating_center)
show()
