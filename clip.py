import arcpy

arcpy.env.workspace ="E:\Python\Arc_files\clip"

input=("E:\Python\Arc_files\clip\gis_osm_buildings_a_free_1.shp")
clip="E:\Python\Arc_files\clip\Maharashtra.shp"

arcpy.Clip_analysis(input,clip,"E:\Python\Arc_files\clip\Buildings_Maharashtra.shp")
print arcpy.GetMessages()

