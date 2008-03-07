__version__ = '20070615'
__doc__="""
Introduction
============

Python module for reading and writing GRIB edition 2 (GRIB2) files
(U{download<http://code.google.com/p/pygrib2/downloads/list>}). 
GRIB2 is the second version of the World Meterological Organization
(WMO) standard for distributing gridded data. The standard is
outlined in U{FM92 GRIB Edition 2, Code Form and Tables
<http://www.wmo.ch/pages/prog/www/WMOCodes/Operational/GRIB2/FM92-GRIB2-2007Nov.pdf>}. The module
includes a programmer interface for reading/writing GRIB2 grids as well as command
line utilities for listing the contents of a grib file and 're-packing' a
grib file using a different compression scheme.

Required
========

- U{Python<http://python.org>} 2.3 or higher.  
- U{numpy<http://sourceforge.net/project/showfiles.php?group_id=1369>}
  N-dimensional array object for python.
- U{pyproj<http://code.google.com/p/pyproj/>} Python interface to 
  U{PROJ.4<http://proj.maptools.org>} library for cartographic transformations.
  U{PROJ.4<http://proj.maptools.org>} library must be installed first.
- U{Jasper<http://www.ece.uvic.ca/~mdadams/jasper>} library. This library
  is a C implementation of the JPEG-2000 Part-1 standard (ISO/IEC 15444-1).
- U{PNG<http://www.libpng.org/pub/png/libpng.html>} library. This library
  is a C implementation of the Portable Network Graphics
  (PNG) image compression format. It's probably already on your system.
- U{zlib<http://www.gzip.org/zlib/>} compression library.
  It's almost certainly already on your system.

Installation
============

 - set the environment variables C{$JASPER_DIR}, C{$PNG_DIR} and 
 C{$ZLIB_DIR} so that the include files and libraries for jasper,
 png and zlib will be found.  For example, the include files for 
 jasper should be found in C{$JASPER_DIR/include}, and the jasper
 library should be found in C{$JASPER_DIR/lib}.

 - Run 'python setup.py install', as root if necessary.


Example usage
=============

 - from the python interpreter prompt, import the package::
    >>> from grib2 import Grib2Decode, dump
 - open a GRIB2 file, create a list of Grib2Message instances::
    >>> grbs = Grib2Decode('sampledata/gfs.grb')  
 - print an inventory of the file::
    >>> for grb in grbs:
    >>>     print grb 
    1:Geopotential height [gpm]:100000 Pa (Isobaric surface):72 Hour Forecast initialized 2004120912:Latitude/longitude:Unperturbed high-resolution control forecast member 0 of 10
    2:Geopotential height [gpm]:97500 Pa (Isobaric surface):72 Hour Forecast initialized 2004120912:Latitude/longitude:Unperturbed high-resolution control forecast member 0 of 10
    3:Geopotential height [gpm]:95000 Pa (Isobaric surface):72 Hour Forecast initialized 2004120912:Latitude/longitude:Unperturbed high-resolution control forecast member 0 of 10
  
       .....

 - find the first grib message containing 500 hPa geopotential height:: 
    >>> z500 = [g for g in grbs if g.parameter=='Geopotential height' and g.vertical_level=='50000 Pa' and g.vertical_level_descriptor=='Isobaric surface'][0]
 - extract the 500 hPa height data::
    >>> z500data = z500.data()
    >>> print z500.shape, z500data.min(), z500data.max()
    (73, 144) 4834.89990234 5931.20019531
 - get the latitudes and longitudes of the grid::
    >>> lats, lons = z500.grid()
    >>> print lats.shape, lats.min(), lats.max(), lons.shape, lons.min(), lons.max()
    (73, 144) -90.0 90.0 (73, 144) 0.0 357.5
 - dump just this grib message to another file::
    >>> dump('gfs_z500.grb',[z500])
 - read that file back in and verify it's contents::
    >>> grbs = Grib2Decode('gfs_z500.grb')
    >>> for g in grbs:
    >>>    print g
    1:Geopotential height [gpm]:50000 Pa (Isobaric surface):72 Hour Forecast initialized 2004120912:Latitude/longitude:Unperturbed high-resolution control forecast member 0 of 10

Documentation
=============

 - see below for python API documentation (L{Grib2Decode}, L{Grib2Encode},
   L{Grib2Message}, L{dump}).
  
Links
=====

 - U{WMO GRIB information<http://www.wmo.ch/pages/prog/www/WMOCodes/GRIB.html>}.
 - U{wgrib2<http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/>}
 - U{NCEP GRIB2 C and FORTRAN libraries
   <http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2/>}. This package uses
   C routines from g2clib.  
 - U{ECMWF gribAPI<http://www.ecmwf.int/products/data/software/grib2.html>}
 - U{MDL GRIB2 Decoder<http://weather.gov/mdl/iwt/grib2/decoder.htm>}
 - U{Pyrex<http://nz.cosc.canterbury.ac.nz/~greg/python/Pyrex/>}
 (used to create python interface to g2clib and proj4).
 - U{proj.4<http://proj.maptools.org>} (used to perform cartographic
 transformations).

Changelog
=========

 - B{20041213}: initial release. Fully supports lat/lon, gaussian, lambert
   conformal, polar stereographic and mercator grids.  Includes all
   product (section 4) tables included in the 20031105 version of the WMO
   GRIB2 document. Works with every GRIB2 file I could find -
   if you find one it has trouble with please let me know.
 - B{20041215}: Fixed to handle files with 'communications headers' at
   beginning of GRIB message.
 - B{20041217}: Added C{matchrecs} class method to find GRIB records with
   matching gdtnum, pdtnum, idsect, gdtmpl or pdtmpl values. Added example
   that reads an ETA grid and plots it with U{Matplotlib<http://matplotlib.sf.net/>}.
 - B{20050118}: Updated C code to g2clib-1.0.2 (from 1.0.1).
 - B{20050316}: added a new class (L{Grib2Encode}) for encoding GRIB2 messages.
   Renamed Grib2 class L{Grib2Decode}. Additional options for rdgrib utility.
 - B{20050322}: bugfixes for L{Grib2Encode}.
   Added test script (test3.py) that exercises both Grib2Decode and Grib2Encode.
 - B{20050716}: Added some support for irregular grids (such as 
   ECMWF reduced gaussian grids). JPEG2000 and PNG support is now optional.
 - B{20050829}: getfld and getflds L{Grib2Decode} methods can
   now return masked arrays when there is a bitmap.
 - B{20050830}: Now displays more ensemble info in inventory.
 - B{20051121}: Now uses Numeric by default (no longer requires
   numarray).  Can easily be modified to use nummarray or Numeric by
   modifying the imports in 3 files (grib2.py, proj.py and gaussian.py).
   A new utility, gribrepack, is included for repacking a grib2 file
   with a different compression scheme.
 - B{20051125}: Updated grib2 tables to version 3 (released
   by WMO on Nov 2, 2005).
 - B{20060117}: Now uses numpy by default (instead of Numeric).
   Python 2.5 compatibility fixes.
 - B{20070130}: Fixes some bugs found by Rob Cermak.  Now
   requires pyproj be installed first (which in turn requires
   that you have the PROJ.4 C-library installed). Updated to g2clib 1.0.4.
 - B{20070428}: Fixed memory leaks with a patch provided
   by Thomas Natschlager.
 - B{20070501}: Included new parameters approved by WMO
   for operational implementation in November, 2007.
   These new parameters are used in the U{TIGGE
   <http://tigge.ecmwf.int/tigge/d/tigge/>} grib2 files, so now all TIGGE
   files should be interpreted correctly. 'Reduced' global gaussian grids
   (from ECMWF) are now expanded to full global gaussian grids automatically
   using linear interpolation.
 - B{20070503}: Now partially supports grid definition template 90 (space-view
   satellite projection). Can't yet handle case when sub-satellite point is off the
   equator and earth is specified as an oblate spheroid. Does work with EUMETSAT
   grib2 files.  Bug fix for Oblate Spheroid earth shape (major and minor
   radii are actually in km, not m).
 - B{20070515}: Totally revamped API for reading.  Now hosted on google code.
   Supports Albers equal area, and azimuthal equidistant projections, although
   these are untested since I couldn't find any grib files in the wild that use these.
   Some support for spectral data and rotated lat/lon and gaussian grids.
   Lots of bug fixes.
 - B{%(__version__)s}: Compatibility fix for python < 2.5, bug fixes.

@author: Jeffrey Whitaker.

@contact: U{Jeff Whitaker<mailto:jeffrey.s.whitaker@noaa.gov>}

@version: %(__version__)s

@copyright: copyright 2007 by Jeffrey Whitaker.

@license: Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
supporting documentation.
THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO
EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
""" % locals()
import g2lib
import sxn0, sxn3, sxn4
import struct
import gaussian
import string
import math

