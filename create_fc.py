import arcpy

# Workspace where you want to create the new feature class
workspace = r"E:\Python\Arcpy\test.gdb"

# Name and path of the new feature class
output_feature_class = r"E:\Python\Arcpy\test.gdb\riser"

# Coordinate system for the new feature class (optional)
coordinate_system = arcpy.SpatialReference(4326)  # Example: WGS 1984

# Create the new feature class
arcpy.CreateFeatureclass_management(workspace, arcpy.Describe(output_feature_class).name, "POINT", "", "", "", coordinate_system)

# Print a message indicating the feature class creation was successful
print("Feature class created successfully!")
