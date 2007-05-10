from grib2 import Grib2Decode, Grib2Encode
import numpy as N
# open a GRIB2 file, create a Grib2 class instance.
filein = '../sampledata/gfs.grb'
print 'input grib file:',filein
grbs = Grib2Decode(filein)
# open a file for output.
fileout = 'test.grb'
print 'output grib file:',fileout
f=open(fileout,'wb')
# test encoding sxn0, sxn1.
print 'message number,field number,bitmap flag,min,max:'
print '------------------------------------------------'
for nmsg,grb in enumerate(grbs):
    grbo = Grib2Encode(grb.discipline_code,grb.identification_section)
    # add grid definition template
    if hasattr(grb,'grid_definition_list'):
       grbo.addgrid(grb.grid_definition_info,grb.grid_definition_template,deflist=grb.grid_definition_list)
    else:
       grbo.addgrid(grb.grid_definition_info,grb.grid_definition_template)
    field = grb.data()
    bitmapflag = grb.bitmap_indicator_flag
    if bitmapflag == 0:
        bitmap = grb._bitmap
    else:
        bitmap = None
    if bitmap is not None:
        fieldcompress = N.compress(N.ravel(bitmap),N.ravel(field))
        fieldmin = fieldcompress.min(); fieldmax = fieldcompress.max()
    else:
        fieldmin = field.min(); fieldmax = field.max()
    print nmsg+1,bitmapflag,fieldmin,fieldmax
    # add product definition template, data representation template
    # and data (field and optional bitmap).
    if hasattr(grb,'extra_vertical_coordinate_info'):
        grbo.addfield(grb.product_definition_template_number,grb.product_definition_template,grb.data_representation_template_number,grb.data_representation_template,field,coordlist=grb.extra_vertical_coordinate_info,bitmapflag=bitmapflag,bitmap=bitmap)
    else:
        grbo.addfield(grb.product_definition_template_number,grb.product_definition_template,grb.data_representation_template_number,grb.data_representation_template,field,bitmapflag=bitmapflag,bitmap=bitmap)
    # finalize the grib message.
    grbo.end()
    # write it to the file.
    f.write(grbo.msg)
# close the output file
f.close()
# close the input GRIB2 file.
print 'done! '+filein+' and '+fileout+' should have identical data'
print '(run grib_list on both and compare output)'