import numpy as N
from numpy import ma
from proj import Proj
import pyproj

def _dec2bin(val, maxbits = 8): 
    """ 
    A decimal to binary converter. Returns bits in a list. 
    """ 
    retval = [] 
    for i in range(maxbits - 1, -1, -1): 
        bit = int(val / (2 ** i)) 
        val = (val % (2 ** i)) 
        retval.append(bit) 
    return retval 

def _putieeeint(r):
    """convert a float to a IEEE format 32 bit integer"""
    ra = N.array([r],'f')
    ia = N.zeros(1,'i')
    g2lib.rtoi_ieee(ra,ia)
    return ia[0]

def _getieeeint(i):
    """convert an IEEE format 32 bit integer to a float"""
    ia = N.array([i],'i')
    ra = N.zeros(1,'f')
    g2lib.itor_ieee(ia,ra)
    return ra[0]

class Grib2Message:
    """
 Class for accessing data in a GRIB Edition 2 message.

 The L{Grib2Decode} function returns a list of these class instances,
 one for each grib message in the file.

 When a class instance is created, metadata in the GRIB2 file
 is decoded and used to set various instance variables.
 
 @ivar bitmap_indicator_flag: flag to indicate whether a bit-map is used (0 for yes, 255 for no).
 @ivar data_representation_template: data representation template  from section 5.
 @ivar data_representation_template_number: data representation template number from section 5.
 @ivar discipline: product discipline for grib message.
 @ivar discipline_code: product discipline code for grib message.
 @ivar earthRmajor: major (equatorial) earth radius.
 @ivar earthRminor: minor (polar) earth radius.
 @ivar ensemble_info: ensemble member information string.
 @ivar forecast_time: string describing forecast time.
 @ivar grid_definition_info: grid definition section information from section 3.
  See L{Grib2Encode.addgrid} for details.
 @ivar grid_definition_template: grid definition template from section 3.
 @ivar grid_definition_template_number: grid definition template number from section 3.
 @ivar gridlength_in_x_direction: x (or longitudinal) direction grid length.
 @ivar gridlength_in_y_direction: y (or latitudinal) direction grid length.
 @ivar identification_section: data from identification section (section 1).
  See L{Grib2Encode.__init__} for details.
 @ivar latitude_first_gridpoint: latitude of first grid point on grid.
 @ivar latitude_last_gridpoint: latitude of last grid point on grid.
 @ivar longitude_first_gridpoint: longitude of first grid point on grid.
 @ivar longitude_last_gridpoint: longitude of last grid point on grid.
 @ivar scanmodeflags: scanning mode flags from Table 3.4.

  - bit 1:

    0 - Points in the first row or column scan in the +i (+x) direction

    1 - Points in the first row or column scan in the +i (+x) direction

  - bit 2:

    0 - Points in the first row or column scan in the -j (-y) direction

    1 - Points in the first row or column scan in the +j (+y) direction

  - bit 3:

    0 - Adjacent points in the i (x) direction are consecutive (row-major order).

    1 - Adjacent points in the j (y) direction are consecutive (column-major order).

  - bit 4:

    0 - All rows scan in the same direction

    1 - Adjacent rows scan in the opposite direction

 @ivar number_of_data_points_to_unpack: total number of data points in grib message.
 @ivar parameter: string describing the variable in the grib message.
 @ivar parameter_category:  string describing the type of variable the grib message.
 @ivar parameter_category_code: variable category code.
 @ivar parameter_code: variable code.
 @ivar parameter_units: units of variable.
 @ivar points_in_x_direction: number of points in the x (longitudinal) direction.
 @ivar points_in_y_direction: number of points in the y (latitudinal) direction.
 @ivar product_definition_template: product definition template nfrom section 4.
 @ivar product_definition_template_name: product definition template name.
 @ivar product_definition_template_number: product definition template number from section 4.
 @ivar shape_of_earth: string describing the shape of the earth (e.g. 'Oblate Spheroid', 'Spheroid').
 @ivar type_of_grid: type of grid or map projection (e.g. 'regular lat/lon', 'Lambert Conformal').
 @ivar vertical_level: string describing vertical level ('50000 Pa', '10 m', etc).
 @ivar vertical_level_descriptor: string describing the type of vertical level 
 (e.g. 'Isobaric surface').
 @ivar spectral_truncation_parameters:  pentagonal truncation parameters that describe the 
 spherical harmonic truncation (only relevant for grid_definition_template_numbers 50-52).
 For triangular truncation, all three of these numbers are the same.
 @ivar latitude_of_southern_pole: the geographic latitude in degrees of the southern 
 pole of the coordinate system (for rotated lat/lon or gaussian grids).
 @ivar longitude_of_southern_pole: the geographic longitude in degrees of the southern 
 pole of the coordinate system (for rotated lat/lon or gaussian grids).
 @ivar angle_of_pole_rotation: The angle of rotation in degrees about the new 
 polar axis (measured clockwise when looking from the southern to the northern pole)
 of the coordinate system. For rotated lat/lon or gaussian grids.
 @ivar missing_value: primary missing value (for data_representation_template_numbers
 2 and 3).
 @ivar missing_value2: secondary missing value (for data_representation_template_numbers
 2 and 3).
 @ivar inventory: a summary string describing the contents of the grib message.
 The format is "_grib_message_number:parameter(parameter_units):vertical_level(vertical_level_descriptor):forecast_time:type_of_grid:ensemble_info".
 @ivar proj4_: instance variables with this prefix are used to set the map projection
 parameters for U{PROJ.4<http://proj.maptools.org>}. 
    """
    def __init__(self,**kwargs):
        """
 create a Grib2Decode class instance given a GRIB Edition 2 filename.
 
 (used by L{Grib2Decode} function - not directly called by user)
        """
        for k,v in kwargs.items():
            setattr(self,k,v)
        # set decoded, human-readable attributes.
        discipline = self.discipline_code
        pdtmpl = self.product_definition_template
        pdtnum = self.product_definition_template_number
        gdsinfo = self.grid_definition_info
        gdtnum = self.grid_definition_template_number
        gdtmpl = self.grid_definition_template
        identsect = self.identification_section
        self.discipline = _getdiscipline(discipline)
        self.product_definition_template_name = _getpdt(pdtnum)
        # parameter.
        paramname = _getparam(discipline,pdtmpl)
        self.parameter = paramname[0]
        if paramname[1] != '':
            self.parameter_units = paramname[1]
        self.parameter_category = _getparamcat(discipline,pdtmpl)
        self.parameter_category_code = pdtmpl[0]
        self.parameter_code = pdtmpl[1]
        # type of grid.
        if gdsinfo[2] == 0:
            self.type_of_grid = sxn3.codetable[1][gdtnum]
        else:
            self.type_of_grid = 'Quasi-regular '+sxn3.codetable[1][gdtnum]
        # time.
        yyyy,mm,dd,hh,min,ss = _getdate(identsect)
        if min == 0 and ss == 0:
            date = '%0.4i'%(yyyy)+'%0.2i'%(mm)+'%0.2i'%(dd)+'%0.2i'%(hh)
        elif ss == 0 and min:
            date = '%0.4i'%(yyyy)+'%0.2i'%(mm)+'%0.2i'%(dd)+'%0.2i'%(hh)+'%0.2i'%(min)
        else:
            date = '%0.4i'%(yyyy)+'%0.2i'%(mm)+'%0.2i'%(dd)+'%0.2i'%(hh)+'%0.2i'%(min)+'%0.2i'%(ss)
        if pdtnum == 8:
           ftime = _getftime(pdtnum,pdtmpl)
           ftimestring = string.lstrip(repr(ftime[2])+' '+ftime[3]+' '+ftime[4]+' from '+repr(ftime[0])+' '+ftime[1]+' Forecast initialized '+date)
        else: 
           try:
               ftime = _getftime(pdtnum,pdtmpl)
               ftimestring = string.lstrip(repr(ftime[0])+' '+ftime[1]+' Forecast initialized '+date)
           except:
               ftimestring=None
        if ftimestring is not None:
            self.forecast_time = ftimestring
        # vertical level.
        levinfo = _getvertlevel(pdtmpl)
        if levinfo[0] is not None:
            if len(levinfo) > 3:
                levs = '%g-%g '%(levinfo[0],levinfo[3])
            else:
                levs = '%g '%levinfo[0]
        else:
            levs = ''
        if levs+levinfo[1] != '':
            self.vertical_level = levs+levinfo[1]
        if levinfo[2] != '':
            self.vertical_level_descriptor = levinfo[2]
        # ensemble info.
        if pdtnum in [1,11]:
            ensname,pertnum,nmembers = _getensinfo(pdtnum,pdtmpl)
            self.ensemble_info = ensname+' member '+repr(pertnum)+' of '+repr(nmembers)
        elif pdtnum in [2,12]:
            ensname,pertnum,nmembers = _getensinfo(pdtnum,pdtmpl)
            self.ensemble_info = ensname+' from a '+repr(nmembers)+' member ensemble'
        # shape of the earth.
        if gdtnum not in [50,51,52,1200]:
            earthR = sxn3.codetable[2][gdtmpl[0]]
            if earthR == 'Reserved': earthR = None
        else:
            earthR = None
        if _isString(earthR) and (earthR.startswith('Reserved') or earthR=='Missing'):
            self.shape_of_earth = earthR
            self.earthRminor = None
            self.earthRmajor = None
        elif _isString(earthR) and earthR.startswith('Spherical'):
            self.shape_of_earth = earthR
            scaledearthR = gdtmpl[2]
            earthRscale = gdtmpl[1]
            self.earthRmajor = math.pow(10,-earthRscale)*scaledearthR
            self.earthRminor = self.earthRmajor
        elif _isString(earthR) and earthR.startswith('OblateSpheroid'):
            self.shape_of_earth = earthR
            scaledearthRmajor = gdtmpl[4]
            earthRmajorscale = gdtmpl[3]
            self.earthRmajor = math.pow(10,-earthRmajorscale)*scaledearthRmajor
            self.earthRmajor = self.earthRmajor*1000. # convert to m from km
            scaledearthRminor = gdtmpl[6]
            earthRminorscale = gdtmpl[5]
            self.earthRminor = math.pow(10,-earthRminorscale)*scaledearthRminor
            self.earthRminor = self.earthRminor*1000. # convert to m from km
        elif _isString(earthR) and earthR.startswith('WGS84'):
            self.shape_of_earth = earthR
            self.earthRmajor = 6378137.0
            self.earthRminor = 6356752.3142
        elif isinstance(earthR,tuple):
            self.shape_of_earth = 'OblateSpheroid'
            self.earthRmajor = earthR[0]
            self.earthRminor = earthR[1]
        else: 
            if earthR is not None:
                self.shape_of_earth = 'Spherical'
                self.earthRmajor = earthR
                self.earthRminor = self.earthRmajor
        # grid information
        reggrid = gdsinfo[2] == 0 # gdsinfo[2]=0 means regular 2-d grid
        if reggrid and gdtnum not in [50,51,52,53,100,120,1000,1200]:
            self.points_in_x_direction = gdtmpl[7]
            self.points_in_y_direction = gdtmpl[8]
        if not reggrid and gdtnum == 40: # 'reduced' gaussian grid.
            self.points_in_y_direction = gdtmpl[8]
        if gdtnum == 0 or gdtnum == 1: # regular lat/lon grid
            scalefact = float(gdtmpl[9])
            divisor = float(gdtmpl[10])
            if scalefact == 0: scalefact = 1.
            if divisor <= 0: divisor = 1.e6
            self.latitude_first_gridpoint = scalefact*gdtmpl[11]/divisor
            self.longitude_first_gridpoint = scalefact*gdtmpl[12]/divisor
            self.latitude_last_gridpoint = scalefact*gdtmpl[14]/divisor
            self.longitude_last_gridpoint = scalefact*gdtmpl[15]/divisor
            self.gridlength_in_x_direction = scalefact*gdtmpl[16]/divisor
            self.gridlength_in_y_direction = scalefact*gdtmpl[17]/divisor
            if self.latitude_first_gridpoint > self.latitude_last_gridpoint:
                self.gridlength_in_y_direction = -self.gridlength_in_y_direction
            if self.longitude_first_gridpoint > self.longitude_last_gridpoint:
                self.gridlength_in_x_direction = -self.gridlength_in_x_direction
            self.scanmodeflags = _dec2bin(gdtmpl[18])[0:4]
            if gdtnum == 1:
                self.latitude_of_southern_pole = scalefact*gdtmpl[19]/divisor
                self.longitude_of_southern_pole = scalefact*gdtmpl[20]/divisor
                self.angle_of_pole_rotation = gdtmpl[21]
        elif gdtnum == 10: # mercator
            self.latitude_first_gridpoint = gdtmpl[9]/1.e6
            self.longitude_first_gridpoint = gdtmpl[10]/1.e6
            self.latitude_last_gridpoint = gdtmpl[13]/1.e6
            self.longitude_last_gridpoint = gdtmpl[14]/1.e6
            self.gridlength_in_x_direction = gdtmpl[17]/1.e3
            self.gridlength_in_y_direction= gdtmpl[18]/1.e3
            self.proj4_lat_ts = gdtmpl[12]/1.e6
            self.proj4_lon_0 = 0.5*(self.longitude_first_gridpoint+self.longitude_last_gridpoint)
            self.proj4_proj = 'merc'
            self.scanmodeflags = _dec2bin(gdtmpl[15])[0:4]
        elif gdtnum == 20: # stereographic
            projflag = _dec2bin(gdtmpl[16])[0]
            self.latitude_first_gridpoint = gdtmpl[9]/1.e6
            self.longitude_first_gridpoint = gdtmpl[10]/1.e6
            self.proj4_lat_ts = gdtmpl[12]/1.e6
            if projflag == 0:
                self.proj4_lat_0 = 90
            elif projflag == 1:
                self.proj4_lat_0 = -90
            else:
                raise ValueError,'Invalid projection center flag = %s' % projflag
            self.proj4_lon_0 = gdtmpl[13]/1.e6
            self.gridlength_in_x_direction = gdtmpl[14]/1000.
            self.gridlength_in_y_direction = gdtmpl[15]/1000.
            self.proj4_proj = 'stere'
            self.scanmodeflags = _dec2bin(gdtmpl[17])[0:4]
        elif gdtnum == 30: # lambert conformal
            self.latitude_first_gridpoint = gdtmpl[9]/1.e6
            self.longitude_first_gridpoint = gdtmpl[10]/1.e6
            self.gridlength_in_x_direction = gdtmpl[14]/1000.
            self.gridlength_in_y_direction = gdtmpl[15]/1000.
            self.proj4_lat_1 = gdtmpl[18]/1.e6
            self.proj4_lat_2 = gdtmpl[19]/1.e6
            self.proj4_lat_0 = gdtmpl[12]/1.e6
            self.proj4_lon_0 = gdtmpl[13]/1.e6
            self.proj4_proj = 'lcc'
            self.scanmodeflags = _dec2bin(gdtmpl[17])[0:4]
        elif gdtnum == 31: # albers equal area.
            self.latitude_first_gridpoint = gdtmpl[9]/1.e6
            self.longitude_first_gridpoint = gdtmpl[10]/1.e6
            self.gridlength_in_x_direction = gdtmpl[14]/1000.
            self.gridlength_in_y_direction = gdtmpl[15]/1000.
            self.proj4_lat_1 = gdtmpl[18]/1.e6
            self.proj4_lat_2 = gdtmpl[19]/1.e6
            self.proj4_lat_0 = gdtmpl[12]/1.e6
            self.proj4_lon_0 = gdtmpl[13]/1.e6
            self.proj4_proj = 'aea'
            self.scanmodeflags = _dec2bin(gdtmpl[17])[0:4]
        elif gdtnum == 40 or gdtnum == 41: # gaussian grid.
            scalefact = float(gdtmpl[9])
            divisor = float(gdtmpl[10])
            if scalefact == 0: scalefact = 1.
            if divisor <= 0: divisor = 1.e6
            self.points_between_pole_and_equator = gdtmpl[17]
            self.latitude_first_gridpoint = scalefact*gdtmpl[11]/divisor
            self.longitude_first_gridpoint = scalefact*gdtmpl[12]/divisor
            self.latitude_last_gridpoint = scalefact*gdtmpl[14]/divisor
            self.longitude_last_gridpoint = scalefact*gdtmpl[15]/divisor
            if reggrid:
                self.gridlength_in_x_direction = scalefact*gdtmpl[16]/divisor
                if self.longitude_first_gridpoint > self.longitude_last_gridpoint:
                    self.gridlength_in_x_direction = -self.gridlength_in_x_direction
            self.scanmodeflags = _dec2bin(gdtmpl[18])[0:4]
            if gdtnum == 41:
                self.latitude_of_southern_pole = scalefact*gdtmpl[19]/divisor
                self.longitude_of_southern_pole = scalefact*gdtmpl[20]/divisor
                self.angle_of_pole_rotation = gdtmpl[21]
        elif gdtnum == 50: # spectral coefficients.
            self.spectral_truncation_parameters = (gdtmpl[0],gdtmpl[1],gdtmpl[2])
            self.scanmodeflags = [None,None,None,None] # doesn't apply
        elif gdtnum == 90: # near-sided vertical perspective satellite projection
            self.proj4_lat_0 = gdtmpl[9]/1.e6
            self.proj4_lon_0 = gdtmpl[10]/1.e6
            self.proj4_h = self.earthRmajor * (gdtmpl[18]/1.e6)
            dx = gdtmpl[12]
            dy = gdtmpl[13]
            if self.proj4_lat_0 == 0.:
                self.proj4_proj = 'geos'
                self.proj4_h = self.proj4_h - self.earthRmajor
                self.gridlength_in_x_direction = 2.*self.earthRmajor/dx
                self.gridlength_in_y_direction = 2.*self.earthRminor/dy
            elif self.earthRmajor != self.earthRminor:
                self.proj4_proj = 'npers'
                self.gridlength_in_x_direction = 2.*self.earthRmajor/dx
                self.gridlength_in_y_direction = 2.*self.earthRmajor/dy
            self.scanmodeflags = _dec2bin(gdtmpl[16])[0:4]
        elif gdtnum == 110: # azimuthal equidistant.
            self.proj4_lat_0 = gdtmpl[9]/1.e6
            self.proj4_lon_0 = gdtmpl[10]/1.e6
            self.gridlength_in_x_direction = gdtmpl[12]/1000.
            self.gridlength_in_y_direction = gdtmpl[13]/1000.
            self.proj4_proj = 'aeqd'
            self.scanmodeflags = _dec2bin(gdtmpl[15])[0:4]
        elif gdtnum == 204: # curvilinear orthogonal
            self.scanmodeflags = _dec2bin(gdtmpl[18])[0:4]
        # missing value.
        drtnum = self.data_representation_template_number
        drtmpl = self.data_representation_template
        if (drtnum == 2 or drtnum == 3) and drtmpl[6] != 0:
            self.missing_value = _getieeeint(drtmpl[7]) 
            if drtmpl[6] == 2:
                self.missing_value2 = _getieeeint(drtmpl[8]) 
        # inventory string.
        if not hasattr(self,'parameter_units') or self.parameter_units=='':
            paramstring = self.parameter
        else:
            paramstring = self.parameter+' ['+self.parameter_units+']'
        if hasattr(self,'forecast_time'):
            fcsttimestring = self.forecast_time
        else:
            fcsttimestring = ''
        if hasattr(self,'vertical_level') and self.vertical_level_descriptor != '':
            levstring = string.lstrip(self.vertical_level+' ('+self.vertical_level_descriptor+')')
        else:
            if hasattr(self,'vertical_level_descriptor'):
                levstring = self.vertical_level_descriptor
            else:
                levstring = ''
        if hasattr(self,'ensemble_info'):
            ensstring = self.ensemble_info
        else:
            ensstring = ''
        self.inventory = repr(self._grib_message_number)+':'+paramstring+':'+levstring+':'+fcsttimestring+':'+self.type_of_grid+':'+ensstring

    def __repr__(self):
        """print a summary string describiing the contents of the GRIB2 message"""
        return self.inventory
        
    def data(self,fill_value=1.e30,masked_array=False,expand=True,order=None):
        """
 returns an unpacked data grid.
 
 @keyword fill_value: missing or masked data is filled with this value
 (default 1.e30).
 @keyword masked_array: if True, return masked array if there is bitmap
 for missing or masked data (default False).
 @keyword expand:  if True (default), ECMWF 'reduced' gaussian grids are
 expanded to regular gaussian grids.
 @keyword order: if 1, linear interpolation is used for expanding reduced
 gaussian grids.  if 0, nearest neighbor interpolation is used. Default 
 is 0 if grid has missing or bitmapped values, 1 otherwise.
 
 @return: C{B{data}}, a float32 numpy regular or masked array
 with shape (nlats,lons) containing the request grid.
        """
        # make sure scan mode is supported.
        # if there is no 'scanmodeflags', then grid is not supported.
        if not hasattr(self,'scanmodeflags'):
            raise ValueError('unsupported grid definition template number %s'%self.grid_definition_template_number)
        else:
            if self.scanmodeflags[2]:
                storageorder='F'
            else:
                storageorder='C'
        bitmapflag = self.bitmap_indicator_flag
        drtnum = self.data_representation_template_number
        drtmpl = self.data_representation_template
        # default order=0 is missing values or bitmap exists.
        if order is None:
            if ((drtnum == 3 or drtnum == 2) and drtmpl[6] != 0) or bitmapflag == 0:
                order = 0
            else:
                order = 1
        f = open(self._grib_filename,'rb')
        f.seek(self._grib_message_byteoffset)
        gribmsg = f.read(self._grib_message_length)
        f.close()
        gdtnum = self.grid_definition_template_number
        gdtmpl = self.grid_definition_template
        ndpts = self.number_of_data_points_to_unpack
        gdsinfo = self.grid_definition_info
        ngrdpts = gdsinfo[1]
        ipos = self._section7_byte_offset
        fld1=g2lib.unpack7(gribmsg,gdtnum,gdtmpl,drtnum,drtmpl,ndpts,ipos,N.zeros,storageorder=storageorder)
        # apply bitmap.
        if bitmapflag == 0:
            bitmap=self._bitmap
            fld = fill_value*N.ones(ngrdpts,'f')
            N.put(fld,N.nonzero(bitmap),fld1)
            if masked_array:
                fld = ma.masked_values(fld,fill_value)
        # missing values instead of bitmap
        elif masked_array and hasattr(self,'missing_value'):
            if hasattr(self, 'missing_value2'):
                mask = N.logical_or(fld1 == self.missing_value, fld1 == self.missing_value2)
            else:
                mask = fld1 == self.missing_value
            fld = ma.array(fld1,mask=mask)
        else:
            fld = fld1
        nx = None; ny = None
        if hasattr(self,'points_in_x_direction'):
            nx = self.points_in_x_direction
        if hasattr(self,'points_in_y_direction'):
            ny = self.points_in_y_direction
        if nx is not None and ny is not None: # rectangular grid.
            if hasattr(fld,'mask'):
                fld = ma.reshape(fld,(ny,nx))
            else:
                fld = N.reshape(fld,(ny,nx))
        else:
            if gdsinfo[2] and gdtnum == 40: # ECMWF 'reduced' global gaussian grid.
                if expand: 
                    nx = 2*ny
                    lonsperlat = self.grid_definition_list
                    if hasattr(fld,'mask'):
                        fld = ma.filled(fld)
                        fld = g2lib._redtoreg(nx, lonsperlat, fld, N.zeros, order=order)
                        fld = ma.masked_values(fld,fill_value)
                    else:
                        fld = g2lib._redtoreg(nx, lonsperlat, fld, N.zeros,order=order)
        # adjacent rows scan in opposite direction.
        # (flip every other row)
        if self.scanmodeflags[3]:
            fldsave = fld.astype('f') # casting makes a copy
            fld[1::2,:] = fldsave[1::2,::-1]
        return fld

    def grid(self):
        """
 return lats,lons (in degrees) of grid.
 currently can handle reg. lat/lon, global gaussian, mercator, stereographic,
 lambert conformal, albers equal-area, space-view and azimuthal 
 equidistant grids.

 @return: C{B{lats},B{lons}}, float32 numpy arrays 
 containing latitudes and longitudes of grid (in degrees).
        """
        gdsinfo = self.grid_definition_info
        gdtnum = self.grid_definition_template_number
        gdtmpl = self.grid_definition_template
        reggrid = gdsinfo[2] == 0 # gdsinfo[2]=0 means regular 2-d grid
        projparams = {}
        projparams['a']=self.earthRmajor
        projparams['b']=self.earthRminor
        if gdtnum == 0: # regular lat/lon grid
            lon1, lat1 = self.longitude_first_gridpoint, self.latitude_first_gridpoint
            lon2, lat2 = self.longitude_last_gridpoint, self.latitude_last_gridpoint
            delon = self.gridlength_in_x_direction
            delat = self.gridlength_in_y_direction
            lats = N.arange(lat1,lat2+delat,delat)
            lons = N.arange(lon1,lon2+delon,delon)
            lons,lats = _meshgrid(lons,lats) # make 2-d arrays.
        elif gdtnum == 40: # gaussian grid (only works for global!)
            lon1, lat1 = self.longitude_first_gridpoint, self.latitude_first_gridpoint
            lon2, lat2 = self.longitude_last_gridpoint, self.latitude_last_gridpoint
            nlats = self.points_in_y_direction
            if not reggrid: # ECMWF 'reduced' gaussian grid.
                nlons = 2*nlats
                delon = 360./nlons
            else:
                nlons = self.points_in_x_direction
                delon = self.gridlength_in_x_direction
            lons = N.arange(lon1,lon2+delon,delon)
            # compute gaussian lats (north to south)
            lats = gaussian.lats(nlats)
            if lat1 < lat2:  # reverse them if necessary
                lats = lats[::-1]
            lons,lats = _meshgrid(lons,lats) # make 2-d arrays
        # mercator, lambert conformal, stereographic, albers equal area, azimuthal equidistant
        elif gdtnum in [10,20,30,31,110]:
            nx = self.points_in_x_direction
            ny = self.points_in_y_direction
            dx = self.gridlength_in_x_direction
            dy = self.gridlength_in_y_direction
            lon1, lat1 = self.longitude_first_gridpoint, self.latitude_first_gridpoint
            if gdtnum == 10: # mercator.
                lon2, lat2 = self.longitude_last_gridpoint, self.latitude_last_gridpoint
                projparams['lat_ts']=self.proj4_lat_ts
                projparams['proj']=self.proj4_proj
                projparams['lon_0']=self.proj4_lon_0
                pj = Proj(projparams,lon1,lat1,lon2,lat2)
            elif gdtnum == 20:  # stereographic
                projparams['lat_ts']=self.proj4_lat_ts
                projparams['proj']=self.proj4_proj
                projparams['lat_0']=self.proj4_lat_0
                projparams['lon_0']=self.proj4_lon_0
                pj = Proj(projparams,lon1,lat1,(nx-1)*dx,(ny-1)*dy,urcrnrislatlon=False)
            elif gdtnum in [30,31]: # lambert, albers
                projparams['lat_1']=self.proj4_lat_1
                projparams['lat_2']=self.proj4_lat_2
                projparams['proj']=self.proj4_proj
                projparams['lon_0']=self.proj4_lon_0
                pj = Proj(projparams,lon1,lat1,(nx-1)*dx,(ny-1)*dy,urcrnrislatlon=False)
            elif gdtnum == 110: # azimuthal equidistant
                projparams['proj']=self.proj4_proj
                projparams['lat_0']=self.proj4_lat_0
                projparams['lon_0']=self.proj4_lon_0
                pj = Proj(projparams,lon1,lat1,(nx-1)*dx,(ny-1)*dy,urcrnrislatlon=False)
            lons, lats = pj.makegrid(nx,ny)
        elif gdtnum == 90: # satellite projection.
            nx = self.points_in_x_direction
            ny = self.points_in_y_direction
            dx = self.gridlength_in_x_direction
            dy = self.gridlength_in_y_direction
            projparams['proj']=self.proj4_proj
            projparams['lon_0']=self.proj4_lon_0
            projparams['lat_0']=self.proj4_lat_0
            projparams['h']=self.proj4_h
            pj = pyproj.Proj(projparams)
            x = dx*N.indices((ny,nx),'f')[1,:,:]
            x = x - 0.5*x.max()
            y = dy*N.indices((ny,nx),'f')[0,:,:]
            y = y - 0.5*y.max()
            lons, lats = pj(x,y,inverse=True)
            # set lons,lats to 1.e30 where undefined
            abslons = N.fabs(lons); abslats = N.fabs(lats)
            lons = N.where(abslons < 1.e20, lons, 1.e30)
            lats = N.where(abslats < 1.e20, lats, 1.e30)
        else:
            print '%s not supported' % self.type_of_grid
            return None, None
        return lats.astype('f'), lons.astype('f')

