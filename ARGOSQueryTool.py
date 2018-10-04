# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: Kelly Dobroski (kelly.dobroski@duke.edu)
# Created on: October 4, 2018

# Create a variable pointing to the file with no header
fileName = "SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read the first line from the open file object
lineStrings = fileObj.readlines()
print ("There are {} records in the file".format(len(lineStrings)))
    
# Close the file object
fileObj.close()

# Create empty dictionaries
dateDict = {}
locationDict = {}

try:

    # Use a for loop to read each line, one at a time, until the list is exhausted
    for lineString in lineStrings:

        # Use the split command to parse the items in lineString into a list object
        lineData = lineString.split("\t")

        # Assign variables to specfic items in the list
        recordID = lineData[0]              # ARGOS tracking record ID
        obsDateTime = lineData[2]           # Observation date and time (combined)
        obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
        obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
        obsLC = lineData[3]                 # Observation Location Class
        obsLat = lineData[5]                # Observation Latitude
        obsLon = lineData[6]                # Observation Longitude

        #Filter records that get added to the dictionary
        if obsLC in ("1","2","3"):

            # Add values to dictionary
            dateDict[recordID] = obsDate
            locationDict[recordID] = (obsLat, obsLon) 

    # Indicate script is complete
    print ("Finished")


    #Ask for a date
    userDate = input("Enter a date (M/D/YYYY):")

    #check the date
    if not "/" in userDate:
        print("wrong format")

    #create empty key list
    keyList = []

    #loop through date dictionary
    for k, v in dateDict.items():
        #see if the date matches the user date
        if v== userDate:
            keyList.append(k)
    for key in keyList:
        print (locationDict[key])

except:
    print("there was an error")
    