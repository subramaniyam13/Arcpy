import arcpy
arcpy.env.workspace = r"E:\Python\Arc_files\Mean"
input="banks.shp"
output="banks_Mean.shp"

arcpy.MeanCenter_stats(input,output)
msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)