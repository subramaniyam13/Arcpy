import arcpy
from arcpy.sa import *
arcpy.env.workspace = r"E:\Python\Arc_files\Raster"

input="2021_1.tif"
output=Square(input)
output.save("Square_output1.tif")

msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)