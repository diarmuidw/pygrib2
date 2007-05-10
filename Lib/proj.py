import numpy as N
import pyproj, math

__version__ = '1.2'
_dg2rad = math.radians(1.)
_rad2dg = math.degrees(1.)

class Proj:
    """
 peforms cartographic transformations (converts from longitude,latitude
 to native map projection x,y coordinates and vice versa) using proj 
 (http://proj.maptools.org/)
 Uses a pyrex generated C-interface to libproj.
 
 __init__ method sets up projection information.
 __call__ method compute transformations.
 See docstrings for __init__ and __call__ for details.

 Contact: Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>
    """

    def __init__(self,projparams,llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat,urcrnrislatlon=True):
        """
 initialize a Proj class instance.

 Input 'projparams' is a dictionary containing proj map
 projection control parameter key/value pairs.
 See the proj documentation (http://www.remotesensing.org/proj/)
 for details.

 llcrnrlon,llcrnrlat are lon and lat (in degrees) of lower left hand corner
 of projection region.

 urcrnrlon,urcrnrlat are lon and lat (in degrees) of upper right hand corner
 of projection region if urcrnrislatlon=True (default). Otherwise, 
 urcrnrlon,urcrnrlat are x,y in projection coordinates (units meters), 
 assuming the lower left corner is x=0,y=0.
        """
        # set units to meters.
        if not projparams.has_key('units'):
            projparams['units']='m'
        elif projparams['units'] != 'm':
            print 'resetting units to meters ...'
            projparams['units']='m'
        # remove x_0, y_0 keys if they exist (and recompute them)
        if projparams.has_key('x_0'):
            del projparams['x_0']
        if projparams.has_key('y_0'):
            del projparams['y_0']
        self.projparams = projparams
        # make sure proj parameter specified.
        # (no other checking done in proj parameters)
        if 'proj' not in projparams.keys():
            raise KeyError, "need to specify proj parameter"
        if 'R' not in projparams.keys() and 'a' and 'b' not in projparams.keys():
            raise KeyError, "need to specify R (perfect sphere radius), or a and b (major and minor sphere radii)"
        self.projection = projparams['proj']
        # rmajor is the semi-major axis.
        # rminor is the semi-minor axis.
        # esq is eccentricity squared.
        try:
            self.rmajor = projparams['a']
            self.rminor = projparams['b']
        except:
            self.rmajor = projparams['R']
            self.rminor = self.rmajor
        if self.rmajor == self.rminor:
            self.ellipsoid = False
        else:
            self.ellipsoid = True
        self.flattening = (self.rmajor-self.rminor)/self.rmajor
        self.esq = (self.rmajor**2 - self.rminor**2)/self.rmajor**2
        self.llcrnrlon = llcrnrlon
        self.llcrnrlat = llcrnrlat
        if self.projection not in ['cyl','ortho','moll','robin']:
            self._proj4 = pyproj.Proj(projparams)
            llcrnrx, llcrnry = self(llcrnrlon,llcrnrlat)
        elif self.projection == 'cyl':
            llcrnrx = llcrnrlon
            llcrnry = llcrnrlat
        elif self.projection == 'ortho':
            self._proj4 = pyproj.Proj(projparams)
            llcrnrx = -self.rmajor
            llcrnry = -self.rmajor
            urcrnrx = -llcrnrx
            urcrnry = -llcrnry
        elif self.projection == 'moll' or self.projection == 'robin':
            self._proj4 = pyproj.Proj(projparams)
            xtmp,urcrnry = self(projparams['lon_0'],90.)
            urcrnrx,xtmp = self(projparams['lon_0']+180.,0)
            llcrnrx = -urcrnrx
            llcrnry = -urcrnry
        # compute x_0, y_0 so ll corner of domain is x=0,y=0.
        # note that for 'cyl' x,y == lon,lat
        self.projparams['x_0']=-llcrnrx
        self.projparams['y_0']=-llcrnry
        # reset with x_0, y_0. 
        if self.projection != 'cyl':
            self._proj4 = pyproj.Proj(projparams)
            llcrnry = 0.
            llcrnrx = 0.
        else:
            llcrnrx = llcrnrlon
            llcrnry = llcrnrlat
        if urcrnrislatlon:
            self.urcrnrlon = urcrnrlon
            self.urcrnrlat = urcrnrlat
            if self.projection not in ['ortho','moll','robin']:
                urcrnrx,urcrnry = self(urcrnrlon,urcrnrlat)
            elif self.projection == 'ortho':
                urcrnrx = 2.*self.rmajor
                urcrnry = 2.*self.rmajor
            elif self.projection == 'moll' or self.projection == 'robin':
                xtmp,urcrnry = self(projparams['lon_0'],90.)
                urcrnrx,xtmp = self(projparams['lon_0']+180.,0)
        else:
            urcrnrx = urcrnrlon
            urcrnry = urcrnrlat
            urcrnrlon, urcrnrlat = self(urcrnrx, urcrnry, inverse=True)
            self.urcrnrlon = urcrnrlon
            self.urcrnrlat = urcrnrlat
        # corners of domain.
        self.llcrnrx = llcrnrx
        self.llcrnry = llcrnry
        self.urcrnrx = urcrnrx
        self.urcrnry = urcrnry
        if urcrnrx > llcrnrx:
            self.xmin = llcrnrx
            self.xmax = urcrnrx
        else:
            self.xmax = llcrnrx
            self.xmin = urcrnrx
        if urcrnry > llcrnry:
            self.ymin = llcrnry
            self.ymax = urcrnry
        else:
            self.ymax = llcrnry
            self.ymin = urcrnry

    def __call__(self,x,y,inverse=False):
        """
 Calling a Proj class instance with the arguments lon, lat will
 convert lon/lat (in degrees) to x/y native map projection 
 coordinates (in meters).  If optional keyword 'inverse' is
 True (default is False), the inverse transformation from x/y
 to lon/lat is performed.

 For cylindrical equidistant projection ('cyl'), this
 does nothing (i.e. x,y == lon,lat).

 lon,lat can be either scalar floats or arrays.
        """
        if self.projection == 'cyl': # for cyl x,y == lon,lat
            return x,y
        if inverse:
            outx,outy = self._proj4(x,y,inverse=True)
            if self.projection in ['merc','mill']: 
                if self.projection == 'merc':
                    coslat = math.cos(math.radians(self.projparams['lat_ts']))
                    sinlat = math.sin(math.radians(self.projparams['lat_ts']))
                else:
                    coslat = 1.
                    sinlat = 0.
                # radius of curvature of the ellipse perpendicular to
                # the plane of the meridian.
                rcurv = self.rmajor*coslat/math.sqrt(1.-self.esq*sinlat**2)
                try: # x a scalar or an array
                    outx = _rad2dg*(x/rcurv) + self.llcrnrlon
                except: # x a sequence
                    outx = [_rad2dg*(xi/rcurv) + self.llcrnrlon for xi in x]
        else:
            outx,outy = self._proj4(x,y)
            if self.projection in ['merc','mill']:
                if self.projection == 'merc':
                    coslat = math.cos(math.radians(self.projparams['lat_ts']))
                    sinlat = math.sin(math.radians(self.projparams['lat_ts']))
                else:
                    coslat = 1.
                    sinlat = 0.
                # radius of curvature of the ellipse perpendicular to
                # the plane of the meridian.
                rcurv = self.rmajor*coslat/math.sqrt(1.-self.esq*sinlat**2)
                try: # x is a scalar or an array
                    outx = rcurv*_dg2rad*(x-self.llcrnrlon)
                except: # x is a sequence.
                    outx = [rcurv*_dg2rad*(xi-self.llcrnrlon) for xi in x]
        return outx,outy

    def makegrid(self,nx,ny,returnxy=False):
        """
 return arrays of shape (ny,nx) containing lon,lat coordinates of
 an equally spaced native projection grid.
 if returnxy=True, the x,y values of the grid are returned also.
        """
        dx = (self.urcrnrx-self.llcrnrx)/(nx-1)
        dy = (self.urcrnry-self.llcrnry)/(ny-1)
        x = self.llcrnrx+dx*N.indices((ny,nx),'f')[1,:,:]
        y = self.llcrnry+dy*N.indices((ny,nx),'f')[0,:,:]
        lons, lats = self(x, y, inverse=True)
        if returnxy:
            return lons, lats, x, y
        else:
            return lons, lats

