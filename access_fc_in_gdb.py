import arcpy

# Set the workspace to the geodatabase
arcpy.env.workspace = r"E:\Python\Arcpy\test.gdb"

# List all feature classes in the geodatabase
feature_classes = arcpy.ListFeatureClasses()

# Print the names of the feature classes
for fc in feature_classes:
    print(fc)
