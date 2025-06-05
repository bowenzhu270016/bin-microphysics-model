# -*- coding: utf-8 -*-
"""
Created on Mon Apr  19 10:00:00 2020

@author: mccikpc2
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib
#matplotlib.use('agg')
from matplotlib import rc

import matplotlib.pyplot as plt
import getpass

username=getpass.getuser()


namelist_files =['namelist-sip-ent-c299.in' , \
	'namelist-sip-ent-c300-bowen.in' ,\
	'namelist-sip-ent-c302.in', \
	'namelist-sip-ent-c303-bowen.in', \
	'namelist-sip-ent-c305.in', \
	'namelist-sip-ent-c307.in', \
	'namelist-sip-ent-c310.in', \
	'namelist-sip-ent-c313.in'] 


from runsDefineBowen import runToDo
from runsDefineBowen import outputDir

outputDir='/tmp'
fileName=outputDir + '/' + username + '/output1.nc'

def plot_model_run():
    
    k=0
    fig=plt.figure()
    for i in range(len(namelist_files)):
        for j in range(len(runToDo[0])):
            fileName = '/tmp/' + username + '/output' + str(k).zfill(3) + '.nc'
            nc=Dataset(fileName)
            """
            read in variabels from file
            """
            time=       nc['time'][:]
            z=          nc['z'][:]
            p=          nc['p'][:]
            t=          nc['t'][:]
            rh=         nc['rh'][:]
            w=          nc['w'][:]
            ql=         nc['ql'][:]
            beta_ext=   nc['beta_ext'][:]
            ndrop=      nc['ndrop'][:]
            deff=       nc['deff'][:]
            mwat=       nc['mwat'][:,:,:]
            ice=False
            if ('qi' in nc.variables.keys()):
    	        ice=True
    	        qi=         nc['qi'][:]
    	        nice=       nc['nice'][:]
    	        mice=       nc['mice'][:,:,:]

            nc.close()
            k += 1

    	    # create a subplot
            ax=plt.subplot(2,4,i+1)
            ax.plot(nice/1000.,z/1000.)
            
        ax.legend([namelist_files[i][17:21] + ' ' + runToDo[0][0], \
            namelist_files[i][17:21] + ' ' + runToDo[0][1]])
        ax.set_xlabel('$N_{ice}$ (L$^{-1}$)')
        ax.set_ylabel('Z (km)')
        ax.set_xscale('log')
        ax.set_xlim((0.01,1e6))
        ax.set_ylim((3,12))
        plt.grid()
        
    plt.ion()
    plt.draw()
    plt.show()
    
    
    
    plt.savefig("/tmp/" + username +  "/bowen_analysis.png")

    
    
    
    
if __name__=="__main__":
    plot_model_run()
