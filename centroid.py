import arcpy

arcpy.env.workspace ="E:\Python\Arc_files\centroid"

input=("E:\Python\Arc_files\centroid\Ind_Stat_uptd.shp")
output="E:\Python\Arc_files\centroid\india_centeroid.shp"

arcpy.FeatureToPoint_management(input,output,"CENTROID")
print arcpy.GetMessages()




