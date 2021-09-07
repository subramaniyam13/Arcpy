import arcpy

Shapefile=r"C:\Users\subra\Documents\CRIME_MAPPING\New_folder\CHENNAI_buffer.shp"
Shapefile_buffer=r"C:\Users\subra\Documents\CRIME_MAPPING\New_folder\CHENNAI_bufferxxx.shp"
arcpy.Buffer_analysis(
    Shapefile,
    Shapefile_buffer,
    '5000 meters'
)
