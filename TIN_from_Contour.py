import arcpy
from arcpy.sa import *
arcpy.env.workspace = r"E:\Python\Arc_files\Raster"


arcpy.CreateTin_3d("TIN.tif","","Contour.shp","constrained_delaunay")

msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)