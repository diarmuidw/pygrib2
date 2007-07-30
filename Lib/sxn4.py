# CODE AND FLAG TABLES USED IN SECTION 4
# from FM 92 GRIB (Edition 2 - Version 3 - 02/11/2005)
# http://www.wmo.int/web/www/DPS/grib-2.html
# Jeffrey Whitaker <jeffrey.s.whitaker@noaa.gov>
codetable={}
# 4.0 Product Definition Template Number
codetable[0]={
0:'Analysis or forecast at a horizontal level or in a horizontal layer at a point in time', 
1:'Individual ensemble forecast, control and perturbed, at a horizontal level or in a horizontal layer at a point in time',  
2:'Derived forecast based on all ensemble members at a horizontal level or in a horizontal layer at a point in time', 
3:'Derived forecasts based on a cluster of ensemble members over a rectangular area at a horizontal level or in a horizontal layer at a point in time', 
4:'Derived forecasts based on a cluster of ensemble members over a circular area at a horizontal level or in a horizontal layer at a point in time', 
5:'Probability forecasts at a horizontal level or in a horizontal layer at a point in time',  
6:'Percentile forecasts at a horizontal level or in a horizontal layer at a point in time', 
7:'Analysis or forecast error at a horizontal level or in a horizontal layer at a point in time', 
8:'Average, accumulation, extreme values or other statistically processed values at a horizontal level or in a horizontal layer in a continuous or non-continuous time interval', 
9 :'Probability forecasts at a horizontal level or in a horizontal layer in a continuous or non-continuous time interval', 
10:'Percentile forecasts at a horizontal level or in a horizontal layer in a continuous or non-continuous time interval', 
11:'Individual ensemble forecast, control and perturbed, at a horizontal level or in a horizontal layer, in a continuous or non-continuous interval', 
12:'Derived forecasts based in all ensemble  members at a horizontal level or in a horizontal layer, in a continuous or non-continuous interval', 
13:'Derived forecasts based on a cluster of ensemble members over a rectangular area, at a horizontal level or in a horizontal layer, in a continuous or non-continuous interval', 
14:'Derived forecasts based on a cluster of ensemble members over a circular area, at a horizontal level or in a horizontal layer, in a continuous or non-continuous interval', 
20:'Radar product',
30:'Satellite product',
253:'CCITT IA5 character string',
1000:'Cross section of analysis and forecast at a point in time', 
1001:'Cross section of averaged or otherwise statistically processed analysis or forecast over a range of time', 
1002:'Cross-section of analysis and forecast, averaged or otherwise statistically processed', 
1100:'Hovmuller-type grid with no averaging or other statistical processing', 
1101:'Hovmuller-type grid with averaging or other statistical processing', 
65535:'Missing'}
for n in range(32678):
    if not codetable[0].has_key(n): codetable[0][n]='Reserved'
for n in range(32678,65535):
    codetable[0][n]='Reserved for local use' 
# 4.1 Category of parameters by product discipline 
# 0: Meteorological Products
codetable[1]={0:{0: 'Temperature', 
1: 'Moisture',
2: 'Momentum',
3: 'Mass',
4: 'Short-wave Radiation', 
5: 'Long-wave Radiation', 
6: 'Cloud',
7: 'Thermodynamic Stability indices', 
8: 'Kinematic Stability indices',
9: 'Temperature Probabilities', 
10: 'Moisture Probabilities', 
11: 'Momentum Probabilities', 
12: 'Mass Probabilities', 
13: 'Aerosols', 
14: 'Trace gases (e.g., ozone, CO2)', 
15: 'Radar',
16: 'Forecast Radar Imagery', 
17: 'Electro-dynamics', 
18: 'Nuclear/radiology', 
19: 'Physical atmospheric properties', 
190:'CCITT IA5 string', 
191:'Miscellaneous', 
255:'Missing'},1:{},2:{},3:{},10:{}}
for n in range(192):
    if not codetable[1][0].has_key(n): codetable[1][0][n]='Reserved'
for n in range(192,255):
    codetable[1][0][n] = 'Reserved for local use'
# 1: Hydrological Products    
codetable[1][1]={0: 'Hydrology basic products',
1:'Hydrology probabilities', 
255:'Missing'}
for n in range(192):
    if not codetable[1][1].has_key(n): codetable[1][1][n]='Reserved'
