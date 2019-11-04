#!/usr/bin/env python3
#import serial
#import serial_handler as sh
#from untitled1 import parse
def data_dump(data): #this function is expecting a list of dictionaries
    sampleDataKeys = list(data[0].keys())#makes a list of the keys of the first dictionary of data in the data array
    firstLine = ""#initializes the first line variable which will hold all the information to be written in the first line
    for i in range(len(sampleDataKeys)):#iterates through each key in the list
        firstLine = firstLine + sampleDataKeys[i]+','#adds each key separated by a comma into the firstLine variable
    
    with open('data.csv', 'w') as o:#opens a file named data.csv as writtable
       o.write(firstLine+"\n")#writes the first line into the csv file
       for i in range(len(data)):#iterates through each datapoint in the given array of dictionaries from the function parameter
            o.write(','.join(map(str,list(data[i].values())))+'\n')#writes the values of each dictionary in the array to the csv file

'''
#This code is for testing the function:
            
sampledict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }

sampledict2 = {
        "brand": "Chevy",
        "model": "Camero",
        "year": 1988
        }

sampledata = [sampledict, sampledict2]
for i in range(0,100):
    sampledict2 = {
        "brand": "Chevy",
        "model": "Camero",
        "year": i
        }
    sampledata.append(sampledict2)
    

data_dump(sampledata)
'''
