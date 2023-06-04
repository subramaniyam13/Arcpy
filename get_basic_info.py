import arcpy
arcpy.env.workspace = r"E:\Python\Arc_files\Raster"
input="2021_1.tif"

desc=arcpy.Describe(input)
print ("Raster base name is :"+ desc.basename)
print ("Raster data type is :"+ desc.dataType)
print ("Raster file extension :" + desc.extension)

msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)