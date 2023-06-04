import arcpy
arcpy.env.workspace = r"E:\Python\Arc_files\Raster"
arcpy.Mosaic_management("2021_1.tif;2021_2.tif","2021_2.tif","LAST","FIRST","0","9","","","")


msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)