def Grib2Decode(filename):
    """
 Read the contents of a GRIB2 file.

 @param filename: name of GRIB2 file.

 @return:  a list of L{Grib2Message} instances representing all of the
 grib messages in the file.  Messages with multiple fields are split 
 into separate messages (so that each L{Grib2Message} instance contains
 just one data field). The metadata in each GRIB2 message can be
 accessed via L{Grib2Message} instance variables, the actual data 
 can be read using L{Grib2Message.data}, and the lat/lon values of the grid
 can be accesses using L{Grib2Message.grid}.
    """
    f = open(filename,'rb')
    nmsg = 0
    # loop over grib messages, read section 0, get entire grib message.
    disciplines = []
    startingpos = []
    msglen = []
    while 1:
        # find next occurence of string 'GRIB' (or EOF).
        nbyte = f.tell()
        while 1:
            f.seek(nbyte)
            start = f.read(4)
            if start == '' or start == 'GRIB': break
            nbyte = nbyte + 1
        if start == '': break # at EOF
        # otherwise, start (='GRIB') contains indicator message (section 0)
        startpos = f.tell()-4
        f.seek(2,1)  # next two octets are reserved
        # get discipline info.
        disciplines.append(struct.unpack('>B',f.read(1))[0])
        # check to see it's a grib edition 2 file.
        vers = struct.unpack('>B',f.read(1))[0]
        if vers != 2: 
            raise IOError, 'not a GRIB2 file (version number %d)' % vers
        lengrib = struct.unpack('>q',f.read(8))[0]
        msglen.append(lengrib)
        startingpos.append(startpos)
        # read in entire grib message.
        f.seek(startpos)
        gribmsg = f.read(lengrib)
        # make sure the message ends with '7777'
        end = gribmsg[-4:lengrib]
        if end != '7777':
           raise IOError, 'partial GRIB message (no "7777" at end)'
        # do next message.
        nmsg=nmsg+1
    # if no grib messages found, nmsg is still 0 and it's not GRIB.
    if nmsg==0:
       raise IOError, 'not a GRIB file'
    # now for each grib message, find number of fields.
    numfields = []
    f.seek(0) # rewind file.
    for n in range(nmsg):
        f.seek(startingpos[n])
        gribmsg = f.read(msglen[n])
        pos = 0
        numflds = 0
        while 1:
            if gribmsg[pos:pos+4] == 'GRIB':
                sectnum = 0
                lensect = 16
            elif gribmsg[pos:pos+4] == '7777':
                break
            else:
                lensect = struct.unpack('>i',gribmsg[pos:pos+4])[0]
                sectnum = struct.unpack('>B',gribmsg[pos+4])[0]
                if sectnum == 4: numflds=numflds+1
                #if sectnum == 2: numlocal=numlocal+1
            pos = pos + lensect
            #print sectnum,lensect,pos
        #print n+1,len(gribmsg),numfields,numlocal
        numfields.append(numflds)
    # decode each section in grib message (sections 1 and above).
    gdtnum = [] # grid defn template number from sxn 3
    gdtmpl = [] # grid defn template from sxn 3
    gdeflist = [] # optional grid definition list from sxn 3
    gdsinfo = [] # grid definition section info from sxn3
    pdtmpl = [] # product defn template from sxn 4
    pdtnum = [] # product defn template number from sxn 4
    coordlist = [] # vertical coordinate info from sxn 4
    drtmpl = [] # data representation template from sxn 5
    drtnum = [] # data representation template number from sxn 5
    ndpts = [] # number of data points to be unpacked (from sxn 5)
    bitmapflag = [] # bit-map indicator flag from sxn 6
    bitmap = [] # bitmap from sxn 6.
    pos7 = [] # byte offset for section 7.
    msgstart = [] # byte offset in file for message start.
    msglength = [] # length of the message in bytes.
    message = [] # the actual grib message.
    identsect = [] # identification section (section 1).
    discipline = [] # discipline code.
    for n in range(nmsg):
        spos = startingpos[n]
        lengrib = msglen[n]
        #gribmsg = gribmsgs[n]
        f.seek(spos)
        gribmsg = f.read(lengrib)
        discipl = disciplines[n]
        lensect0 = 16
        # get length of section 1 and section number.
        #lensect1 = struct.unpack('>i',gribmsg[lensect0:lensect0+4])[0]
        #sectnum1 = struct.unpack('>B',gribmsg[lensect0+4])[0]
        #print 'sectnum1, lensect1 = ',sectnum1,lensect1
        # unpack section 1, octets 1-21 (13 parameters).  This section
        # can occur only once per grib message.
        #idsect,pos = _unpack1(gribmsg,lensect0) # python version
        idsect,pos = g2lib.unpack1(gribmsg,lensect0,N.zeros) # c version
        # loop over rest of sections in message.
        gdtnums = []
        gdtmpls = []
        gdeflists = []
        gdsinfos = []
        pdtmpls = []
        coordlists = []
        pdtnums = []
        drtmpls = []
        drtnums = []
        ndptslist = []
        bitmapflags = []
        bitmaps = []
        sxn7pos = []
        while 1:
            # check to see if this is the end of the message.
            if gribmsg[pos:pos+4] == '7777': break
            lensect = struct.unpack('>i',gribmsg[pos:pos+4])[0]
            sectnum = struct.unpack('>B',gribmsg[pos+4])[0]
            # section 2, local use section.
            if sectnum == 2:  # skip
                #localsxns.append(gribmsg[pos+5:pos+lensect-5])
                pos = pos + lensect
            # section 3, grid definition section.
            elif sectnum == 3:
                gds,gdtempl,deflist,pos = g2lib.unpack3(gribmsg,pos,N.zeros)
                gdtnums.append(gds[4])
                gdtmpls.append(gdtempl)
                gdeflists.append(deflist)
                gdsinfos.append(gds)
            # section, product definition section.
            elif sectnum == 4:
                pdtempl,pdtn,coordlst,pos = g2lib.unpack4(gribmsg,pos,N.zeros)
                pdtmpls.append(pdtempl)
                coordlists.append(coordlst)
                pdtnums.append(pdtn)
            # section 5, data representation section.
            elif sectnum == 5:
                drtempl,drtn,npts,pos = g2lib.unpack5(gribmsg,pos,N.zeros)
                drtmpls.append(drtempl)
                drtnums.append(drtn)
                ndptslist.append(npts)
            # section 6, bit-map section.
            elif sectnum == 6:
                bmap,bmapflag = g2lib.unpack6(gribmsg,gds[1],pos,N.zeros)
                #bitmapflag = struct.unpack('>B',gribmsg[pos+5])[0]
                if bmapflag == 0:
                    bitmaps.append(bmap.astype('b'))
                # use last defined bitmap.
                elif bmapflag == 254:
                    bmapflag = 0
                    for bmp in bitmaps[::-1]:
                        if bmp is not None: bitmaps.append(bmp)
                else:
                    bitmaps.append(None)
                bitmapflags.append(bmapflag)
                pos = pos + lensect
            # section 7, data section (nothing done here,
            # data unpacked when getfld method is invoked).
            else:
                if sectnum != 7:
                   msg = 'unknown section = %i' % sectnum
                   raise ValueError,msg
                sxn7pos.append(pos)
                pos = pos + lensect
        # extend by repeating last value for all remaining fields.
        gdtnum.append(_repeatlast(numfields[n],gdtnums))
        gdtmpl.append(_repeatlast(numfields[n],gdtmpls))
        gdeflist.append(_repeatlast(numfields[n],gdeflists))
        gdsinfo.append(_repeatlast(numfields[n],gdsinfos))
        pdtmpl.append(_repeatlast(numfields[n],pdtmpls))
        pdtnum.append(_repeatlast(numfields[n],pdtnums))
        coordlist.append(_repeatlast(numfields[n],coordlists))
        drtmpl.append(_repeatlast(numfields[n],drtmpls))
        drtnum.append(_repeatlast(numfields[n],drtnums))
        ndpts.append(_repeatlast(numfields[n],ndptslist))
        bitmapflag.append(_repeatlast(numfields[n],bitmapflags))
        bitmap.append(_repeatlast(numfields[n],bitmaps))
        pos7.append(_repeatlast(numfields[n],sxn7pos))
        msgstart.append(_repeatlast(numfields[n],[spos]))
        msglength.append(_repeatlast(numfields[n],[lengrib]))
        identsect.append(_repeatlast(numfields[n],[idsect]))
        discipline.append(_repeatlast(numfields[n],[discipl]))

    gdtnum = _flatten(numfields,gdtnum)
    gdtmpl = _flatten(numfields,gdtmpl)
    gdeflist = _flatten(numfields,gdeflist)
    gdsinfo = _flatten(numfields,gdsinfo)
    pdtmpl = _flatten(numfields,pdtmpl)
    pdtnum = _flatten(numfields,pdtnum)
    coordlist = _flatten(numfields,coordlist)
    drtmpl = _flatten(numfields,drtmpl)
    drtnum = _flatten(numfields,drtnum)
    ndpts = _flatten(numfields,ndpts)
    bitmapflag = _flatten(numfields,bitmapflag)
    bitmap = _flatten(numfields,bitmap)
    pos7 = _flatten(numfields,pos7)
    msgstart = _flatten(numfields,msgstart)
    msglength = _flatten(numfields,msglength)
    identsect = _flatten(numfields,identsect)
    discipline = _flatten(numfields,discipline)

    gribs = []
    for n in range(len(msgstart)):
        kwargs = {}
        kwargs['grid_definition_template_number']=gdtnum[n]
        kwargs['grid_definition_template']=gdtmpl[n]
        if gdeflist[n] != []:
            kwargs['grid_definition_list']=gdeflist[n]
        kwargs['grid_definition_info']=gdsinfo[n]
        kwargs['discipline_code']=discipline[n]
        kwargs['product_definition_template_number']=pdtnum[n]
        kwargs['product_definition_template']=pdtmpl[n]
        kwargs['data_representation_template_number']=drtnum[n]
        kwargs['data_representation_template']=drtmpl[n]
        if coordlist[n] != []:
            kwargs['extra_vertical_coordinate_info']=coordlist[n]
        kwargs['number_of_data_points_to_unpack']=ndpts[n]
        kwargs['bitmap_indicator_flag']=bitmapflag[n]
        if bitmap[n] is not []:
            kwargs['_bitmap']=bitmap[n]
        kwargs['_section7_byte_offset']=pos7[n]
        kwargs['_grib_message_byteoffset']=msgstart[n]
        kwargs['_grib_message_length']=msglength[n]
        kwargs['_grib_filename']=filename
        kwargs['identification_section']=identsect[n]
        kwargs['_grib_message_number']=n+1
        gribs.append(Grib2Message(**kwargs))
    f.close()
    return gribs 

