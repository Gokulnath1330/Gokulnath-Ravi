# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:47:14 2022

@author: GOKULNATH
"""
#use matplotlib to plot the graph
import matplotlib.pyplot as plt
#using pandas to read the csv file
import pandas as pd
report = pd.read_csv(r"E:\New folder\mental health IHR.csv")
print(report)
#To take specific data location is used
mentalhealth1=report.loc[report['Location'] == 'India']
mentalhealth2=report.loc[report['Location'] == 'Switzerland']
#To plot four axis we used x,y,w,u
x,y = (mentalhealth1['Period'],mentalhealth1['Value'])
w,u = (mentalhealth2['Period'],mentalhealth2['Value'])
#To show figure plot
plt.figure()
#To plot line plot I use plot and label is used to label ther axis
plt.plot(x,y,label='India',linewidth = 5)
plt.plot(w,u,label='Switzerland',linewidth = 5)
#To give background style
plt.style.use('ggplot')
plt.xlabel('Period')
plt.ylabel('Value') 
#To give the title
plt.title('Mental health IHR')
plt.legend(loc='center right')
plt.show()

