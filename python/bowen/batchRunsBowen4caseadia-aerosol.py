import os
import tempfile
import numpy as np
import itertools
from subprocess import check_output
import getpass
username=getpass.getuser()


namelist_files =[
    
	'namelist-sip-c300-adia-303aerosol.in' ,\
	'namelist-sip-c303-adia-300aerosol.in'] 




def batchRuns():
    from runsDefineBowen4caseadia import runToDo
    from runsDefineBowen4caseadia import outputDir
    
    k=200
    
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
    
