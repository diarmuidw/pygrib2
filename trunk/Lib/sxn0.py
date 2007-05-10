# CODE AND FLAG TABLES USED IN SECTION 0
# from FM 92 GRIB (Edition 2 - Version 3 - 02/11/2005)
# http://www.wmo.int/web/www/DPS/grib-2.html
# Jeffrey Whitaker <jeffrey.s.whitaker@noaa.gov>
# Code Table 0.0: Discipline of processed data in the GRIB message, 
# number of GRIB Master Table
codetable={0:'Meteorological products',
  0:'Meteorological products', 
  1:'Hydrological products', 
  2:'Land surface products', 
  3:'Space products', 
 10:'Oceanographic products',  
255:'Missing'}
for n in range(256):
    if not codetable.has_key(n): codetable[n]='Reserved' 
for n in range(192,256):
    codetable[n] = 'Reserved for local use'
