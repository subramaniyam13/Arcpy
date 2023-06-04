import arcpy
from arcpy.sa import *
arcpy.env.workspace = r"E:\Python\Arc_files\Raster"

input="2021_1.tif"
output="2021_1_Resample.tif"
arcpy.Resample_management(input,output,"","NEAREST")

msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)