for n in range(192,255):
    codetable[1][1][n] = 'Reserved for local use'
# 2: Land Surface Products
codetable[1][2]={0: 'Vegetation/Biomass', 
1:'Agri-/aquacultural Special Products',  
2:'Transportation-related Products' ,
3:'Soil Products', 
255:'Missing'}
for n in range(192):
    if not codetable[1][2].has_key(n): codetable[1][2][n]='Reserved'
for n in range(192,255):
    codetable[1][2][n] = 'Reserved for local use'
# 3: Space Products
codetable[1][3]={0: 'Image format products', 
1:'Quantitative products', 
255:'Missing'}
for n in range(192):
    if not codetable[1][3].has_key(n): codetable[1][3][n]='Reserved'
for n in range(192,255):
    codetable[1][3][n] = 'Reserved for local use'
# 10: Oceanographic Products   
codetable[1][10]={0: 'Waves', 
1:'Currents', 
2:'Ice', 
3:'Surface Properties', 
4:'Sub-surface Properties', 
255:'Missing'} 
for n in range(192):
    if not codetable[1][10].has_key(n): codetable[1][10][n]='Reserved'
for n in range(192,255):
    codetable[1][10][n] = 'Reserved for local use'
# 4.2: Parameter number by product discipline and parameter category.
# Product Discipline 0: Meterological Products
# 0: Temperature.
codetable[2]={0:{0:{0:('Temperature','K'),
1:('Virtual temperature','K'), 
2:('Potential temperature','K'), 
3:('Pseudo-adiabatic or equivalent potential temperature','K'),  
4:('Maximum temperature','K'), 
5:('Minimum temperature','K'), 
6:('Dew point temperature','K'), 
7:('Dew point depression (or deficit)','K'), 
8:('Lapse rate','K m-1'), 
9:('Temperature anomaly','K'), 
10:('Latent heat net flux','W m-2'), 
11:('Sensible heat net flux','W m-2'), 
12:('Heat index','K'), 
13:('Wind chill factor','K'), 
14:('Minimum dew point depression','K'), 
15:('Virtual potential temperature','K'),
16:('Snow phase change heat flux','W m-2'),
17:('Skin temperature','K'),
19:('Snow albedo','percent'),
255:('Missing','')},
1:{},2:{},3:{},4:{},5:{},6:{},7:{},13:{},14:{},15:{},18:{},19:{},190:{},191:{}},1:{},2:{},3:{},10:{}}
for n in range(192):
    if not codetable[2][0][0].has_key(n): codetable[2][0][0][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][0][n] = ('Reserved for local use','')
