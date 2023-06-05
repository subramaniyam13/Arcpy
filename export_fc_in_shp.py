import arcpy

# Path to the input feature class
input_feature_class = r"E:\Python\Arcpy\test.gdb\service_line"

# Path to the output shapefile
output_shapefile = r"E:\Python\output\service_line.shp"

# Export the feature class to a shapefile
arcpy.FeatureClassToFeatureClass_conversion(input_feature_class, output_shapefile)