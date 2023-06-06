import arcpy

# Path to the feature class
feature_class = r"E:\Python\Arcpy\test.gdb\proposed"

# Field name to be used for selection
field_name = "status"

# Attribute value for selection
attribute_value = "active"

# Create a feature layer to perform the selection
arcpy.MakeFeatureLayer_management(feature_class, "temp_layer")

# Construct the SQL query for the selection
sql_query = "{0} = '{1}'".format(arcpy.AddFieldDelimiters("temp_layer", field_name), attribute_value)

# Select features based on the attribute value
arcpy.SelectLayerByAttribute_management("temp_layer", "NEW_SELECTION", sql_query)

# Copy the selected features to a new feature class
output_feature_class = r"E:\Python\Arcpy\test.gdb\proposed_selected"
arcpy.CopyFeatures_management("temp_layer", output_feature_class)

# Print a message indicating the selection and copy process was successful
print("Features selected and copied successfully!")
