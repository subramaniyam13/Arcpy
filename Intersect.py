import arcpy
arcpy.env.workspace = r"E:\Python\Arc_files\Intersect"
input="Maharashtra.shp","gis_osm_railways_free_1.shp"
output="Intersect.shp"
arcpy.Intersect_analysis(["Maharashtra.shp","gis_osm_railways_free_1.shp",],"Intersect.shp", "ALL","","INPUT")
msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)