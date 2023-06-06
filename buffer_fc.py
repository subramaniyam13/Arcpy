import arcpy

# Path to the input feature class
input_feature_class = r"E:\Python\Arcpy\test.gdb\service_line"

# Path to the output feature class
output_feature_class = r"E:\Python\Arcpy\test.gdb\service_line_buffer"

# Distance and unit for the buffer (e.g., 100 meters)
buffer_distance = "100 meters"

# Buffer method (e.g., "FULL", "OUTSIDE_ONLY", "INSIDE_ONLY")
buffer_method = "FULL"

# Create the buffer around the features
arcpy.Buffer_analysis(input_feature_class, output_feature_class, buffer_distance, buffer_method)

# Print a message indicating the buffer creation was successful
print("Buffer created successfully!")