def dump(filename, grbs):
    """
 write the given L{Grib2Message} instances to a grib file.
 
 @param filename: file to write grib data to.
 @param grbs: a list of L{Grib2Message} instances.
    """
    gribfile = open(filename,'wb')
    for grb in grbs:
        f = open(grb._grib_filename,'rb')
        f.seek(grb._grib_message_byteoffset)
        gribmsg = f.read(grb._grib_message_length)
        f.close()
        gribfile.write(gribmsg)
    gribfile.close() 

# private methods and functions below here.

def _getvertlevel(pdtmpl):
    """return vertical coordinate level info"""
    try:
        level1info = sxn4.codetable[5][pdtmpl[9]]
        scaledlevel1 = pdtmpl[11]
        level1scale = pdtmpl[10]
    except:
        scaledlevel1 = None
        level1scale = None
        level1info = ['','']
    if level1scale in [-127,255]: # either of these two values can indicate 'Missing'
        level1scale = None
    if scaledlevel1 in [2*(2**31-1),-(2**31-1)]: # ditto 
        scaledlevel1 = None
    if scaledlevel1 is not None and level1scale is not None:
        level1 = math.pow(10,level1scale)*scaledlevel1
    else:
        level1 = None
    if len(pdtmpl) >= 12 and pdtmpl[12] != 255:
       level2info = sxn4.codetable[5][pdtmpl[12]]
       scaledlevel2 = pdtmpl[14]
       level2scale = pdtmpl[13]
       level2 = math.pow(10,level2scale)*scaledlevel2
       return level1,level1info[1],level1info[0],level2,level2info[1],level2info[0]
    else:
       return level1,level1info[1],level1info[0]

