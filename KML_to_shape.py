import arcpy

arcpy.env.workspace ="E:\Python\Arc_files"
kml="E:\Python\Arc_files\Baks and ATMs.kml"
shapefile="E:\Python\Arc_files\Baks and ATMs.shp
"

arcpy.KMLToLayer_conversion(kml,shapefile)
print arcpy.GetMessages()
