from distutils.core import setup
from distutils.extension import Extension
import os, glob, sys

g2clib_deps = glob.glob('g2clib_src/*.c')
proj_deps = glob.glob('proj_src/*.c')

jasper_dir = os.environ.get('JASPER_DIR')
png_dir = os.environ.get('PNG_DIR')
zlib_dir = os.environ.get('ZLIB_DIR')

incdirs = ["g2clib_src"]
libdirs=[]
libraries=[]
macros=[]
f=open('Lib/compression_support.py','w')
if jasper_dir: 
    incdirs.append(os.path.join(jasper_dir,'include'))
    libdirs.append(os.path.join(jasper_dir,'lib'))
    macros.append(('USE_JPEG2000',1))
    libraries.append("jasper")
    f.write('jpeg2000_support = True\n')
else:
    f.write('jpeg2000_support = False\n')
if png_dir: 
    incdirs.append(os.path.join(png_dir,'include'))
    libdirs.append(os.path.join(png_dir,'lib'))
    macros.append(('USE_PNG',1))
    libraries.append("png")
    libraries.append("z")
    f.write('png_support = True\n')
else:
    f.write('png_support = False\n')
if zlib_dir: 
    incdirs.append(os.path.join(zlib_dir,'include'))
    libdirs.append(os.path.join(zlib_dir,'lib'))
f.close()

if sys.maxint > 2**31-1:
     macros.append(('__64BIT__',1))

extensions = [Extension("g2lib",g2clib_deps,include_dirs=incdirs,library_dirs=libdirs,libraries=libraries,define_macros=macros)]
extensions.append(Extension("proj4", proj_deps,include_dirs=["proj_src"]))

setup(
  name = "pygrib2",
  version           = "20051125",
  description       = "Python module for reading GRIB Edition 2 files",
  author            = "Jeff Whitaker",
  author_email      = "jeffrey.s.whitaker@noaa.gov",
  url               = "http://www.cdc.noaa.gov/people/jeffrey.s.whitaker/python/grib2/",
  download_url      = "http://www.cdc.noaa.gov/people/jeffrey.s.whitaker/python/grib2/grib2-20051125.tar.gz",
  packages          = ['grib2'],
  package_dir       = {'grib2':'Lib'},
  scripts           = ['utils/rdgrib','utils/gribrepack'],
  ext_modules       = extensions)