def _getdate(idsect):
    """return yyyy,mm,dd,min,ss from section 1"""
    yyyy=idsect[5]
    mm=idsect[6]
    dd=idsect[7]
    hh=idsect[8]
    min=idsect[9]
    ss=idsect[10]
    return yyyy,mm,dd,hh,min,ss

def _getftime(pdtnum,pdtmpl):
    """return forecast time, units"""
    # assumes forecast time is eighth value in 
    # all product defn templates.
    time = pdtmpl[8]
    units = sxn4.codetable[4][pdtmpl[7]]
    if pdtnum == 8:
        stattype = pdtmpl[23]
        if stattype == 255:
            stattype = 'Period'
        else:
            stattype = sxn4.codetable[10][stattype]
        timeintervalunits = pdtmpl[25]
        timeintervalunits = sxn4.codetable[4][timeintervalunits]
        timeintervallen = pdtmpl[26]
        if timeintervalunits == 10:
            timelintervallen = timeintervallen*3
        elif timeintervalunits == 11:
            timeintervallen = timeintervallen*6
        elif timeintervalunits == 12:
            timeintervallen = timeintervallen*12
        return time,units,timeintervallen,timeintervalunits,stattype
    else:
        return time,units

def _getensinfo(pdtnum,pdtmpl):
    """return ensemble info (from pdts 4.1, 4.2, 4.11, 4.12)"""
    if pdtnum in [1,11]:
        enstype = sxn4.codetable[6][pdtmpl[15]]
        pertnum = pdtmpl[16]
        nmembers = pdtmpl[17]
        return enstype,pertnum,nmembers
    elif pdtnum in [2,12]:
        enstype = sxn4.codetable[7][pdtmpl[15]]
        nmembers = pdtmpl[16]
        return enstype,None,nmembers
    else:
        print 'not an ensemble product'
        return None,None,None

