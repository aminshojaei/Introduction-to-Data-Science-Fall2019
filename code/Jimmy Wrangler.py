# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:53:47 2019

@author: a335s717
"""


import pandas as pd
import matplotlib.pyplot as plt


Ave_temp_vector=[]
Solar_sum_vector=[]
Wind_sum_vector=[]
Ave_wind_speed_vector=[]
other_renewable_sum_vector=[]
total_load_sum_vector=[]
total_load_sum_year=0
Solar_sum_year=0
Wind_sum_year=0
other_renewable_sum_year=0

Spain_generation = pd.read_csv('https://raw.githubusercontent.com/aminshojaei/Introduction-to-Data-Science-Fall2019/master/energy_dataset.csv', low_memory = False)
Spain_weather = pd.read_csv('https://raw.githubusercontent.com/aminshojaei/Jimmy-Wrangler-Data-Explorer/master/weather_features.csv', low_memory = False)

S_generation = Spain_generation [['time' ,'generation solar', 'generation wind onshore','generation other renewable','total load actual']]
S_weather = Spain_weather [['dt_iso','city_name' ,'temp', 'wind_speed']]



i = 0     ## slelect a number for choosing which city are you looking for
if i==0 : City_name = "Valencia"
if i==1 : City_name = "Madrid"
if i==2 : City_name = "Bilbao"
if i==3 : City_name = "Barcelona"
if i==4 : City_name = "Seville"

S_weather_city = S_weather.loc[S_weather.city_name == City_name]

S_weather_city = S_weather_city.loc[S_weather_city.dt_iso >='2018-01-01' ]   
S_generation = S_generation.loc[S_generation.time >='2018-01-01']

S_weather_city= S_weather_city.drop_duplicates()
S_generation = S_generation.drop_duplicates()


S_weather_city.rename(columns={'dt_iso':'time'}, inplace=True)

merged= pd.merge(S_generation,S_weather_city[['time','temp','wind_speed']], on='time')


merged['temp']= merged['temp'] - 273.15     ## change Kelvin to celcius

NaN=merged.isna()      # To show the NaN values
merged=merged.dropna(how='any')
    
describe= merged.describe()      # show the static summary


for i in range (12):
    if i == 0 : ## January
        Month = merged.loc[(merged.time >='2018-01-01') & (merged.time <'2018-02-01')  ] 
        Solar_sum= Month['generation solar'].sum() 
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 1 : ## February
        Month = merged.loc[(merged.time >='2018-02-01') & (merged.time <'2018-03-01')  ] 
        Solar_sum= Month['generation solar'].sum() 
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 2 : ## March
        Month = merged.loc[(merged.time >='2018-03-01') & (merged.time <'2018-04-01')  ]
        Solar_sum= Month['generation solar'].sum()
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 3 : ## April
        Month = merged.loc[(merged.time >='2018-04-01') & (merged.time <'2018-05-01')  ] 
        Solar_sum= Month['generation solar'].sum() 
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 4 : ## May
        Month = merged.loc[(merged.time >='2018-05-01') & (merged.time <'2018-06-01')  ] 
        Solar_sum= Month['generation solar'].sum() 
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 5 : ## June
        Month = merged.loc[(merged.time >='2018-06-01') & (merged.time <'2018-07-01')  ]
        Solar_sum= Month['generation solar'].sum() 
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 6 : ## July
        Month = merged.loc[(merged.time >='2018-07-01') & (merged.time <'2018-08-01')  ] 
        Solar_sum= Month['generation solar'].sum() 
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 7 : ## August
        Month = merged.loc[(merged.time >='2018-08-01') & (merged.time <'2018-09-01')  ] 
        Solar_sum= Month['generation solar'].sum()
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 8 : ## September
        Month = merged.loc[(merged.time >='2018-09-01') & (merged.time <'2018-10-01')  ] 
        Solar_sum= Month['generation solar'].sum()
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 9 : ## October
        Month = merged.loc[(merged.time >='2018-10-01') & (merged.time <'2018-11-01')  ]
        Solar_sum= Month['generation solar'].sum() 
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 10: ##November 
        Month = merged.loc[(merged.time >='2018-11-01') & (merged.time <'2018-12-01')  ] 
        Solar_sum= Month['generation solar'].sum() 
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()
    if i == 11: ## December
        Month = merged.loc[(merged.time >='2018-12-01') & (merged.time <'2018-13-01')  ] 
        Solar_sum= Month['generation solar'].sum() 
        Wind_onshore_sum= Month['generation wind onshore'].sum() 
        Other_renewable_sum= Month['generation other renewable'].sum()
        total_load_sum=Month['total load actual'].sum()

    Ave_temp= Month['temp'].mean()
    Ave_temp_vector.append (Ave_temp)
    Ave_wind_speed=Month['wind_speed'].mean()
    Ave_wind_speed_vector.append(Ave_wind_speed)
    Solar_sum_vector.append(Solar_sum)
    Wind_sum_vector.append(Wind_onshore_sum)
    other_renewable_sum_vector.append(Other_renewable_sum)
    total_load_sum_vector.append(total_load_sum)

Month_name=['Jan' , 'Feb' , 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
plt.bar(Month_name, Solar_sum_vector)
plt.xlabel('MONTH')
plt.ylabel('Power(MW)')
plt.title('Solar generation for '+str(City_name))
plt.show()

plt.bar(Month_name, Wind_sum_vector)
plt.xlabel('MONTH')
plt.ylabel('Power(MW)')
plt.title('Wind generation for '+str(City_name))
plt.show()  


for i in range(len(total_load_sum_vector)):
    total_load_sum_year += total_load_sum_vector[i]
    Solar_sum_year += Solar_sum_vector[i]
    Wind_sum_year += Wind_sum_vector[i]
    other_renewable_sum_year += other_renewable_sum_vector[i]

values=[total_load_sum_year , Solar_sum_year , Wind_sum_year , other_renewable_sum_year]
colors=['b','g','r','c']
labels=['non-renewable generation','Solar generation','Wind generation','other renewable generation']
plt.pie(values, colors=colors,autopct='%1.1f%%', labels= labels,counterclock=False, shadow=True)
plt.title('2018 power generation for Valencia')
#plt.legend(labels,loc=3)
plt.show()
        
        
      



















