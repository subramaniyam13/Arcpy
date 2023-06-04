import arcpy
arcpy.env.workspace = r"E:\Python\Arc_files\Erase"
input="58M_3.shp"
erase= "Polygons.shp"
output="Erase.shp"
arcpy.Erase_analysis(input,erase,output,"")
msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)