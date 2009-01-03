from distutils.core import setup
from distutils.extension import Extension
import os, glob, sys

g2clib_deps = glob.glob('g2clib_src/*.c')

jasper_dir = os.environ.get('JASPER_DIR')
png_dir = os.environ.get('PNG_DIR')
zlib_dir = os.environ.get('ZLIB_DIR')
if jasper_dir is None or png_dir is None:
    print """
 Please set the JASPER_DIR and PNG_DIR environment variables
 to point to the locations of the JasPer (jpeg2000 -
 http://www.ece.uvic.ca/~mdadams/jasper/) and png libraries
 and include files. If zlib is not installed in the standard
 library search path, you may need to set ZLIB_DIR as well.
    """
    sys.exit(1)

incdirs = ["g2clib_src"]
libdirs=[]
libraries=[]
macros=[]
incdirs.append(os.path.join(jasper_dir,'include'))
libdirs.append(os.path.join(jasper_dir,'lib'))
macros.append(('USE_JPEG2000',1))
libraries.append("jasper")
incdirs.append(os.path.join(png_dir,'include'))
libdirs.append(os.path.join(png_dir,'lib'))
macros.append(('USE_PNG',1))
libraries.append("png")
libraries.append("z")
if zlib_dir: 
    incdirs.append(os.path.join(zlib_dir,'include'))
    libdirs.append(os.path.join(zlib_dir,'lib'))

if sys.maxint > 2**31-1:
     macros.append(('__64BIT__',1))

extensions = [Extension("g2lib",g2clib_deps,include_dirs=incdirs,library_dirs=libdirs,libraries=libraries,define_macros=macros)]

setup(
  name = "pygrib2",
  version           = "20090105",
  description       = "Python module for reading and writing GRIB Edition 2 files",
  author            = "Jeff Whitaker",
  author_email      = "jeffrey.s.whitaker@noaa.gov",
  url               = "http://code.google.com/p/pygrib2",
  download_url      = "http://code.google.com/p/pygrib2/downloads/list",
  packages          = ['grib2'],
  package_dir       = {'grib2':'Lib'},
  scripts           = ['examples/grib_list','examples/grib_repack'],
  ext_modules       = extensions)
