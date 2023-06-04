import arcpy
from arcpy.sa import *
arcpy.env.workspace = r"E:\Python\Arc_files\Raster"
outslope=Slope("n23_e091_1arc_v3.tif","Degree",0.3043)
outslope.save("E:\Python\Arc_files\Raster\otslope1")


msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)