#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 04:40:58 2019

@author: matteo
"""
import numpy as np


def ROC_Computer(H0,H1,Binning,Number_Events):  
    
    """
    H0,H1 : your inputs, they should be at least a 1 dimensional array containing your observations
    Number_Events : simply the total number of measures
    Binning: the number of bins you want to use for generate the histograms
    """
    
    Hist0,Bins0 = np.histogram(H0,bins = Binning)
    Hist1,Bins1 = np.histogram(H1,bins = Binning)
    
    Extremal_Points = np.array([np.min(Bins0),np.min(Bins1),np.max(Bins0),np.max(Bins1)])
    
    Threshold = np.linspace(np.min(Extremal_Points),np.max(Extremal_Points),Binning)
    
    Hist_H0,Bins0 = np.histogram(H0,bins = Threshold)
    Hist_H1,Bins1 = np.histogram(H1,bins = Threshold)
        
    True_Positive_Rate = np.zeros((len(Threshold),))
    False_Positive_Rate = np.zeros((len(Threshold),))
    
    for k in range(len(Threshold)):
        True_Positive_Rate[k]  = np.sum(Hist_H1[k:len(Threshold)])
        False_Positive_Rate[k] = np.sum(Hist_H0[k:len(Threshold)])
    
    
    False_Positive_Rate = False_Positive_Rate/Number_Events
    True_Positive_Rate  = True_Positive_Rate/Number_Events   
    Area_Under_Curve = np.sum(True_Positive_Rate[0:Binning-1]*np.abs(np.diff(False_Positive_Rate)))
    

    return True_Positive_Rate,False_Positive_Rate,Area_Under_Curve 