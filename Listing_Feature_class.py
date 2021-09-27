import arcpy

arcpy.env.workspace ="E:\Python\Arc_files\india-latest-free.shp"

arcpy.env.overwriteOutput = True
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    print (fcdesc.basename + " is a" + " " +fcdesc.shapetype + " " + fcdesc.datasettype)
