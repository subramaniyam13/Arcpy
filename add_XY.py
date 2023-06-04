

import arcpy
from arcpy import env

env.workspace = r"E:\Python\Arc_files\add_XY"
arcpy.Copy_management("chennai.shp", "chennaiXYpts.shp")
arcpy.AddXY_management("chennaiXYpts.shp")