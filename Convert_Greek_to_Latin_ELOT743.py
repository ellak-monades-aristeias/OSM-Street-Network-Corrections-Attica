# Use Unicode Codepage UTF-8
# -*- coding: utf-8 -*-

# SCRIPT HEADER
#
# Script Name: "Convert_Greek_to_Latin_ELOT743.py"
#
# Script Description:
# This script converts Greek strings to their Latin counterparts, according to the ELOT-743 specifications.
#
# Script Timeline:
# October 2015: Creation
#
# Author: Ioannis Dafermos
# Works in: QGIS
# Licensed under: EUPL V.1.1

# Set the input parameters of this tool
##Convert Greek to Latin (ELOT743)=name
##Table=group
##Input_Table=table
##Greek_Field=field Input_Table
##Latin_Field=field Input_Table

# Import necessary modules & packages
# Module "icpyqg.py" contains functions required by this script
import sys
theModulePath = "C:\\Users\\JohnGreat\\.qgis2\\processing\\scripts"
sys.path.append(theModulePath)
import icpyqg

# Get necessary objects from the input parameters
theInputTable = processing.getObject(Input_Table)
theGreekFieldName = Greek_Field
theGreekFieldIndex = theInputTable.fieldNameIndex(Greek_Field)
theLatinFieldName = Latin_Field
theLatinFieldIndex = theInputTable.fieldNameIndex(Latin_Field)

# Get a <Features Iterator> on <theInputTable> for looping through its records
# If no records have been selected by the User, then use all records
theFeaturesIterator = theInputTable.selectedFeaturesIterator()
theFeaturesIteratorCount = theInputTable.selectedFeatureCount()
if theInputTable.selectedFeatureCount() == 0:
    theFeaturesIterator = theInputTable.getFeatures()
    theFeaturesIteratorCount = theInputTable.featureCount()

# Start editing <theInputTable> and initialize <theCounter> for the progress bar
theInputTable.startEditing()
theCounter = 0

# Loop through the records of <theFeaturesIterator> to convert strings from Greek to Latin
for theFeature in theFeaturesIterator:
    # Move the progress bar forward
    theCounter += 1
    progress.setPercentage( int(100*theCounter/theFeaturesIteratorCount) )

    # Get the contents of the <Greek_Field>, convert them into Latin using a special
    # function from module "icpyqg" and write the resulting string to the <Latin_Field>
    theGreekString = theFeature[theGreekFieldName]
    theLatinString = icpyqg.convertGreekToLatinELOT743(theGreekString, 'utf-8')
    theInputTable.changeAttributeValue(theFeature.id(), theLatinFieldIndex, theLatinString)
