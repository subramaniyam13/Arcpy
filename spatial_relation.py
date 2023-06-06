import arcpy

# Path to the feature class to be selected from
input_feature_class = r"E:\Python\Arcpy\test.gdb\forest.shp"

# Path to the feature class used for the spatial relationship
relationship_feature_class = r"E:\Python\Arcpy\test.gdb\lake.shp"

# Spatial relationship type
# Options: "INTERSECT", "CONTAINS", "WITHIN", "BOUNDARY", "CROSSES", "SHARE_A_LINE_SEGMENT_WITH"
relationship_type = "INTERSECT"

# Create a feature layer for the input feature class
arcpy.MakeFeatureLayer_management(input_feature_class, "input_layer")

# Select features based on the spatial relationship
arcpy.SelectLayerByLocation_management("input_layer", relationship_type, relationship_feature_class)

# Copy the selected features to a new feature class
output_feature_class = r"E:\Python\Arcpy\test.gdb\lakes_in_forest.shp"
arcpy.CopyFeatures_management("input_layer", output_feature_class)

# Print a message indicating the selection and copy process was successful
print("Features selected and copied successfully!")
