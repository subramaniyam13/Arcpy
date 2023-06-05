import arcpy

# Path to the feature class
feature_class = r"E:\Python\Arcpy\test.gdb\main_line"

# Add a new field called "NewField" of type Integer
arcpy.AddField_management(feature_class, "NewField", "INTEGER")
