# CODE AND FLAG TABLES USED IN SECTION 3
# from FM 92 GRIB (Edition 2 - Version 23- 02/11/2005)
# http://www.wmo.int/web/www/DPS/grib-2.html
# Jeffrey Whitaker <jeffrey.s.whitaker@noaa.gov>
# Code Table 3.1: Grid Definition Template Number (Map projection)
codetable = {1:{0:'Latitude/longitude',
  1:'Rotated latitude/longitude',
  2:'Stretched latitude/longitude',
  3:'Stretched and rotated latitude/longitude',
 10:'Mercator',
 20:'Polar stereographic',
 30:'Lambert Conformal',
 31:'Albers equal-area',
 40:'Gaussian latitude/longitude',
 41:'Rotated Gaussian latitude/longitude',
 42:'Stretched Gaussian latitude/longitude',
 43:'Stretched and rotated Gaussian latitude/longitude',
 50:'Spherical harmonic coefficients',
 51:'Rotated spherical harmonic coefficients',
 52:'Stretched spherical harmonic coefficients',
 53:'Stretched and rotated spherical harmonic coefficients',
 90:'Space view perspective orthographic',
100:'Triangular grid based on an icosahedron',
110:'Equatorial azimuthal equidistant projection',
120:'Azimuth-range projection',
203:'Rotated Latitude/Longitude (Arakawa Staggerred E-Grid)',
204:'Curvilinear Orthogonal Grid',
205:'Rotated Latitude/Longitude (Arakawa Staggerred B-Grid)',
1000:'Cross-section grid, with points equally spaced on the horizontal',
1100:'Hovmoller diagram grid, with points equally spaced on the horizontal',
1200:'Time section grid',
65535:'Missing'}}
for n in range(32678):
    if not codetable[1].has_key(n): codetable[1][n]='Reserved'
for n in range(32678,65535):
    codetable[1][n]='Reserved for local use' 
# Code Table 3.2: Shape of the Earth.
codetable[2]={0:6367470.0,
1:'Spherical - radius specified in m by data producer',
2:(6378160.0,6356775.0),
3:'OblateSpheroid - major and minor axes specified in km by data producer',
4:(6378137.0,6356752.314),
5:'WGS84',
6:6371229.0,
7:'OblateSpheroid - major and minor axes specified in m by data producer',
255:'Missing'}
for n in range(192):
    if not codetable[2].has_key(n): codetable[2][n]='Reserved'
for n in range(192,255):
    codetable[2][n] = 'Reserved for local use'