def _getdiscipline(discipline):
    """return descipline"""
    return sxn0.codetable[discipline] 

def _getpdt(pdtnum):
    """return name of product definition template"""
    return sxn4.codetable[0][pdtnum]

def _getparamcat(discipline,pdtmpl):
    """return parameter category description"""
    paramcat = pdtmpl[0]
    try:
        return sxn4.codetable[1][discipline][paramcat]
    except:
        return 'Unknown'

def _getparam(discipline,pdtmpl):
    """return parameter name, units"""
    # assumes parameter category and parameter number are first two in 
    # all product defn templates.
    paramcat = pdtmpl[0]
    try:
        sxn4.codetable[2][discipline][paramcat].has_key(pdtmpl[1]) 
        return sxn4.codetable[2][discipline][paramcat][pdtmpl[1]]
    except:
        return 'Unknown',''

def _unpack1(gribmsg,pos):
    """unpack section 1 given starting point in bytes
    used to test pyrex interface to g2_unpack1"""
    idsect = []
    pos = pos + 5
    idsect.append(struct.unpack('>h',gribmsg[pos:pos+2])[0])
    pos = pos + 2
    idsect.append(struct.unpack('>h',gribmsg[pos:pos+2])[0])
    pos = pos + 2
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    idsect.append(struct.unpack('>h',gribmsg[pos:pos+2])[0])
    pos = pos + 2
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    idsect.append(struct.unpack('>B',gribmsg[pos])[0])
    pos = pos + 1
    return N.array(idsect,'i'),pos

