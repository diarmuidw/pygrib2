from pylab import *
from mpl_toolkits.basemap import Basemap
from numpy import ma
from grib2 import Grib2Decode, dump

grbs = Grib2Decode('../sampledata/tigge.grib')
for grb in grbs:
    fld = 0.01*grb.data() # convert to hPa
    lats,lons = grb.grid()
    print grb.originating_center, fld.shape, fld.min(), fld.max()
    # stack grids side-by-side (in longitiudinal direction), so
    # any range of longitudes (between -360 and 360) may be plotted on a world map.
    lons = concatenate((lons-360,lons),1)
    lats = concatenate((lats,lats),1)
    fld = ma.concatenate((fld,fld),1)
    fig=figure(figsize=(9,6))
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    # setup miller cylindrical map projection.
    m = Basemap(llcrnrlon=-180.,llcrnrlat=-90,urcrnrlon=180.,urcrnrlat=90.,\
                resolution='l',area_thresh=10000.,projection='mill')
    x, y = m(lons,lats)
    levels = arange(475,1101,25)
    CS = m.contourf(x,y,fld,levels,cmap=cm.jet)
    pos = ax.get_position()
    l, b, w, h = pos.bounds
    cax = axes([l+w+0.025, b, 0.025, h]) # setup colorbar axes
    colorbar(drawedges=True, cax=cax, format='%d') # draw colorbar
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
    title(grb.parameter+' '+grb.originating_center)
show()
