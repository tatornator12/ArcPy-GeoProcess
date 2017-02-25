# Script Name: Calculate Slope of Buffered Area
# Description: Clips a raster file by a buffered
#              shapefile and calculates the slope
#              of the clipped raster file.
# Created By:  Taylor Teske
# Date:        8/07/2016

# Import ArcPy site-package and os modules
import arcpy 
from arcpy import env
from arcpy.sa import *

# Set the input raster data for the mask
rasterMaskFeatures = arcpy.GetParameterAsText(0)

# Set the feature mask data
maskFeatures = arcpy.GetParameterAsText(1)

# Set the input slope raster data
outRaster = arcpy.GetParameterAsText(2)

# Set the output slope data
outSlopeRaster = arcpy.GetParameterAsText(3)


try:
    
    # Execute Mask Extract and Save
    outExtractByMask = ExtractByMask(rasterMaskFeatures, maskFeatures)
    outExtractByMask.save(outRaster)
    
    # Set Slope Variables
    outMeasurement = "DEGREE"
    zFactor = 1
    
    #Execute Slope and Save
    outSlope = Slope(outRaster, outMeasurement, zFactor)
    outSlope.save(outSlopeRaster)
    
except:
    arcpy.AddMessage(arcpy.GetMessages(2))
    print arcpy.GetMessages(2)