def _repeatlast(numfields,listin):
    """repeat last item in listin, until len(listin) = numfields"""
    if len(listin) < numfields:
        last = listin[-1]
        for n in range(len(listin),numfields):
            listin.append(last)
    return listin

def _flatten(numfields, listin):
   listout = []
   for n in xrange(len(listin)):
       for i in xrange(numfields[n]):
           listout.append(listin[n][i])
   return listout

def _isString(string):
    """Test if string is a string like object if not return 0 """
    try: string + ''
    except: return 0
    else: return 1

def _meshgrid(x, y):
    """
    For vectors x, y with lengths Nx=len(x) and Ny=len(y), return X, Y
    where X and Y are (Ny, Nx) shaped arrays with the elements of x
    and y repeated to fill the matrix
    """
    x = N.array(x)
    y = N.array(y)
    numRows, numCols = len(y), len(x)  # yes, reversed
    x.shape = 1, numCols
    X = N.repeat(x, numRows, 0)
    y.shape = numRows,1
    Y = N.repeat(y, numCols, 1)
    return X, Y

class Grib2Encode:
    """
 Class for encoding data into a GRIB2 message.
  - Creating a class instance (L{__init__}) initializes the message and adds 
    sections 0 and 1 (the indicator and identification sections), 
  - method L{addgrid} adds a grid definition (section 3) to the messsage.
  - method L{addfield} adds sections 4-7 to the message (the product
    definition, data representation, bitmap and data sections).
  - method L{end} adds the end section (section 8) and terminates the message.


 A GRIB Edition 2 message is a machine independent format for storing
 one or more gridded data fields.  Each GRIB2 message consists of the 
 following sections:
  - SECTION 0: Indicator Section - only one per message
  - SECTION 1: Identification Section - only one per message
  - SECTION 2: (Local Use Section) - optional                          
  - SECTION 3: Grid Definition Section                                
  - SECTION 4: Product Definition Section              
  - SECTION 5: Data Representation Section   
  - SECTION 6: Bit-map Section               
  - SECTION 7: Data Section                  
  - SECTION 8: End Section                   

 Sequences of GRIB sections 2 to 7, 3 to 7, or sections 4 to 7 may be repeated
 within a single GRIB message.  All sections within such repeated sequences
 must be present and shall appear in the numerical order noted above.
 Unrepeated sections remain in effect until redefined.

 Note:  Reading/writing section 2 (the 'local use section') is
 not yet supported.

 @ivar msg: A binary string containing the GRIB2 message.
 After the message has been terminated by calling
 the L{end} method, this string can be written to a file.
    """

    def __init__(self, discipline, idsect):
        """
 create a Grib2Enecode class instance given the GRIB2 discipline
 parameter and the identification section (sections 0 and 1).

 The GRIB2 message is stored as a binary string in instance variable L{msg}.

 L{addgrid}, L{addfield} and L{end} class methods must be called to complete
 the GRIB2 message.
 
 @param discipline:  Discipline or GRIB Master Table Number (Code Table 0.0).
 (0 for meteorlogical, 1 for hydrological, 2 for land surface, 3 for space,
 10 for oceanographic products).

 @param idsect:  Sequence containing identification section (section 1).
  - idsect[0]=Id of orginating centre (Common Code Table C-1) 
  - idsect[1]=Id of orginating sub-centre (local table) 
  - idsect[2]=GRIB Master Tables Version Number (Code Table 1.0) 
  - idsect[3]=GRIB Local Tables Version Number (Code Table 1.1) 
  - idsect[4]=Significance of Reference Time (Code Table 1.2) 
  - idsect[5]=Reference Time - Year (4 digits) 
  - idsect[6]=Reference Time - Month 
  - idsect[7]=Reference Time - Day 
  - idsect[8]=Reference Time - Hour 
  - idsect[9]=Reference Time - Minute 
  - idsect[10]=Reference Time - Second 
  - idsect[11]=Production status of data (Code Table 1.3) 
  - idsect[12]=Type of processed data (Code Table 1.4) 
        """
        self.msg,msglen=g2lib.grib2_create(N.array([discipline,2],'i'),N.array(idsect,'i'))

    def addgrid(self,gdsinfo,gdtmpl,deflist=None):
        """
 Add a grid definition section (section 3) to the GRIB2 message.

 @param gdsinfo: Sequence containing information needed for the grid definition section.
  - gdsinfo[0] = Source of grid definition (see Code Table 3.0) 
  - gdsinfo[1] = Number of grid points in the defined grid.
  - gdsinfo[2] = Number of octets needed for each additional grid points defn.
    Used to define number of points in each row for non-reg grids (=0 for 
    regular grid).
  - gdsinfo[3] = Interp. of list for optional points defn (Code Table 3.11)
  - gdsinfo[4] = Grid Definition Template Number (Code Table 3.1)

 @param gdtmpl: Contains the data values for the specified Grid Definition 
 Template ( NN=gds[4] ).  Each element of this integer  
 array contains an entry (in the order specified) of Grid 
 Definition Template 3.NN 

 @param deflist: (Used if gds[2] != 0)  Sequence containing the
 number of grid points contained in each row (or column) 
 of a non-regular grid.
        """
        if deflist is not None:
            dflist = N.array(deflist,'i')
        else:
            dflist = None
        self.msg,msglen=g2lib.grib2_addgrid(self.msg,N.array(gdsinfo,'i'),N.array(gdtmpl,'i'),dflist)

    def addfield(self,pdtnum,pdtmpl,drtnum,drtmpl,field,coordlist=None,bitmapflag=255,bitmap=None):
        """
 Add a product definition section, data representation section,
 bitmap section and data section to the GRIB2 message (sections 4-7).

 @param pdtnum: Product Definition Template Number (see Code Table 4.0)

 @param pdtmpl: Sequence with the data values for the specified Product Definition
 Template (N=pdtnum).  Each element of this integer 
 array contains an entry (in the order specified) of Product
 Definition Template 4.N

 @param drtnum: Data Representation Template Number (see Code Table 5.0).

 @param drtmpl: Sequence with the data values for the specified Data Representation
 Template (N=drtnum).  Each element of this integer 
 array contains an entry (in the order specified) of Data
 Representation Template 5.N
 Note that some values in this template (eg. reference
 values, number of bits, etc...) may be changed by the
 data packing algorithms.
 Use this to specify scaling factors and order of
 spatial differencing, if desired.

 @param field:  float32 numpy array of data points to pack.

 @param coordlist: Sequence containing floating point values intended to document
 the vertical discretization with model data
 on hybrid coordinate vertical levels. Default None.

 @param bitmapflag: Bitmap indicator (see Code Table 6.0) Default 255.
  - 0 = bitmap applies and is included in Section 6.
  - 1-253 = Predefined bitmap applies
  - 254 = Previously defined bitmap applies to this field
    (it still must be provided, it just won't
    be encoded into the message again)
  - 255 = Bit map does not apply to this product.

 @param bitmap: int32 numpy array containing bitmap to be added 
 (if bitmapflag=0 or 254). Default None.
        """
        fld = N.array(field.astype('f'),'f')
        if bitmap is not None:
            bmap = N.ravel(N.array(bitmap,'i'))
        else:
            bmap = None
        if coordlist is not None:
            crdlist = N.array(coordlist,'f')
        else:
            crdlist = None
        self.msg,msglen=g2lib.grib2_addfield(self.msg,pdtnum,N.array(pdtmpl,'i'),crdlist,drtnum,N.array(drtmpl,'i'),N.ravel(fld),bitmapflag,bmap)

    def end(self):
        """
 Add an end section (section 8) to the GRIB2 message.
 A GRIB2 message is not complete without an end section.
 Once an end section is added, the GRIB2 message can be
 output to a file.
        """
        self.msg,msglen=g2lib.grib2_end(self.msg)
