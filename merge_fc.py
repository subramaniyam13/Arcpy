import arcpy

# List of input feature classes to be merged
input_feature_classes = [r"E:\Python\Arcpy\test.gdb\service_line", r"E:\Python\Arcpy\test.gdb\main_line",]

# Path to the output merged feature class
output_feature_class = r"E:\Python\Arcpy\test.gdb\merged_fc"

# Merge the input feature classes into the output feature class
arcpy.Merge_management(input_feature_classes, output_feature_class)

# Print a message indicating the merge was successful
print("Feature classes merged successfully!")
