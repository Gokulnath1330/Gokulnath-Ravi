# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:02:41 2022

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
#colors is used for different ratio separation
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'r']
#explode is used for separate the pie into pieces
explode = (0, 0, 0, 0, 0,0.3,0.2)  
#to show the plot figure
plt.figure()
#plt.pie used to plot piechart
plt.pie(mentalhealth1['Value'],labels=mentalhealth1['Period'],
colors=colors, explode=explode, shadow=True, autopct='%1.1f%%')
#It is used to give title
plt.title('India Mental health IHR')
plt.show()
