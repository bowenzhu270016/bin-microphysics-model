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


from runsDefineBowen1104 import runToDo
from runsDefineBowen1104 import outputDir

outputDir='/tmp'
fileName=outputDir + '/' + username + '/output1.nc'

def plot_model_run():
    k = 0
    fig, axes = plt.subplots(3, 5, figsize=(12, 6))  # 创建 2x4 网格的子图
    axes = axes.flatten()  # 展平成一维数组，方便按索引访问

    for i in range(len(namelist_files)):
        ax = axes[i]  # 选择当前子图
        # 为每个子图设置标题
        experiment_title = namelist_files[i].split('-')[-2] if 'bowen' in namelist_files[i] else namelist_files[i].split('-')[-1].split('.')[0]
        ax.set_title(experiment_title, fontsize=10, fontweight='bold')
        ax.grid()
        ax.set_ylim(-50, 1050)
        # ax.axhspan(-8, -3, facecolor='gray', alpha=0.3, label='Y-axis range: -3 to -8')
        # ax.axhline(y=-37.5, color='#4682B4', linestyle='--', linewidth=1.5, label='Y = -37.5')
        
        
        for j in range(len(runToDo[0])):
            # 构建文件路径
            fileName = f'/tmp/{username}/output{str(k).zfill(3)}.nc'
            print(f"Attempting to open: {fileName}")  # 调试输出，检查文件路径
            
            try:
                # 打开文件
                nc = Dataset(fileName)
                time = nc['time'][:]
                z = nc['z'][:]
                
                if 'qi' in nc.variables.keys():
                    nice = nc['nice'][:]
                    cdnc = nc['ndrop'][:]
                    # 绘制当前组合下的线条
                    # ax.plot(time, nice/1000, label=f"{runToDo[0][j]}")  # 使用参数组合作为标签
                    ax.plot(time, cdnc/1e6, label=f"{runToDo[0][j]}")  # 使用参数组合作为标签
                nc.close()
            except FileNotFoundError:
                print(f"File {fileName} not found.")
            
            k += 1  # 在内层循环中递增 k，确保文件索引唯一

        # 设置子图标签和图例
        # ax.legend()


        # 判断是否为最左列，保留纵坐标，否则隐藏
        if ax.is_first_col():
            # ax.set_ylabel('$N_{ice}$ (L$^{-1}$)', fontsize=10)  # 设置纵坐标标签
            ax.set_ylabel('CDNC', fontsize=10)  # 设置纵坐标标签
        else:
            # ax.set_yticks([])  # 隐藏刻度
            ax.set_ylabel('')  # 隐藏标签

        # 判断是否为最下一行，保留横坐标，否则隐藏
        if ax.is_last_row():
            ax.set_xlabel('Time (s)', fontsize=10)  # 设置横坐标标签
        else:
            # ax.set_xticks([])  # 隐藏刻度
            ax.set_xlabel('')  # 隐藏标签
        
        # ax.set_xlabel('Time (s)', fontsize=10)
        # ax.set_ylabel('$N_{ice}$ (L$^{-1}$)', fontsize=10)
        # ax.grid()

    plt.tight_layout()
    plt.show()

    
    
    
    plt.savefig("/tmp/" + username +  "/bowen_analysis.png")

    
    
    
    
if __name__=="__main__":
    plot_model_run()
