# Script Name: Calculate Statistics of Clipped Features
# Description: Clips a raster file by a buffered
#              shapefile and calculates the slope
#              of the clipped raster file.
# Created By:  Taylor Teske
# Date:        8/07/2016

# Import ArcPy site-package and os modules
import arcpy
import os


#Set the Selection Input
selectInput = arcpy.GetParameterAsText(0)

#Set the Selection Field
selectField = arcpy.GetParameterAsText(1)

#Set the layer inputs
layerOne = arcpy.GetParameterAsText(2)
layerTwo = arcpy.GetParameterAsText(3)
layerThree = arcpy.GetParameterAsText(4)

#Set the output layers
outputLayer1 = arcpy.GetParameterAsText(5)
outputLayer2 = arcpy.GetParameterAsText(6)
outputLayer3 = arcpy.GetParameterAsText(7)

try:
    
    arcpy.MakeFeatureLayer_management(selectInput, "selectLayer")
    count = 1

    while count < 11:
        exp = selectField + "=" + str(count)
        outputName1 = arcpy.CreateUniqueName(outputLayer1)
        outputName2 = arcpy.CreateUniqueName(outputLayer2)
        outputName3 = arcpy.CreateUniqueName(outputLayer3)
        arcpy.SelectLayerByAttribute_management("selectLayer", "NEW_SELECTION", exp)
        arcpy.Clip_analysis(layerOne, "selectLayer", outputName1)
        arcpy.Clip_analysis(layerTwo, "selectLayer", outputName2)
        arcpy.Clip_analysis(layerThree, "selectLayer", outputName3)
        arcpy.AddField_management(outputName1, "CENTROID_ID", "SHORT")
        rows1 = arcpy.SearchCursor(outputName1, "CENTROID_ID")
        for r in rows1:
            r.getValue(count)
        arcpy.AddField_management(outputName2, "CENTROID_ID", "SHORT")
        arcpy.AddField_management(outputName3, "CENTROID_ID", "SHORT")
        count += 1

except:
    arcpy.AddMessage(arcpy.GetMessages(2))
    print arcpy.GetMessages(2)
    
    
    
