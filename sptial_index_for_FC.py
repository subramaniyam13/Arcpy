import arcpy

# Path to the feature class
feature_class = r"E:\Python\Arcpy\test.gdb\service_line"

# Create a spatial index
arcpy.AddSpatialIndex_management(service_line)