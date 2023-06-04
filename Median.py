import arcpy
arcpy.env.workspace = r"E:\Python\Arc_files\Mean"
input="banks.shp"

output="banks_Median.shp"

arcpy.MedianCenter_stats(input,output)
msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)