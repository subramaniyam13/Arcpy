
import arcpy

arcpy.env.workspace ="E:\Python\Arc_files\Baks and ATMs.shp"

input=("E:\Python\Arc_files\Baks and ATMs.shp")
output=("E:\Python\Arc_files\Baks and ATMs.shp")

arcpy.Dissolve_management(input,output,"","","SINGLE_PART","")
print arcpy.GetMessages()
