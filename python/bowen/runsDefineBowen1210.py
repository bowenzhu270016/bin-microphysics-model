#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:27:20 2020

@author: mccikpc2
"""
set1=5
if set1==1:
    runToDo = [['tinit=280.','tinit=290.'], \
               ['n_aer1(1:3,1:1)        = 2.27e9, 3.08e9, 1.05e9, d_aer1(1:3,1:1)        = 13e-9   , 32e-9, 123e-9, sig_aer1(1:3,1:1)      = 0.66   , 0.69, 0.54, ', 
            'n_aer1(1:3,1:1)        = 1.0e7, 5.08e7, 0.55e8,    d_aer1(1:3,1:1)        = 13e-9   , 32e-9, 223e-9,    sig_aer1(1:3,1:1)      = 0.66   , 0.69, 0.54, '], \
               ['hm_flag=.false.','hm_flag=.true.'], \
               ['break_flag=0','break_flag=2'], \
               ['mode1_flag=.false.','mode1_flag=.true.'], \
               ['mode2_flag=.false.','mode2_flag=.true.'], \
                   ]
    columns1=['t','aer','hm','br','m1','m2']
elif set1==2:
    runToDo = [[['tinit=276.869','pinit=57645.1,','rhinit=0.52341,', \
                'n_aer1(1:4,1:1)        = 850e6, 8e6, 210e6, 0.e6, d_aer1(1:4,1:1)        = 0.099e-6  , 0.2e-6, 0.04e-6, 1e-7, sig_aer1(1:4,1:1)      = 0.39   , 0.05, 0.25, 0.25,'],\
                ['tinit=282.069','pinit=65016.9,','rhinit=0.66744,',\
                'n_aer1(1:4,1:1)        = 850e6, 7e6, 650e6, 20.e6, d_aer1(1:4,1:1)        = 0.115e-6  , 0.195e-6, 0.05e-6, 0.26e-6, sig_aer1(1:4,1:1)      = 0.37   , 0.03, 0.3, 0.08,'] ], \
               [['winit=2.5','t_thresh=1600.'], ['winit=5.0','t_thresh=800.']], \
               ['hm_flag=.false.','hm_flag=.true.'], \
               ['break_flag=0','break_flag=2'], \
               ['mode1_flag=.false.','mode1_flag=.true.'], \
               ['mode2_flag=.false.','mode2_flag=.true.'], \
                   ]
    columns1=['case','w','hm','br','m1','m2']
elif set1==3:
    runToDo = [[['hm_flag=.false.','break_flag=0','mode1_flag=.false.','mode2_flag=.false.'],['hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.']]]
    columns1=['sip']

elif set1==4:
    runToDo = [
               # ['break_flag=0','break_flag=2'], \
                  ['hm_flag=.false.','hm_flag=.true.'], \
                # ['mode1_flag=.false.','mode1_flag=.true.'], \
                # ['mode2_flag=.false.','mode2_flag=.true.'], \
                   ]
    columns1=['sip']    

elif set1==5:
    runToDo = [[['updraft_type=4','ent_rate=0.1','winit=0.15','hm_flag=.false.','break_flag=0','mode1_flag=.false.','mode2_flag=.false.'],\
                ['updraft_type=4','ent_rate=0.14','winit=0.15','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=4','ent_rate=0.14','winit=0.17','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=4','ent_rate=0.14','winit=0.2','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=4','ent_rate=0.14','winit=0.22','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=4','ent_rate=0.14','winit=0.25','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=4','ent_rate=0.14','winit=0.27','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.']]]
    columns1=['ent']
    
elif set1==7:
    runToDo = [[['updraft_type=4','ent_rate=0.2','winit=2.5','t_thresh=2000.','hm_flag=.false.','break_flag=0','mode1_flag=.false.','mode2_flag=.false.'],\
                ['updraft_type=4','ent_rate=0.2','winit=2.5','t_thresh=2000.','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=2','ent_rate=0.0','winit=2.0','t_thresh=2500.','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=2','ent_rate=0.0','winit=1.5','t_thresh=3333.','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=2','ent_rate=0.0','winit=1.0','t_thresh=5000.','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=2','ent_rate=0.0','winit=0.5','t_thresh=10000.','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],\
                ['updraft_type=2','ent_rate=0.0','winit=0.25','t_thresh=20000.','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.']]]
    columns1=['ent']
elif set1==6:
    runToDo = [[['updraft_type=4','ent_rate=0.2','thresh_to_start_hom_mix=0.','hm_flag=.false.','break_flag=0','mode1_flag=.false.','mode2_flag=.false.'],['updraft_type=4','ent_rate=0.2','thresh_to_start_hom_mix=0.','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],['updraft_type=4','ent_rate=0.2','thresh_to_start_hom_mix=8000.','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.'],['updraft_type=2','ent_rate=0.0','thresh_to_start_hom_mix=0.','hm_flag=.true.','break_flag=2','mode1_flag=.true.','mode2_flag=.true.']]]
    columns1=['ent']


outputDir='/tmp'
