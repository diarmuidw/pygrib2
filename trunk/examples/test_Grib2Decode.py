from grib2 import Grib2Decode
import numpy as N
# open a GRIB2 file, create a Grib2 class instance.
grbs = Grib2Decode('../sampledata/eta.grb')  
# print an inventory of the file.
for g in grbs:
    print g
# extract just geopotential height on isobaric surfaces.
zgribs = [g for g in grbs if g.parameter == 'Geopotential height' and g.vertical_level_descriptor == 'Isobaric surface']
nlevs = len(zgribs)
nlons = zgribs[0].points_in_x_direction
nlats = zgribs[0].points_in_y_direction
data = N.zeros((nlevs,nlats,nlons),'f')
print
# verify we got z on p.
for nlev,zg in enumerate(zgribs):
    if nlev == 0: lats,lons = zg.grid() # get lats and lons of grid
    print nlev,zg
    data[nlev] = zg.data()
print
# plot min/max of data and grid.
print data.shape,data.min(),data.max()
print lats.shape,lats.min(),lats.max()
print lons.shape,lons.min(),lons.max()