if __name__ == "__main__":

    params = {}
    params['proj'] = 'lcc'
    params['R'] = 6371200
    params['lat_1'] = 50
    params['lat_2'] = 50
    params['lon_0'] = -107
    nx = 349; ny = 277; dx = 32463.41; dy = dx
    awips221 = Proj(params,-145.5,1.0,(nx-1)*dx,(ny-1)*dy,urcrnrislatlon=False)
# AWIPS grid 221 parameters
# (from http://www.nco.ncep.noaa.gov/pmb/docs/on388/tableb.html)
    llcornerx, llcornery = awips221(-145.5,1.)
# find 4 lon/lat corners of AWIPS grid 221.
    llcornerx = 0.; llcornery = 0.
    lrcornerx = dx*(nx-1); lrcornery = 0.
    ulcornerx = 0.; ulcornery = dy*(ny-1)
    urcornerx = dx*(nx-1); urcornery = dy*(ny-1)
    llcornerlon, llcornerlat = awips221(llcornerx, llcornery, inverse=True)
    lrcornerlon, lrcornerlat = awips221(lrcornerx, lrcornery, inverse=True)
    urcornerlon, urcornerlat = awips221(urcornerx, urcornery, inverse=True)
    ulcornerlon, ulcornerlat = awips221(ulcornerx, ulcornery, inverse=True)
    print '4 corners of AWIPS grid 221:'
    print llcornerlon, llcornerlat
    print lrcornerlon, lrcornerlat
    print urcornerlon, urcornerlat
    print ulcornerlon, ulcornerlat
    print 'from GRIB docs'
    print '(see http://www.nco.ncep.noaa.gov/pmb/docs/on388/tableb.html)'
    print '   -145.5  1.0'
    print '   -68.318 0.897'
    print '   -2.566 46.352'
    print '   148.639 46.635'
# compute lons and lats for the whole AWIPS grid 221 (377x249).
    import time; t1 = time.clock()
    lons, lats = awips221.makegrid(nx,ny)
    t2 = time.clock()
    print 'compute lats/lons for all points on AWIPS 221 grid (%sx%s)' %(nx,ny)
    print 'max/min lons'
    print min(N.ravel(lons)),max(N.ravel(lons))
    print 'max/min lats'
    print min(N.ravel(lats)),max(N.ravel(lats))
    print 'took',t2-t1,'secs'
