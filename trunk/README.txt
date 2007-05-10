Python module for reading and writing GRIB edition 2 files.

Uses C code from NCEP's g2clib (http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2).

GRIB is the World Meteorological Organization (WMO) standard
file format for the weather data exchange.

**Requires** 

1) Python 2.3 or higher.

2) numpy:      N-dimensional array object for python
               (http://numpy.scipy.org).

3) pyproj:     python interface to PROJ.4 library 
               (http://code.google.com/p/pyproj). This in turn requires
               the PROJ.4 C library from http://proj.maptools.org.

4) jasper lib: This library is a C implementation of the JPEG-2000 Part-1 
               standard (i.e., ISO/IEC 15444-1).
               Download from the JasPer Project's
               home page, http://www.ece.uvic.ca/~mdadams/jasper/.
               Needed to work with GRIB2 files that use JPEG2000 compression.

4) png lib:    This library is a C implementation of the Portable Network
               Graphics PNG image compression format. 
               It's probably already on your system.
               If not, download 
               from http://www.libpng.org/pub/png/libpng.html.
               Needed to work with GRIB2 files that use PNG compression.

5) zlib:       This library contains compression/decompression routines
               used by libpng for PNG image compression support. 
               It's probably already on your system.
               If not, download from http://www.gzip.org/zlib/.
               Needed to work with GRIB2 files that use PNG compression.

**Installation**

1) set the environment variables JASPER_DIR, PNG_DIR, ZLIB_DIR to point
to the directories where jasper, png and zlib are installed.
For example, the jasper libs should be found in $JASPER_DIR/lib, and
the include files in $JASPER_DIR/include.
Windows users will need either cygwin (www.cygwin.com) or mingw (www.mingw.org).

2) Run 'python setup.py install', as root if necessary.

**Usage**

See documentation in the 'doc/html' directory, and try the test scripts
in the 'examples' directory.  Sample GRIB2 files are in the
sampledata directory.

NCEP GRIB Edition 2 files are available at:
ftp://tgftp.nws.noaa.gov/SL.us008001/ST.opnt/

Feedback to Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>

**Copyright**

the source code from g2clib (http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2)
is include in the 'g2clib_src' directory and is in the public domain.

Everything else:

copyright (c) 2007 by Jeffrey Whitaker.

Permission to use, copy, modify, and distribute this software and its
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

**Links**

http://code.google.com/p/pygrib2
http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/
http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2
http://www.ecmwf.int/products/data/software/grib2.html
http://weather.gov/mdl/iwt/grib2/decoder.htm
http://www.nws.noaa.gov/datamgmt/doc/GRIB2_encoding.html
http://proj.maptools.org
http://tigge.ucar.edu