# 1: Moisture.
codetable[2][0][1]={0:('Specific humidity','kg kg-1'),          
 1:('Relative humidity','%'),
 2:('Humidity mixing ratio','kg kg-1'),
 3:('Precipitable water','kg m'),
 4:('Vapor pressure','Pa'),
 5:('Saturation deficit','Pa'),
 6:('Evaporation','kg m-2'),
 7:('Precipitation rate','kg m-2 s-1'),
 8:('Total precipitation','kg m-2'),
 9:('Large scale precipitation (non-convective)','kg m-2'),
10:('Convective precipitation','kg m-2'),
11:('Snow depth','m'),
12:('Snowfall rate water equivalent','kg m-2 s-1'),
13:('Water equivalent of accumulated snow depth','kg m-2'),
14:('Convective snow','kg m-2'),
15:('Large scale snow','kg m-2'),
16:('Snow melt','kg m-2'),
17:('Snow age','day'),
18:('Absolute humidity','kg m-3'),
19:('Precipitation type','code table (4.201)'),
20:('Integrated liquid water','kg m-2'),
21:('Condensate','kg kg-1'),
22:('Cloud mixing ratio','kg kg-1'),
23:('Ice water mixing ratio','kg kg-1'),
24:('Rain mixing ratio','kg kg-1'),
25:('Snow mixing ratio','kg kg-1'),
26:('Horizontal moisture convergence','kg kg-1 s-1'),
27:('Maximum relative humidity','%'),
28:('Maximum absolute humidity','kg m-3'),
29:('Total snowfall','m'),
30:('Precipitable water category','code table (4.202)'),
31:('Hail','m'),
32:('Graupel (snow pellets)','kg kg-1'),
33:('Categorical rain','code table (4.222)'),
34:('Categorical freezing rain','code table (4.222)'),
35:('Categorical ice pellets','code table (4.222)'),
36:('Categorical snow','code table (4.222)'),
37:('Convective precipitation rate','kg m-2 s-1'), 
38:('Horizontal moisture divergence','kg kg-1 s-1'), 
39:('Percent frozen precipitation','%'), 
40:('Potential evaporation','kg m-2'),
41:('Potential evaporation rate','W m-2'), 
42:('Snow cover','%'), 
43:('Rain fraction of total cloud water','Proportion'), 
44:('Rime factor','Numeric'), 
45:('Total column integrated rain','kg m-2'),
46:('Total column integrated snow','kg m-2'),
47:('Large-scale precipitaton (non-convective)','kg m-2'),
48:('Convective water precipitation','kg m-2'),
49:('Total water precipitation','kg m-2'),
50:('Total snow precipitation','kg m-2'),
51:('Total column water','kg m-2'),
52:('Total precipitation','kg m-2'),
53:('Total snowfall water equivalent','kg m-2'),
54:('Large-scale precipitation rate','kg m-2 s-1'),
55:('Convective snowfall rate (water equivalent)','kg m-2 s-1'),
56:('Large-scale snowfall rate (water equivalent)','kg m-2 s-1'),
57:('Total snowfall rate','m s-1'),
58:('Convective snowfall rate','m s-1'),
59:('Large-scale snowfall rate','m s-1'),
60:('Snow depth (water-equivalent)','kg m-2'),
61:('Snow density','kg m-3'),
62:('Snow evaporation','kg m-2'),
63:('Large-scale precipitation fraction','s'),
64:('Total column-integrated water vapor','kg m-2'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][1].has_key(n): codetable[2][0][1][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][1][n] = ('Reserved for local use','')
# 2: Momentum. 
codetable[2][0][2]={0:('Wind direction (from which blowing)','deg true'),
 1:('Wind speed','m s-1'),
 2:('u-component of wind','m s-1'),
 3:('v-component of wind','m s-1'),
 4:('Stream function','m2 s-1'),
 5:('Velocity potential','m2 s-1'),
 6:('Montgomery stream function','m2 s-2'),
 7:('Sigma coordinate vertical velocity','s-1'),
 8:('Vertical velocity (pressure)','Pa s-1'),
 9:('Vertical velocity (geometric)','m s-1'),
10:('Absolute vorticity','s-1'),
11:('Absolute divergence','s-1'),
12:('Relative vorticity','s-1'),
13:('Relative divergence','s-1'),
14:('Potential vorticity','K m2 kg-1 s-1'),
15:('Vertical u-component shear','s-1'),
16:('Vertical v-component shear','s-1'),
17:('Momentum flux, u component','N m-2'),
18:('Momentum flux, v component','N m-2'),
19:('Wind mixing energy','J'),
20:('Boundary layer dissipation','W m-2'),
21:('Maximum wind speed','m s-1'),
22:('Wind speed (gust)','m s-1'),
23:('u-component of wind (gust)','m s-1'),
24:('v-component of wind (gust)','m s-1'), 
25:('Vertical speed shear','s-1'), 
26:('Horizontal momentum flux','N m-2'), 
27:('U-component storm motion','m s-1'), 
28:('V-component storm motion','m s-1'), 
29:('Drag coefficient','Numeric'), 
30:('Frictional velocity','m s-1'), 
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][2].has_key(n): codetable[2][0][2][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][2][n] = ('Reserved for local use','')
# 3: Mass.
codetable[2][0][3]={0:('Pressure','Pa'), 
 1:('Pressure reduced to MSL','Pa'),
 2:('Pressure tendency','Pa s-1'),
 3:('ICAO Standard Atmosphere Reference Height','m'),
 4:('Geopotential','m2 s-2'),
 5:('Geopotential height','gpm'),
 6:('Geometric height','m'),
 7:('Standard deviation of height','m'),
 8:('Pressure anomaly','Pa'),
 9:('Geopotential height anomaly','gpm'),
10:('Density','kg m-3'),
11:('Altimeter setting','Pa'),
12:('Thickness','m'),
13:('Pressure altitude','m'),
14:('Density altitude','m'),
15:('5-wave geopotential height','gpm'), 
16:('Zonal flux of gravity wave stress','N m-2'), 
17:('Meridional flux of gravity wave stress','N m-2'), 
18:('Planetary boundary layer height','m'), 
19:('5-wave geopotential height anomaly','gpm'), 
20:('Standard deviation of sub-grid scale orography','m'),
21:('Angle of sub-gridscale orography','radians'),
22:('Slope of sub-gridscale orography','Numeric'),
23:('Gravity wave dissipation','W m-2'),
24:('Anisotropy of sub-gridscale orography','Numeric'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][3].has_key(n): codetable[2][0][3][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][3][n] = ('Reserved for local use','')
# 4: Short-wave radiation.
codetable[2][0][4]={0:('Net short-wave radiation flux (surface)','W m-2'),
1:('Net short-wave radiation flux (top of atmosphere)','W m-2'),
2:('Short wave radiation flux','W m-2'),
3:('Global radiation flux','W m-2'),
4:('Brightness temperature','K'),
5:('Radiance (with respect to wave number)','W m-1 sr-1'),
6:('Radiance (with respect to wave length)','W m-3 sr-1'),
7:('Downward short-wave radiation flux','W m-2'),
8:('Upward short-wave radiation flux','W m-2'), 
9:('Time-integrated net short-wave radiation at the surface','W m-2 s'),
10:('Photosynthetically active radiation','W m-2'),
11:('Net short-wave radiation flux (clear sky)','W m-2'),
12:('Downward UV radiation','W m-2'),
50:('UV index (under clear sky)','Numeric'),
51:('UV index','Numeric'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][4].has_key(n): codetable[2][0][4][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][4][n] = ('Reserved for local use','')
# 5: Long-wave radiation.
codetable[2][0][5]={0:('Net long-wave radiation flux (surface)','W m-2'),
1:('Net long-wave radiation flux (top of atmosphere)','W m-2'),
2:('Long-wave radiation flux','W m-2'),
3:('Downward long-wave radiation flux','W m-2'),
4:('Upward long-wave radiation flux','W m-2 '),
5:('Time-integrated net long-wave radiation (top of the atmosphere)','W m-2 s'),
6:('Net long-wave radiation flux (clear sky)','W m-2'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][5].has_key(n): codetable[2][0][5][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][5][n] = ('Reserved for local use','')
# 6: Cloud 
codetable[2][0][6]={0:('Cloud ice','kg m-2'),
 1:('Total cloud cover','%'),
 2:('Convective cloud cover','%'),
 3:('Low cloud cover','%'),
 4:('Medium cloud cover','%'),
 5:('High cloud cover','%'),
 6:('Cloud water','kg m-2'),
 7:('Cloud amount','%'),
 8:('Cloud type','code table (4.203)'),
 9:('Thunderstorm maximum tops','m'),
10:('Thunderstorm coverage','code table (4.204)'),
11:('Cloud base','m'),
12:('Cloud top','m'),
13:('Ceiling','m'),
14:('Non-convective cloud cover','%'),
15:('Cloud work function','J kg-1'), 
16:('Convective cloud efficiency','Proportion'), 
17:('Total condensate','kg kg-1'), 
18:('Total column-integrated cloud water','kg m-2'), 
19:('Total column-integrated cloud ice','kg m-2'), 
20:('Total column-integrated condensate','kg m-2'), 
21:('Ice fraction of total condensate','Proportion'), 
22:('Cloud cover','percent'),
23:('Cloud water mixing ratio','kg kg-1'),
24:('Sunshine duration','s'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][6].has_key(n): codetable[2][0][6][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][6][n] = ('Reserved for local use','')
# 7. Thermodynamic Stability Indices.
codetable[2][0][7]={0:('Parcel lifted index (to 500 hPa)','K'), 
1:('Best lifted index (to 500 hPa','K'),
2:('K index','K'), 
3:('KO index','K'), 
4:('Total totals index','K'), 
5:('Sweat index',''), 
6:('Convective available potential energy','J kg-1'), 
7:('Convective inhibition','J kg-1'), 
8:('Storm relative helicity','J kg-1'), 
9:('Energy helicity index',''),  
10:('Surface lifted index','K'), 
11:('Best (4-layer) lifted index','K'), 
12:('Richardson number','Numeric'), 
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][7].has_key(n): codetable[2][0][7][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][7][n] = ('Reserved for local use','') 
# 13: Aerosols. 
codetable[2][0][13]={0:('Aerosol type','code table (4.205)'), 
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][13].has_key(n): codetable[2][0][13][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][13][n] = ('Reserved for local use','')  
# 14: Trace Gases. 
codetable[2][0][14]={0:('Total ozone','Dobson'),
1:('Ozone mixing ratio','kg kg-1'),
2:('Total column-integrated ozone','Dobson'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][14].has_key(n): codetable[2][0][14][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][14][n] = ('Reserved for local use','')    
# 15: Radar.
codetable[2][0][15]={0:('Base spectrum width','m s-1'), 
1:('Base reflectivity','dB'),
2:('Base radial velocity','m s-1'),
3:('Vertically-integrated liquid','kg m-1'),
4:('Layer-maximum base reflectivity','dB'),
5:('Precipitation','kg m-2'),
6:('Radar spectra (1)',''),
7:('Radar spectra (2)',''),
8:('Radar spectra (3)',''),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][15].has_key(n): codetable[2][0][15][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][15][n] = ('Reserved for local use','')
# 18: Nuclear/radiology.
codetable[2][0][18]={0:('Air concentration of Caesium 137','Bq m-3'),
1:('Air concentration of Iodine 131','Bq m-3'),
2:('Air concentration of radioactive pollutant','Bq m-'),
3:('Ground deposition of Caesium 137','Bq m-2'),
4:('Ground deposition of Iodine 131','Bq m-2'),
5:('Ground deposition of radioactive pollutant','Bq m-2'),
6:('Time-integrated air concentration of caesium pollutant','Bq s m-3'),
7:('Time-integrated air concentration of iodine pollutant','Bq s m-3'),
8:('Time-integrated air concentration of radioactive pollutant','Bq s m-3'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][18].has_key(n): codetable[2][0][18][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][18][n] = ('Reserved for local use','')
# 19: Physical atmospheric properties. 
codetable[2][0][19]= {0:('Visibility','m'),
 1:('Albedo','%'),
 2:('Thunderstorm probability','%'),
 3:('mixed layer depth','m'),
 4:('Volcanic ash','code table (4.206)'),
 5:('Icing top','m'),
 6:('Icing base','m'),
 7:('Icing','code table (4.207)'),
 8:('Turbulence top','m'),
 9:('Turbulence base','m'),
10:('Turbulence','code table (4.208)'),
11:('Turbulent kinetic energy','J kg-1'),
12:('Planetary boundary layer regime','code table (4.209)'),
13:('Contrail intensity','code table (4.210)'),
14:('Contrail engine type','code table (4.211)'),
15:('Contrail top','m'),
16:('Contrail base','m'),
17:('Maximum snow albedo','%'),
18:('Snow free albedo','%'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][19].has_key(n): codetable[2][0][19][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][19][n] = ('Reserved for local use','')
# Parameter Category 190: ASCII character string.
codetable[2][0][190]= {0:('Arbitrary text string','CCITTIA5'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][190].has_key(n): codetable[2][0][190][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][190][n] = ('Reserved for local use','')
# Parameter Category 191: Miscellaneous.
codetable[2][0][191]= {0:('Seconds prior to initial reference time (defined in Section 1)','s'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][0][191].has_key(n): codetable[2][0][191][n]=('Reserved','')
for n in range(192,255):
    codetable[2][0][191][n] = ('Reserved for local use','')
# Product Discipline 1: Hydrologic products.
# Parameter Category 0: Hydrology basic products. 
codetable[2][1][0] = {0:('Flash flood guidance','kg m-2'), 
1:('Flash flood runoff','kg m-2'),
2:('Remotely sensed snow cover','(code table 4.215)'),
3:('Elevation of snow covered terrain','(code table 4.216)'),
4:('Snow water equivalent percent of normal','%'),
5:('Baseflow-groundwater runoff','kg m-2'),
6:('Storm surface runoff','kg m-2'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][1][0].has_key(n): codetable[2][1][0][n]=('Reserved','')
for n in range(192,255):
    codetable[2][1][0][n] = ('Reserved for local use','')
#Parameter Category 1: Hydrology probabilities.  
codetable[2][1][1] = {0:('Conditional percent precipitation amount fractile for an overall period','kg m-2'),
1:('Percent precipitation in a sub-period of an overall period','%'),
2:('Probability of 0.01 inch of precipitation (POP)','%'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][1][1].has_key(n): codetable[2][1][1][n]=('Reserved','')
for n in range(192,255):
    codetable[2][1][1][n] = ('Reserved for local use','')
# Product Discipline 2: Land surface products.
# Parameter Category 0: Vegetation/Biomass.
codetable[2][2][0] = {0:('Land cover (1=land, 2=sea)','Proportion'),
1:('Surface roughness',' m'),
2:('Soil temperature','K'),
3:('Soil moisture content','kg m-2'),
4:('Vegetation','%'),
5:('Water runoff','kg m-2'),
6:('Evapotranspiration','kg -2 s-1'),
7:('Model terrain height','m'),
8:('Land use','code table (4.212)'),
9:('Volumetric soil moisture content','Proportion'), 
10:('Ground heat flux','W m-2'), 
11:('Moisture availability','%'),
12:('Exchange coefficient','kg m-2 s-1'), 
13:('Plant canopy surface water','kg m-2'), 
14:('Blackadar?s mixing length scale','m'), 
15:('Canopy conductance','m s-1'), 
16:('Minimal stomatal resistance','s m-1'), 
17:('Wilting point','Proportion'), 
18:('Solar parameter in canopy conductance','Proportion'), 
19:('Temperature parameter in canopy conductance','Proportion'), 
20:('Soil moisture parameter in canopy conductance','Proportion'), 
21:('Humidity parameter in canopy conductance','Proportion'), 
22:('Volumetric soil moisture','kg m-3'),
23:('Column integrated soil moisture','kg m-2'),
24:('Heat flux','W m-2'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][2][0].has_key(n): codetable[2][2][0][n]=('Reserved','')
for n in range(192,255):
    codetable[2][2][0][n] = ('Reserved for local use','')
# Parameter Category 3: Soil 
codetable[2][2][3] = {0:('Soil Type','code table (4.213)'),       
1:('Upper layer soil temperature','K'),
2:('Upper layer soil moisture','kg m-3'),
3:('Lower layer soil moisture','kg m-3'),
4:('Bottom layer soil temperature','K'),
5:('Liquid volumetric soil moisture (non-frozen)','Proportion'), 
6:('Number of soil layers in root zone','Numeric'), 
7:('Transpiration stress-onset (soil moisture)','Proportion'), 
8:('Direct evaporation cease (soil moisture)','Proportion'), 
9:('Soil porosity','Proportion'), 
255:('Missing','')}
for n in range(192):
    if not codetable[2][2][3].has_key(n): codetable[2][2][3][n]=('Reserved','')
for n in range(192,255):
    codetable[2][2][3][n] = ('Reserved for local use','')
# Product Discipline 3: Space products.
# Parameter Category 0: Image format products.
codetable[2][3][0] = {0:('Scaled radiance','numeric'),
1:('Scaled albedo','numeric'),
2:('Scaled brightness temperature','numeric'),
3:('Scaled precipitable water','numeric'),
4:('Scaled lifted index','numeric'),
5:('Scaled cloud top pressure','numeric'),
6:('Scaled skin temperature','numeric'),
7:('Cloud mask','Code table 4.217'),
8:('Pixel scene type','Code table 4.218'),
9:('Fire detection indicator','Code table 4.223'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][3][0].has_key(n): codetable[2][3][0][n]=('Reserved','')
for n in range(192,255):
    codetable[2][3][0][n] = ('Reserved for local use','')
# Parameter Category 1: Quantitative products.
codetable[2][3][1] = {0:('Estimated precipitation','kg m-2'),
1:('Instantaneous rain rate','kg m-2 s-1'), 
2:('Cloud top height','m'), 
3:('Cloud top height quality indicator','Code table 4.219'), 
4:('Estimated u component of wind','m s-1'), 
5:('Estimated v component of wind','m s'),
6:('Number of pixels used','Numeric'),
7:('Solar zenith angle','degrees'),
8:('Relative azimuth angle','degrees'),
9:('Reflectance in 0.6 micron channel','percent'),
10:('Reflectance in 0.8 micron channel','percent'),
11:('Reflectance in 1.6 micron channel','percent'),
12:('Reflectance in 3.9 micron channel','percent'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][3][1].has_key(n): codetable[2][3][1][n]=('Reserved','')
for n in range(192,255):
    codetable[2][3][1][n] = ('Reserved for local use','')
# Product Discipline 10: Oceanographic products.
# Parameter Category 0: Waves. 
codetable[2][10][0] = {0:('Wave spectra (1)',''),
 1:('Wave spectra (2)',''), 
 2:('Wave spectra (3)',''),
 3:('Significant height of combined wind waves and swell','m'),
 4:('Direction of wind waves','Degree true'),
 5:('Significant height of wind waves','m'),
 6:('Mean period of wind waves','s'),
 7:('Direction of swell waves','Degree true'),
 8:('Significant height of swell waves','m'),
 9:('Mean period of swell waves','s'),
10:('Primary wave direction','Degree true'),
11:('Primary wave mean period','s'),
12:('Secondary wave direction','Degree true'),
13:('Secondary wave mean period','s'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][10][0].has_key(n): codetable[2][10][0][n]=('Reserved','')
for n in range(192,255):
    codetable[2][10][0][n] = ('Reserved for local use','')
# Parameter Category 1: Currents 
codetable[2][10][1] = {0:('Current direction','Degree true'), 
1:('Current speed','m s-1'),
2:('u-component of current','m s-1'),
3:('v-component of current','m s-1'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][10][1].has_key(n): codetable[2][10][1][n]=('Reserved','')
for n in range(192,255):
    codetable[2][10][1][n] = ('Reserved for local use','')
# Parameter Category 2: Ice 
codetable[2][10][2] = {0:('Ice cover','Proportion'), 
1:('Ice thickness','m'),
2:('Direction of ice drift','Degree true'),
3:('Speed of ice drift','m s-1'),
4:('u-component of ice drift','m s-1'),
5:('v-component of ice drift','m s-1'),
6:('Ice growth rate','m s-1'),
7:('Ice divergence','s-1'),
8:('Ice temperature','K'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][10][2].has_key(n): codetable[2][10][2][n]=('Reserved','')
for n in range(192,255):
    codetable[2][10][2][n] = ('Reserved for local use','')
# Parameter Category 3: Surface Properties 
codetable[2][10][3] = {0:('Water temperature','K'), 
1:('Deviation of sea level from mean','m'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][10][3].has_key(n): codetable[2][10][3][n]=('Reserved','')
for n in range(192,255):
    codetable[2][10][3][n] = ('Reserved for local use','') 
# Parameter Category 4: Sub-surface Properties 
codetable[2][10][4] = {0:('Main thermocline depth','m'), 
1:('Main thermocline anomaly','m'),
2:('Transient thermocline depth','m'),
3:('Salinity','kg kg-1'),
255:('Missing','')}
for n in range(192):
    if not codetable[2][10][4].has_key(n): codetable[2][10][4][n]=('Reserved','')
for n in range(192,255):
    codetable[2][10][4][n] = ('Reserved for local use','')
# Code table 4.3: Type of generating process 
codetable[3]={0:'Analysis', 
1:'Initialization',
2:'Forecast', 
3:'Bias corrected forecast', 
4:'Ensemble forecast', 
5:'Probability forecast', 
6:'Forecast error', 
7:'Analysis error', 
8:'Observation', 
255:'Missing'}
for n in range(192):
    if not codetable[3].has_key(n): codetable[3][n]=('Reserved','')
for n in range(192,255):
    codetable[3][n] = ('Reserved for local use','') 
# Code Table 4.4: Indicator of unit of time range
codetable[4]={0:'Minute', 
 1:'Hour',
 2:'Day',
 3:'Month',
 4:'Year', 
 5:'Decade (10 years)',
 6:'Normal (30 years)',
 7:'Century (100 years)',
10:'3 hours',
11:'6 hours',
12:'12 hours',
13:'Second',
255:'Missing'}
for n in range(192):
    if not codetable[4].has_key(n): codetable[4][n]=('Reserved','')
for n in range(192,255):
    codetable[4][n] = ('Reserved for local use','')  
# Code table 4.5: Fixed surface types and units     
codetable[5]={0:('Reserved',''),
  1:('Ground or water surface',''),
  2:('Cloud base level',''),
  3:('Level of cloud tops',''),
  4:('Level of 0 deg C isotherm',''),
  5:('Level of adiabatic condensation lifted from the surface',''),
  6:('Maximum wind level',''),
  7:('Tropopause',''),
  8:('Nominal top of the atmosphere',''),
  9:('Sea bottom',''),
 20:('Isothermal level','K'),
100:('Isobaric surface','Pa'),
101:('Mean sea level',''), 
102:('Specific altitude above mean sea level','m'),
103:('Specified height level above ground','m'),
104:('Sigma level','sigma value'),
105:('Hybrid level',''),
106:('Depth below land surface','m'),
107:('Isentropic (theta) level','K'),
108:('Level at specified pressure difference from ground to level','Pa'),
109:('Potential vorticity surface','K m2  kg-1 s-1'),
111:('Eta level',''),
117:('Mixed layer depth','m'),
160:('Depth below sea level','m'),
255:('Missing','')}
for n in range(192):
    if not codetable[5].has_key(n): codetable[5][n]=('Reserved','')
for n in range(192,255):
    codetable[5][n] = ('Reserved for local use','')
# Code Table 4.6: Type of ensemble forecast 
codetable[6]={0:'Unperturbed high-resolution control forecast', 
1:'Unperturbed low-resolution control forecast',
2:'Negatively perturbed forecast',
3:'Positively perturbed forecast',
255:('Missing','')}
for n in range(192):
    if not codetable[6].has_key(n): codetable[6][n]='Reserved'
for n in range(192,255):
    codetable[6][n] = 'Reserved for local use'
# Code Table 4.7: Derived forecast 
codetable[7]={0:'Unweighted mean of all members', 
1:'Weighted mean of all members',
2:'Standard deviation with respect to cluster mean',
3:'Standard deviation with respect to cluster mean, normalized',
4:'Spread of all members',
5:'Large anomaly index of all members',
6:'Unweighted mean of the cluster members',
255:('Missing','')}
for n in range(192):
    if not codetable[7].has_key(n): codetable[7][n]=('Reserved','')
for n in range(192,255):
    codetable[7][n] = ('Reserved for local use','')
# Code Table 4.8: Clustering Method 
codetable[8]={0:'Anomaly correlation', 
1:'Root mean square',
255:('Missing','')}
for n in range(192):
    if not codetable[8].has_key(n): codetable[8][n]=('Reserved','')
for n in range(192,255):
    codetable[8][n] = ('Reserved for local use','')
# Code Table 4.9: Probability Type
codetable[9]={0:'Probability of event below lower limit',
1:'Probability of event above upper limit',
2:'Probability of event between lower and upper limits. The range includes the lower limit but not the upper limit.',
3:'Probability of event above lower limit',
4:'Probability of event below upper limit',
255:('Missing','')}
for n in range(192):
    if not codetable[9].has_key(n): codetable[9][n]=('Reserved','')
for n in range(192,255):
    codetable[9][n] = ('Reserved for local use','')
# Code Table 4.10: Type of statistical processing 
codetable[10]={0:'Average',
1:'Accumulation',
2:'Maximum',
3:'Minimum',
4:'Difference (Value at the end of time range minus value at the beginning)', 
5:'Root mean square',
6:'Standard deviation',
7:'Covariance (Temporal variance)',
8:'Difference (Value at the start of time range minus value at the end)',
9:'Ratio',
255:'Missing'}
for n in range(192):
    if not codetable[10].has_key(n): codetable[10][n]='Reserved'
for n in range(192,255):
    codetable[10][n] = 'Reserved for local use'
#Code Table 4.11: Type of time intervals
codetable[11]={1:'Successive times processed have same forecast time, start time of is incremented',
1:'Successive times processed have same forecast time, start time of forecast is incremented', 
2:'Successive times processed have same start time of forecast, forecast time is incremented', 
3:'Successive times processed have start time of forecast incremented and forecast time decremented so that valid time remains constant', 
4:'Successive times processed have start time of forecast decremented and forecast time incremented so that valid time remains constant',
5:'Floating subinterval of time between forecast time and end of overall time interval', 
255:'Missing'}
for n in range(192):
    if not codetable[11].has_key(n): codetable[11][n]='Reserved'
for n in range(192,255):
    codetable[11][n] = 'Reserved for local use'
# Code Table 4.205: Aerosol type  
codetable[205]={0:'Aerosol not present', 
1:'Aerosol present',
255:'Missing'}
for n in range(192):
    if not codetable[205].has_key(n): codetable[205][n]='Reserved'
for n in range(192,255):
    codetable[205][n] = 'Reserved for local use'
