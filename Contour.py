import arcpy
from arcpy.sa import *
arcpy.env.workspace = r"E:\Python\Arc_files\Raster"

Contour("n23_e091_1arc_v3.tif","Contour.shp",200)


msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)