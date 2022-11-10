# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:19:30 2022

@author: GOKULNATH
"""
#use matplotlib to plot the graph
import matplotlib.pyplot as plt
#using pandas to read the csv file
import pandas as pd
report = pd.read_csv(r"E:\New folder\mental health IHR.csv")
print(report)
#To take specific data I used location
mentalhealth1=report.loc[report['Location'] == 'China']
mentalhealth2=report.loc[report['Location'] == 'Switzerland']
x,y = (mentalhealth1['Period'],mentalhealth1['Value'])
w,u = (mentalhealth2['Period'],mentalhealth2['Value'])
#To show the plotfigure
plt.figure()
#ply.scatter is used for plot the scatter plot
plt.scatter(x,y,label='China',linewidth = 5,color='blue')
plt.scatter(w,u,label='Switzerland',linewidth = 5,color='red')
#To label x and y axis
plt.xlabel('Period')
plt.ylabel('Value') 
#Plt.title is used to give title at the top of plot
plt.title('Mental health IHR')
#It is for apply style in the background
plt.style.use('ggplot')
#legend is a tool used for explain a graph
plt.legend(loc='center right')#
plt.show()