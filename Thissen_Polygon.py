import arcpy
arcpy.env.workspace = r"E:\Python\Arc_files\Thissen_polygon"
input="banks.shp"
#erase= "Polygons.shp"
output="Thissen.shp"
outFields= "ALL"
arcpy.CreateThiessenPolygons_analysis(input,output,outFields)
msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)