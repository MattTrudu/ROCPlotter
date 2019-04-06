#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 04:46:08 2019

@author: matteo
"""

import numpy as np
import matplotlib.pyplot as plt
import ROC_Generator as roc
"""
def Histogram_Plotter(H0,H1,Binning):
    
    plt.figure()


    plt.hist(H0,bins=Binning,label='Hypothesis 0',color='g',histtype='step')    
    plt.hist(H1,bins=Binning,label='Hypothesis 1',color='r',histtype='step')
    plt.xlabel('Outcome',fontsize = 10)
    plt.ylabel('Counts',fontsize = 10)
    plt.legend(loc=0,fancybox=True,shadow=True)
    
"""
def ROC_Plotter(H0,H1,Number_Events,Binning):
    
    labelpad = 10
    labelfont = 14
    fontlegend = 14
    fonttitle = 20
    ticksize  =14
    
    TPR,FPR,AUC = roc.ROC_Computer(H0,H1,Binning,Number_Events)
    
    plt.figure()
    plt.suptitle('Hypothesis Analysis',fontsize=fonttitle,family='serif')
    plt.subplot(1,2,1)
    plt.title('Hypothesis Histograms',fontsize=fonttitle,family='serif')
    plt.hist(H0,bins=Binning,label='Hypothesis 0',color='g',histtype='step')    
    plt.hist(H1,bins=Binning,label='Hypothesis 1',color='r',histtype='step')
    plt.xlabel('Outcomes',family='serif',labelpad=labelpad,fontsize=labelfont)
    plt.ylabel('Counts',family='serif',labelpad=labelpad,fontsize=labelfont)
    
    plt.subplot(1,2,2)
    plt.title('ROC Curve',fontsize=fonttitle,family='serif')
    plt.plot(FPR,TPR,'-D',markersize = 5,color='r')
    plt.plot(np.linspace(0,1,Binning),np.linspace(0,1,Binning),'--',color='k')
    plt.grid(which='both',linestyle='-.')
    plt.minorticks_on()
    plt.xlabel('False Positive Rate (FPR)',family='serif',labelpad=labelpad,fontsize=labelfont)
    plt.ylabel('True Positive Rate (TPR)',family='serif',labelpad=labelpad,fontsize=labelfont)
    plt.xlim(-0.1,1.1)
    plt.ylim(-0.1,1.1)
    L = plt.legend(loc=9,ncol = 1 ,fontsize=fontlegend,handleheight=1.0, handletextpad=0.5,labelspacing=0.05,framealpha=1, bbox_to_anchor=(0.80,0.55),title='AUC = '+str("%.3f" % AUC)+'')
    plt.setp(L.texts, family='serif')
    plt.setp(L.get_title(),family='serif',fontsize=fontlegend)
    plt.tick_params(labelsize=ticksize)
    

Number_Events = 100000
Binning = 100

H0 = np.random.normal(3,0.2,size = Number_Events)
H1 = np.random.normal(5,0.5,size = Number_Events)    

ROC_Plotter(H0,H1,Number_Events,Binning)

    

plt.show()