import arcpy

# Path to the feature class
fc_path = r"E:\Python\Arcpy\test.gdb\service_line"

# Use Describe to get information about the feature class
desc = arcpy.Describe(fc_path)

# Access the spatial reference object
spatial_reference = desc.spatialReference

# Print the name and code of the spatial reference
print("Spatial Reference Name:", spatial_reference.name)
print("Spatial Reference Code:", spatial_reference.factoryCode)
