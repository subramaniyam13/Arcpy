import arcpy

arcpy.env.workspace ="E:\Python\Arc_files\Thrissur"

arcpy.CreateFileGDB_management("E:\Python\Arc_files\Thrissur","Thrissurbala.gdb")

input=["final_soil_data.shp","Karuvannur River Basin","River_Reservoir.shp","Relief.shp"]
output="E:\Python\Arc_files\Thrissur\Thrissurbala.gdb"




