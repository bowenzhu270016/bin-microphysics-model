#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:36:56 2020

@author: mccikpc2
"""

"""
    0. function to change file
    1. loops
    2. run command
"""

import os
import tempfile
import numpy as np
import itertools
from subprocess import check_output
import getpass
username=getpass.getuser()


namelist_files =['namelist-sip-ent-c298.in' , \
                 
                 
	'namelist-sip-ent-c299.in', \
	'namelist-sip-ent-c300-bowen.in' ,\
	'namelist-sip-ent-c302.in', \
	'namelist-sip-ent-c303-bowen.in', \
	'namelist-sip-ent-c304.in', \
	'namelist-sip-ent-c305.in', \
	'namelist-sip-ent-c306.in', \
	'namelist-sip-ent-c307.in', \
	'namelist-sip-ent-c308.in', \
	'namelist-sip-ent-c309.in', \
	'namelist-sip-ent-c310.in', \
	'namelist-sip-ent-c312.in', \
	'namelist-sip-ent-c313.in', \
	'namelist-sip-ent-c314.in'] 

    



def batchRuns():
    from runsDefineBowen1104 import runToDo
    from runsDefineBowen1104 import outputDir
    
    k=500
    
    """
    	run the parcel model for each namelist
    """
    if not os.path.exists('/tmp/' + username):
        os.mkdir('/tmp/' + username)
    for i in range(len(namelist_files)):
        inputFile=os.getcwd()+ '/' + namelist_files[i]
        
        dumpFileObj=tempfile.NamedTemporaryFile(delete=False)
        dumpFile=dumpFileObj.name
        
        
        tmpFileObj=tempfile.NamedTemporaryFile(delete=False)
        tmpFile=tmpFileObj.name
        
        # loop over parameter off/ on
        for j in range(len(runToDo[0])):
            print('Run number ' + str(k).zfill(3) + '; namelist: ' + namelist_files[i] + '; params: '  + str(runToDo[0][j]))      
            changeFile(inputFile,dumpFile,'/tmp/output1.nc','/tmp/' + username + '/output' +str(k).zfill(3) + '.nc')
            changeFile(dumpFile,tmpFile,runToDo[0][0],runToDo[0][j])
            
            print(tmpFile)
            #print(dumpFile)
            # define the string to run the model
            str1='./main.exe ' + tmpFile
            # runs the model
            result = check_output(str1,shell=True,cwd='../').decode()

            k += 1
    
        dumpFileObj.close()
        os.unlink(dumpFileObj.name)
        tmpFileObj.close()
        os.unlink(tmpFileObj.name)

"""
    0. function to change file
"""
def changeFile(inFile,outFile,inString,outString):
    fin = open(inFile,"rt")
    
    lines=[]
    for line in fin:
         lines.append(line)
        
    fin.close()


    fout = open(outFile,"wt")

    for line in lines:
        if isinstance(outString, list):
            line1=line
            for i in range(len(outString)):
                line1=line1.replace(inString[i],outString[i])
            fout.write(line1)
        else:
            fout.write(line.replace(inString,outString))
    

    fout.close()
    
    
if __name__=="__main__":
    batchRuns()
    
