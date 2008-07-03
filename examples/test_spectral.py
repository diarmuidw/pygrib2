from pylab import *
from mpl_toolkits.basemap import Basemap
from grib2 import Grib2Decode
try:
    import spharm
except:
    raise ImportError("requires pyspharm (python spherical harmonic module) from http://code.google.com/p/pyspharm")

grbs = Grib2Decode('../sampledata/spectral.grb')
for g in grbs:
    if g.parameter_abbrev == 'TMP' and g.vertical_level=='0.99598':
        fld = g.data()
        break

print fld.min(), fld.max(), fld.shape
fldr = fld[0::2]
fldi = fld[1::2]
fld = zeros(fldr.shape,'F')
fld.real = fldr
fld.imag = fldi
ntrunc = g.spectral_truncation_parameters[0]
print ntrunc
nlons = 360;  nlats = 181
s = spharm.Spharmt(nlons,nlats)
print fld.real[0:10]
print fld.imag[0:10]
data = s.spectogrd(fld)
print data.min(),data.max()
lons = (360./nlons)*arange(nlons)
lats = 90.-(180./(nlats-1))*arange(nlats)
lons, lats = meshgrid(lons, lats)
# stack grids side-by-side (in longitiudinal direction), so
# any range of longitudes (between -360 and 360) may be plotted on a world map.
lons = concatenate((lons-360,lons),1)
lats = concatenate((lats,lats),1)
data = concatenate((data,data),1)
# setup miller cylindrical map projection.
m = Basemap(llcrnrlon=-180.,llcrnrlat=-90,urcrnrlon=180.,urcrnrlat=90.,\
            resolution='l',area_thresh=10000.,projection='mill')
x, y = m(lons,lats)
CS = m.contourf(x,y,data,15,cmap=cm.jet)
ax = gca()
pos = ax.get_position()
l, b, w, h = pos.bounds
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
title(g.parameter+' at '+g.vertical_level+' from Spherical Harmonic Coeffs')
show()
