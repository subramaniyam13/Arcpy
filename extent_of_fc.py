import arcpy

# Path to the feature class
feature_class = r"E:\Python\Arcpy\test.gdb\service_line"

# Create a Describe object for the feature class
desc = arcpy.Describe(feature_class)

# Get the extent of the feature class
extent = desc.extent

# Print the extent values
print("XMin: {0}".format(extent.XMin))
print("YMin: {0}".format(extent.YMin))
print("XMax: {0}".format(extent.XMax))
print("YMax: {0}".format(extent.YMax))
