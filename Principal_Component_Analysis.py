import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.workspace = r"E:\Python\Arc_files\Raster"

outPCA=PrincipalComponents(["n23_e091_1arc_v3.tif"],1,"pcsdata.txt")
outPCA.save("E:\Python\Arc_files\Raster/outpc01")
msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)