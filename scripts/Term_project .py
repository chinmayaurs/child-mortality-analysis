#cell 0
  --------------------------------------------------------
    Project Code :Python for Data Analysis
    Participants : Pretik C P, Deepak Nayak
    ME Big Data, SOIS
  -----------------------------------------------------------


#cell 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nvd3 import multiBarChart,multiBarHorizontalChart
import nvd3
nvd3.ipynb.initialize_javascript()
from IPython.core.display import display, HTML
get_ipython().magic('matplotlib nbagg')

#cell 2
# Reading xlsx file 

#cell 3
df = pd.read_excel('cod.xlsx')
#df



#cell 4
# Creating DataFrames

#cell 5
df1 = pd.DataFrame(df)
#df1

#cell 6
# Converting to csv file

#cell 7
df1.to_csv('cod_data.csv')


#cell 8
csv_file = pd.read_csv('cod_data.csv')
#list(csv_file,)

#cell 9
# Deaths of children Under 5 year

#cell 10
selected_columns_under5 = csv_file[['ISO_Code',
'CountryName',
 'Year','Preterm',
 'Pertussis',
 'Intrapartum',
 'Sepsis',
 'Tetanus',
 'Congenital',
 'Pneumonia',
 'Diarrhoea',
 'Malaria',
 'Aids',
 'Measles',
 'Injury',
 'Meningitis']]

#cell 11
list(selected_columns_under5)

#cell 12
under_five = pd.DataFrame(selected_columns_under5)

#cell 13
#under_five

#cell 14
# New born(first month)

#cell 15
selected_columns_2 = csv_file[['ISO_Code',
 'CountryName',
 'Year','Pneumonia .1',
 'Preterm ',
 'Intrapartum ',
 'Sepis ',
 'Tetanus ',
 'Congenital ',
 'Diarrheoea ']]

#cell 16
list(selected_columns_2)

#cell 17
new_born_first_month = pd.DataFrame(selected_columns_2)

#cell 18
#new_born_first_month


#cell 19
# Death of childrens in Newborn

#cell 20
selected_columns_3 = csv_file[['ISO_Code',
 'CountryName',
 'Year','Pneumonia (Newborn)',
 'Preterm (Newborn)',
 'Intrapartum (Newborn)',
 'Sepis (Newborn)',
 'Tetanus (Newborn)',
 'Congenital (Newborn)',
 'Diarrheoea (Newborn)']]

#cell 21
list(selected_columns_3)

#cell 22
new_born = pd.DataFrame(selected_columns_3)

#cell 23
#new_born

#cell 24
# Death in 1-59 months

#cell 25
selected_columns_4 = csv_file[['ISO_Code',
 'CountryName',
 'Year','Pneumonia ',
 'Diarrhoea ',
 'Malaria ',
 'AIDS ',
 'Measles ',
 'Injuries ',
 'Meningitis ']]

#cell 26
one_to_59 = pd.DataFrame(selected_columns_4)

#cell 27
#one_to_59


#cell 28
### List of dataframes

#cell 29
#under_five
#new_born_first_month
#new_born
#one_to_59

#cell 30
# --------------Under_Five-------------------

#cell 31
# Creating a list of Dveloping Countries

#cell 32
a = ['AFG','ALB','DZA','AGO','ARG','ARM','AZE','BGD','BLR','BLZ','BEN','BTN','BOL','BIH','BWA','BRA','BGR','BFA',
     'BDI','KHM','CMR','CAF','TCD','CHN','COL','COM','COG','CRI','CIV','CUB','DJI','DMA','DOM','ECU','EGY','SLV','ERI',
     'ETH','FJI','GAB','GMB','GEO','GHA','GRD','GTM','GIN','GNB','GUY','HTI','HUN','IND','IDN','IRN','IRQ','JAM','JOR',
     'KAZ','KEN','KIR','KGZ','LAO','LBN','LSO','LBR','LBY','MDG','MYS','MDV','MLI','MHL','MRT','MUS','MEX','MNG','MNE',
     'MAR','MOZ','MMR','NAM','NPL','NIC','NER','NGA','PAK','PLW','PAN','PNG','PRY','PER','PHL','ROU','RUS','RWA','WSM',
     'STP','SEN','SRB','SYC','SLE','SLB','SOM','ZAF','SSD','LKA','SDN','SUR','SWZ','SYR','TJK','THA','TLS','TGO','TON',
     'TUN','TUR','TKM','TUV','UGA','UKR','UZB','VUT','VEN','VNM','YEM','ZMB','ZWE']  

#cell 33
# DataFrame for Developing countries

#cell 34
developing_countries = under_five.loc[under_five['ISO_Code'].isin(a)]
developing_countries.reset_index(drop=True)

            
      

#cell 35
# DataFrame for Developed Countries

#cell 36
developed_countries = under_five.loc[~under_five['ISO_Code'].isin(a)]
developed_countries.reset_index(drop=True)
 


#cell 37
# Calculating aggr value for diseases (Developed)

#cell 38
Preterm_developed = developed_countries['Preterm']
Preterm_developed = Preterm_developed.mean()
Preterm_developed

#cell 39
Intrapartum_developed = developed_countries['Intrapartum']
Intrapartum_developed = Intrapartum_developed.mean()
Intrapartum_developed

#cell 40
Sepsis_developed = developed_countries['Sepsis']
Sepsis_developed = Sepsis_developed.mean()
Sepsis_developed

#cell 41
Congenital_developed = developed_countries['Congenital']
Congenital_developed = Congenital_developed.mean()
Congenital_developed

#cell 42
Pneumonia_developed = developed_countries['Pneumonia']
Pneumonia_developed = Pneumonia_developed.mean()
Pneumonia_developed

#cell 43
Injury_developed = developed_countries['Injury']
Injury_developed = Injury_developed.mean()
Injury_developed

#cell 44
Diarrhoea_developed = developed_countries['Diarrhoea']
Diarrhoea_developed = Diarrhoea_developed.mean()
Diarrhoea_developed

#cell 45
# Calculating aggr value for diseases (developing)

#cell 46
Preterm_developing = developing_countries['Preterm']
Preterm_developing = Preterm_developing.mean()
Preterm_developing

#cell 47
Intrapartum_developing = developing_countries['Intrapartum']
Intrapartum_developing = Intrapartum_developing.mean()
Intrapartum_developing

#cell 48
Sepsis_developing = developing_countries['Sepsis']
Sepsis_developing = Sepsis_developing.mean()
Sepsis_developing

#cell 49
Congenital_developing = developing_countries['Congenital']
Congenital_developing = Congenital_developing.mean()
Congenital_developing

#cell 50
Pneumonia_developing = developing_countries['Pneumonia']
Pneumonia_developing = Pneumonia_developing.mean()
Pneumonia_developing

#cell 51
Injury_developing = developing_countries['Injury']
Injury_developing = Injury_developing.mean()
Injury_developing

#cell 52

Diarrhoea_developing = developing_countries['Diarrhoea']
Diarrhoea_developing = Diarrhoea_developing.mean()
Diarrhoea_developing

#cell 53
# Creating a dataframe for aggr values

#cell 54
developed={'preterm':Preterm_developed}
developing={'preterm':Preterm_developing}

#cell 55
d=pd.Series(developed)
d=pd.DataFrame(d)
d.columns=['Developed']
d

#cell 56
d0 = pd.Series(developing)
d0= pd.DataFrame(d0)
d0.columns = ['Developing']
d0

#cell 57
res = pd.concat([d, d0], axis=1, join_axes=[d.index])
res

#cell 58
developed={'Intrapartum':Intrapartum_developed}
developing={'Intrapartum':Intrapartum_developing}

#cell 59
d1=pd.Series(developed)
d1=pd.DataFrame(d1)
d1.columns=['Developed']
d1

#cell 60
d11 = pd.Series(developing)
d11 = pd.DataFrame(d11)
d11.columns = ['Developing']
d11

#cell 61
res1 = pd.concat([d1, d11], axis=1, join_axes=[d1.index])
res1

#cell 62
developed={'Sepsis':Sepsis_developed}
developing={'Sepsis':Sepsis_developing}

#cell 63
d2=pd.Series(developed)
d2=pd.DataFrame(d2)
d2.columns=['Developed']
d2

#cell 64
d22 = pd.Series(developing)
d22 = pd.DataFrame(d22)
d22.columns = ['Developing']
d22

#cell 65
res2 = pd.concat([d2, d22], axis=1, join_axes=[d2.index])
res2

#cell 66
developed={'Congenital':Congenital_developed}
developing={'Congenital':Congenital_developing}

#cell 67
d3=pd.Series(developed)
d3=pd.DataFrame(d3)
d3.columns=['Developed']
d3

#cell 68
d33 = pd.Series(developing)
d33 = pd.DataFrame(d33)
d33.columns = ['Developing']
d33

#cell 69
res3 = pd.concat([d3, d33], axis=1, join_axes=[d3.index])
res3

#cell 70
developed={'Pneumonia':Pneumonia_developed}
developing={'Pneumonia':Pneumonia_developing}

#cell 71
d4=pd.Series(developed)
d4=pd.DataFrame(d4)
d4.columns=['Developed']
d4

#cell 72
d44 = pd.Series(developing)
d44 = pd.DataFrame(d44)
d44.columns = ['Developing']
d44

#cell 73
res4 = pd.concat([d4, d44], axis=1, join_axes=[d4.index])
res4

#cell 74
developed={'Injury':Injury_developed}
developing={'Injury':Injury_developing}

#cell 75
d5=pd.Series(developed)
d5=pd.DataFrame(d5)
d5.columns=['Developed']
d5

#cell 76
d55 = pd.Series(developing)
d55 = pd.DataFrame(d55)
d55.columns = ['Developing']
d55

#cell 77
res5 = pd.concat([d5, d55], axis=1, join_axes=[d5.index])
res5

#cell 78
developed={'Diarrhoea':Diarrhoea_developed}
developing={'Diarrhoea':Diarrhoea_developing}

#cell 79
d6=pd.Series(developed)
d6=pd.DataFrame(d6)
d6.columns=['Developed']
d6

#cell 80

d66 = pd.Series(developing)
d66 = pd.DataFrame(d66)
d66.columns = ['Developing']
d66

#cell 81
res6 = pd.concat([d6, d66], axis=1, join_axes=[d6.index])
res6

#cell 82
frames = [res,res1,res2,res3,res4,res5,res6]

#cell 83
final_frames = pd.concat(frames)
final_frames

#cell 84
chart = multiBarChart(width=1100, height=500, x_axis_format=None)
causes = list(final_frames.index)
Developed = list(final_frames.Developed)
Developing = list(final_frames.Developing)
chart.add_serie(name="Developed", y=Developed, x=causes)
chart.add_serie(name="Developing", y=Developing, x=causes)
chart.buildhtml()
display(HTML(chart.htmlcontent))

#cell 85
#get_ipython().magic('matplotlib nbagg')
#final_frames.plot(kind='barh', title='Variations of the diseases for under 5yrs of age', rot=0, color=(['g','y']),
#                  stacked=True, figsize=(12, 6), edgecolor='b', linewidth=1, fontsize='13', )
#plt.ylabel('<------ Cause of death ------>', fontsize=14, color='b')
#plt.xlabel('<------ Percentage aggregated values ------>', fontsize=14, color='b')



#cell 86
# Divideing developed dataframe according to years

#cell 87
# For 2015

#cell 88
developed_2015 = developed_countries.reset_index(drop=True)
developed_2015 = developed_2015[:68]

#cell 89

Preterm_developed_2015 = developed_2015['Preterm']
Preterm_developed_2015 = Preterm_developed_2015.mean()

#cell 90


Intrapartum_developed_2015 = developed_2015['Intrapartum']
Intrapartum_developed_2015 = Intrapartum_developed_2015.mean()

#cell 91
Sepsis_developed_2015 = developed_2015['Sepsis']
Sepsis_developed_2015 = Sepsis_developed_2015.mean()

#cell 92
Congenital_developed_2015 = developed_2015['Congenital']
Congenital_developed_2015 = Congenital_developed_2015.mean()

#cell 93

Pneumonia_developed_2015 = developed_2015['Pneumonia']
Pneumonia_developed_2015 = Pneumonia_developed_2015.mean()

#cell 94
Injury_developed_2015 = developed_2015['Injury']
Injury_developed_2015 = Injury_developed_2015.mean()

#cell 95

Diarrhoea_developed_2015 = developed_2015['Diarrhoea']
Diarrhoea_developed_2015 = Diarrhoea_developed_2015.mean()

#cell 96

Meningitis_developed_2015 = developed_2015['Meningitis']
Meningitis_developed_2015 = Meningitis_developed_2015.mean()


#cell 97

# For 2000

#cell 98
developed_2000 = developed_countries.reset_index(drop=True)
developed_2000 = developed_2000[68:]

#cell 99
Preterm_developed_2000 = developed_2000['Preterm']
Preterm_developed_2000 = Preterm_developed_2000.mean()

#cell 100
Intrapartum_developed_2000 = developed_2000['Intrapartum']
Intrapartum_developed_2000 = Intrapartum_developed_2000.mean()

#cell 101
Sepsis_developed_2000 = developed_2000['Sepsis']
Sepsis_developed_2000 = Sepsis_developed_2000.mean()

#cell 102
Congenital_developed_2000 = developed_2000['Congenital']
Congenital_developed_2000 = Congenital_developed_2000.mean()

#cell 103
Pneumonia_developed_2000 = developed_2000['Pneumonia']
Pneumonia_developed_2000 = Pneumonia_developed_2000.mean()

#cell 104
Injury_developed_2000 = developed_2000['Injury']
Injury_developed_2000 = Injury_developed_2000.mean()

#cell 105
Diarrhoea_developed_2000 = developed_2000['Diarrhoea']
Diarrhoea_developed_2000 = Diarrhoea_developed_2000.mean()

#cell 106
Meningitis_developed_2000 = developed_2000['Meningitis']
Meningitis_developed_2000 = Meningitis_developed_2000.mean()

#cell 107
# Creating Dataframe for Developed countries (2000&2015)

#cell 108
developed_countries_2000 = {'preterm':Preterm_developed_2000}
developed_countries_2015 = {'preterm':Preterm_developed_2015}
developed_d0 = pd.Series(developed_countries_2000)
developed_d0 = pd.DataFrame(developed_d0)
developed_d0.columns=['2000']
developed_d00 = pd.Series(developed_countries_2015)
developed_d00 = pd.DataFrame(developed_d00)
developed_d00.columns = ['2015']
resd0 = pd.concat([developed_d0, developed_d00], axis=1, join_axes=[developed_d0.index])
resd0


#cell 109
developed_countries_2000 = {'Intrapartum':Intrapartum_developed_2000}
developed_countries_2015 = {'Intrapartum':Intrapartum_developed_2015}
developed_d1 = pd.Series(developed_countries_2000)
developed_d1 = pd.DataFrame(developed_d1)
developed_d1.columns=['2000']
developed_d11 = pd.Series(developed_countries_2015)
developed_d11 = pd.DataFrame(developed_d11)
developed_d11.columns = ['2015']
resd1 = pd.concat([developed_d1, developed_d11], axis=1, join_axes=[developed_d1.index])
resd1



#cell 110
developed_countries_2000 = {'Sepsis':Sepsis_developed_2000}
developed_countries_2015 = {'Sepsis':Sepsis_developed_2015}
developed_d2 = pd.Series(developed_countries_2000)
developed_d2 = pd.DataFrame(developed_d2)
developed_d2.columns=['2000']
developed_d22 = pd.Series(developed_countries_2015)
developed_d22 = pd.DataFrame(developed_d22)
developed_d22.columns = ['2015']
resd2 = pd.concat([developed_d2, developed_d22], axis=1, join_axes=[developed_d2.index])
resd2

#cell 111
developed_countries_2000 = {'Congenital':Congenital_developed_2000}
developed_countries_2015 = {'Congenital':Congenital_developed_2015}
developed_d3 = pd.Series(developed_countries_2000)
developed_d3 = pd.DataFrame(developed_d3)
developed_d3.columns=['2000']
developed_d33 = pd.Series(developed_countries_2015)
developed_d33 = pd.DataFrame(developed_d33)
developed_d33.columns = ['2015']
resd3 = pd.concat([developed_d3, developed_d33], axis=1, join_axes=[developed_d3.index])
resd3


#cell 112
developed_countries_2000 = {'Pneumonia':Pneumonia_developed_2000}
developed_countries_2015 = {'Pneumonia':Pneumonia_developed_2015}
developed_d4 = pd.Series(developed_countries_2000)
developed_d4 = pd.DataFrame(developed_d4)
developed_d4.columns=['2000']
developed_d44 = pd.Series(developed_countries_2015)
developed_d44 = pd.DataFrame(developed_d44)
developed_d44.columns = ['2015']
resd4 = pd.concat([developed_d4, developed_d44], axis=1, join_axes=[developed_d4.index])
resd4

#cell 113
developed_countries_2000 = {'Injury':Injury_developed_2000}
developed_countries_2015 = {'Injury':Injury_developed_2015}
developed_d5 = pd.Series(developed_countries_2000)
developed_d5 = pd.DataFrame(developed_d5)
developed_d5.columns=['2000']
developed_d55 = pd.Series(developed_countries_2015)
developed_d55 = pd.DataFrame(developed_d55)
developed_d55.columns = ['2015']
resd5 = pd.concat([developed_d5, developed_d55], axis=1, join_axes=[developed_d5.index])
resd5

#cell 114
developed_countries_2000 = {'Diarrhoea':Diarrhoea_developed_2000}
developed_countries_2015 = {'Diarrhoea':Diarrhoea_developed_2015}
developed_d6 = pd.Series(developed_countries_2000)
developed_d6 = pd.DataFrame(developed_d6)
developed_d6.columns=['2000']
developed_d66 = pd.Series(developed_countries_2015)
developed_d66 = pd.DataFrame(developed_d66)
developed_d66.columns = ['2015']
resd6 = pd.concat([developed_d6, developed_d66], axis=1, join_axes=[developed_d6.index])
resd6

#cell 115
developed_countries_2000 = {'Meningitis':Meningitis_developed_2000}
developed_countries_2015 = {'Meningitis':Meningitis_developed_2015}
developed_d7 = pd.Series(developed_countries_2000)
developed_d7 = pd.DataFrame(developed_d7)
developed_d7.columns=['2000']
developed_d77 = pd.Series(developed_countries_2015)
developed_d77 = pd.DataFrame(developed_d77)
developed_d77.columns = ['2015']
resd7 = pd.concat([developed_d7, developed_d77], axis=1, join_axes=[developed_d7.index])
resd7

#cell 116
frames1 = [resd0,resd1,resd2,resd3,resd4,resd5,resd6,resd7]
final_frames1 = pd.concat(frames1)
final_frames1



#cell 117
final_frames1.plot(kind='barh', title='Variations in the deaths for under 5yrs of age for developed region', rot=0, color=(['r','b']),
                  figsize=(11, 8), edgecolor='w', linewidth=2, width=0.7)
plt.ylabel('<------ Cause of deaths ------>', fontsize=14, color='m')
plt.xlabel('<------ Percentage aggregated values ------>', fontsize=14, color='m')
#plt.savefig("image.png")

#for i,v in final_frames1(2000):
#    plt.text(v +1, i+.75, str(v), color='black')
#plt.show()
 

#cell 118
# Divinding developing dataframe according to years (2000&2015)

#cell 119
# 2015

#cell 120
developing_2015 = developing_countries.reset_index(drop=True)
developing_2015 = developing_2015[:126]

#cell 121
Preterm_developing_2015 = developing_2015['Preterm']
Preterm_developing_2015 = Preterm_developing_2015.mean()

#cell 122
Intrapartum_developing_2015 = developing_2015['Intrapartum']
Intrapartum_developing_2015 = Intrapartum_developing_2015.mean()

#cell 123
Sepsis_developing_2015 = developing_2015['Sepsis']
Sepsis_developing_2015 = Sepsis_developing_2015.mean()

#cell 124
Congenital_developing_2015 = developing_2015['Congenital']
Congenital_developing_2015 = Congenital_developing_2015.mean()

#cell 125
Pneumonia_developing_2015 = developing_2015['Pneumonia']
Pneumonia_developing_2015 = Pneumonia_developing_2015.mean()

#cell 126
Injury_developing_2015 = developing_2015['Injury']
Injury_developing_2015 = Injury_developing_2015.mean()

#cell 127
Diarrhoea_developing_2015 = developing_2015['Diarrhoea']
Diarrhoea_developing_2015 = Diarrhoea_developing_2015.mean()

#cell 128
Meningitis_developing_2015 = developing_2015['Meningitis']
Meningitis_developing_2015 = Meningitis_developing_2015.mean()

#cell 129
# 2000

#cell 130
developing_2000 = developing_countries.reset_index(drop=True)
developing_2000 = developing_2000[126:]

#cell 131
Preterm_developing_2000 = developing_2000['Preterm']
Preterm_developing_2000 = Preterm_developing_2000.mean()

#cell 132
Intrapartum_developing_2000 = developing_2000['Intrapartum']
Intrapartum_developing_2000 = Intrapartum_developing_2000.mean()

#cell 133
Sepsis_developing_2000 = developing_2000['Sepsis']
Sepsis_developing_2000 = Sepsis_developing_2000.mean()

#cell 134
Congenital_developing_2000 = developing_2000['Congenital']
Congenital_developing_2000 = Congenital_developing_2000.mean()

#cell 135
Pneumonia_developing_2000 = developing_2000['Pneumonia']
Pneumonia_developing_2000 = Pneumonia_developing_2000.mean()

#cell 136
Injury_developing_2000 = developing_2000['Injury']
Injury_developing_2000 = Injury_developing_2000.mean()

#cell 137
Diarrhoea_developing_2000 = developing_2000['Diarrhoea']
Diarrhoea_developing_2000 = Diarrhoea_developing_2000.mean()

#cell 138
Meningitis_developing_2000 = developing_2000['Meningitis']
Meningitis_developing_2000 = Meningitis_developing_2000.mean()

#cell 139
# Creating dataframes for developing countries (2000&2015)

#cell 140
developing_countries_2000 = {'preterm':Preterm_developing_2000}
developing_countries_2015 = {'preterm':Preterm_developing_2015}
developing_d0 = pd.Series(developing_countries_2000)
developing_d0 = pd.DataFrame(developing_d0)
developing_d0.columns=['2000']
developing_d00 = pd.Series(developing_countries_2015)
developing_d00 = pd.DataFrame(developing_d00)
developing_d00.columns = ['2015']
resdg0 = pd.concat([developing_d0, developing_d00], axis=1, join_axes=[developing_d0.index])
resdg0

#cell 141
developing_countries_2000 = {'Intrapartum':Intrapartum_developing_2000}
developing_countries_2015 = {'Intrapartum':Intrapartum_developing_2015}
developing_d1 = pd.Series(developing_countries_2000)
developing_d1 = pd.DataFrame(developing_d1)
developing_d1.columns=['2000']
developing_d11 = pd.Series(developing_countries_2015)
developing_d11 = pd.DataFrame(developing_d11)
developing_d11.columns = ['2015']
resdg1 = pd.concat([developing_d1, developing_d11], axis=1, join_axes=[developing_d1.index])
resdg1

#cell 142
developing_countries_2000 = {'Sepsis':Sepsis_developing_2000}
developing_countries_2015 = {'Sepsis':Sepsis_developing_2015}
developing_d2 = pd.Series(developing_countries_2000)
developing_d2 = pd.DataFrame(developing_d2)
developing_d2.columns=['2000']
developing_d22 = pd.Series(developing_countries_2015)
developing_d22 = pd.DataFrame(developing_d22)
developing_d22.columns = ['2015']
resdg2 = pd.concat([developing_d2, developing_d22], axis=1, join_axes=[developing_d2.index])
resdg2

#cell 143
developing_countries_2000 = {'Congenital':Congenital_developing_2000}
developing_countries_2015 = {'Congenital':Congenital_developing_2015}
developing_d3 = pd.Series(developing_countries_2000)
developing_d3 = pd.DataFrame(developing_d3)
developing_d3.columns=['2000']
developing_d33 = pd.Series(developing_countries_2015)
developing_d33 = pd.DataFrame(developing_d33)
developing_d33.columns = ['2015']
resdg3 = pd.concat([developing_d3, developing_d33], axis=1, join_axes=[developing_d3.index])
resdg3

#cell 144
developing_countries_2000 = {'Pneumonia':Pneumonia_developing_2000}
developing_countries_2015 = {'Pneumonia':Pneumonia_developing_2015}
developing_d4 = pd.Series(developing_countries_2000)
developing_d4 = pd.DataFrame(developing_d4)
developing_d4.columns=['2000']
developing_d44 = pd.Series(developing_countries_2015)
developing_d44 = pd.DataFrame(developing_d44)
developing_d44.columns = ['2015']
resdg4 = pd.concat([developing_d4, developing_d44], axis=1, join_axes=[developing_d4.index])
resdg4

#cell 145
developing_countries_2000 = {'Injury':Injury_developing_2000}
developing_countries_2015 = {'Injury':Injury_developing_2015}
developing_d5 = pd.Series(developing_countries_2000)
developing_d5 = pd.DataFrame(developing_d5)
developing_d5.columns=['2000']
developing_d55 = pd.Series(developing_countries_2015)
developing_d55 = pd.DataFrame(developing_d55)
developing_d55.columns = ['2015']
resdg5 = pd.concat([developing_d5, developing_d55], axis=1, join_axes=[developing_d5.index])
resdg5

#cell 146
developing_countries_2000 = {'Diarrhoea':Diarrhoea_developing_2000}
developing_countries_2015 = {'Diarrhoea':Diarrhoea_developing_2015}
developing_d6 = pd.Series(developing_countries_2000)
developing_d6 = pd.DataFrame(developing_d6)
developing_d6.columns=['2000']
developing_d66 = pd.Series(developing_countries_2015)
developing_d66 = pd.DataFrame(developing_d66)
developing_d66.columns = ['2015']
resdg6 = pd.concat([developing_d6, developing_d66], axis=1, join_axes=[developing_d6.index])
resdg6

#cell 147
developing_countries_2000 = {'Meningitis':Meningitis_developing_2000}
developing_countries_2015 = {'Meningitis':Meningitis_developing_2015}
developing_d7 = pd.Series(developing_countries_2000)
developing_d7 = pd.DataFrame(developing_d7)
developing_d7.columns=['2000']
developing_d77 = pd.Series(developing_countries_2015)
developing_d77 = pd.DataFrame(developing_d77)
developing_d77.columns = ['2015']
resdg7 = pd.concat([developing_d7, developing_d77], axis=1, join_axes=[developing_d7.index])
resdg7

#cell 148
frames2 = [resdg0,resdg1,resdg2,resdg3,resdg4,resdg5,resdg6,resdg7]
final_frames2 = pd.concat(frames2)
final_frames2


#cell 149
#get_ipython().magic('matplotlib nbagg')
#developing2000 = list(final_frames2['2000'])
#final_frames2_index = list(final_frames2.index)
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','sage', 'tan', 'plum', 'gainsboro']
#explode = (0, 0, 0, 0, 0, 0, 0, 0)  
#plt.pie(developing2000, explode=explode, labels=final_frames2_index, colors=colors,
#        autopct='%1.1f%%', shadow=True, startangle=360)
#plt.axis('equal')
#plt.title("For developing region in the year 2000", y=1.08)
#plt.show()


#cell 150
#get_ipython().magic('matplotlib nbagg')
#final_frames2_index = list(final_frames2.index)
#developing2015 = list(final_frames2['2015'])
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','sage', 'tan', 'plum', 'gainsboro']
#explode = (0.1, 0, 0.1, 0.1, 0, 0.1, 0, 0)  
#plt.pie(developing2015, explode=explode, labels=final_frames2_index, colors=colors,
#        autopct='%1.1f%%', shadow=True, startangle=360)
#plt.axis('equal')
#plt.title("For developing region in the year 2015", y=1.08)
#plt.show()

#cell 151
# ----------------New_born_first_month-------------------

#cell 152
list(new_born_first_month)

#cell 153
# Extracting top 30 countries (2015) 

#cell 154
# Preterm

#cell 155
new_born_first_month_Preterm = new_born_first_month[:194]
new_born_first_month_Preterm = new_born_first_month_Preterm[['CountryName','Preterm ']]
new_born_first_month_Preterm = new_born_first_month_Preterm.sort_values(by='Preterm ', ascending=False)
new_born_first_month_Preterm = new_born_first_month_Preterm[:30].reset_index(drop=True)
#new_born_first_month_Preterm.to_csv('Preterm_top30.csv')
#new_born_first_month_Preterm


#cell 156
new_born_first_month_Intrapartum = new_born_first_month[:194]
new_born_first_month_Intrapartum = new_born_first_month_Intrapartum[['CountryName','Intrapartum ']]
new_born_first_month_Intrapartum = new_born_first_month_Intrapartum.sort_values(by='Intrapartum ', ascending=False)
new_born_first_month_Intrapartum = new_born_first_month_Intrapartum[:30].reset_index(drop=True)
#new_born_first_month_Intrapartum.to_csv('Intrapartum_top30.csv')
#new_born_first_month_Intrapartum


#cell 157
new_born_first_month_Sepsis = new_born_first_month[:194]
new_born_first_month_Sepsis = new_born_first_month_Sepsis[['CountryName','Sepis ']]
new_born_first_month_Sepsis = new_born_first_month_Sepsis.sort_values(by='Sepis ', ascending=False)
new_born_first_month_Sepsis = new_born_first_month_Sepsis[:30].reset_index(drop=True)
#new_born_first_month_Sepsis.to_csv('Sepsis_top30.csv')
#new_born_first_month_Sepsis

#cell 158
new_born_first_month_Congenital = new_born_first_month[:194]
new_born_first_month_Congenital = new_born_first_month_Congenital[['CountryName','Congenital ']]
new_born_first_month_Congenital = new_born_first_month_Congenital.sort_values(by='Congenital ', ascending=False)
new_born_first_month_Congenital = new_born_first_month_Congenital[:30].reset_index(drop=True)
#new_born_first_month_Congenital.to_csv('Congenital_top30.csv')
#new_born_first_month_Congenital

#cell 159
# Analysis over Asia country

#cell 160
asian_countries = pd.read_csv('Asia_Country_list.csv')
#asian_countries

#cell 161
asian_countries['Country'] = asian_countries['Countries  ']
asia = pd.DataFrame(asian_countries['Country'])
#asia

#cell 162
remove_spaces = [x.strip().replace(' ', ' ') for x in asia.Country]
remove_spaces = pd.DataFrame(remove_spaces)
formated = remove_spaces.rename(columns={0:"Country"})
column_names = list(formated.Country)

#cell 163
major_diseases = under_five[['ISO_Code','CountryName','Preterm','Intrapartum','Sepsis','Congenital','Pneumonia']][:194]
major_diseases1 = major_diseases.loc[major_diseases['CountryName'].isin(column_names)]
major_disease = major_diseases1.reset_index(drop=True)
#major_disease.to_csv('List_Asian_Countries_With_Cause_For_Deaths.csv')
major_disease.mean()

#cell 164
asian_countries_preterm = major_disease[['CountryName','ISO_Code','Preterm']]
asian_countries_preterm.to_csv('asia_preterm.csv')

#cell 165
# Analysis over Europe country

#cell 166
european_countries = pd.read_csv('European_country_list.csv')
european_countries['Country'] = european_countries['Country ']
european_countries = pd.DataFrame(european_countries['Country'])
#european_countries
#column_names1 = list(european_countries.Country)


#cell 167
remove_spaces1 = [x.strip().replace(' ', ' ') for x in european_countries.Country]
remove_spaces1 = pd.DataFrame(remove_spaces1)
formated1 = remove_spaces1.rename(columns={0:"Country"})
column_names1 = list(formated1.Country)

#cell 168
europe_major_diseases = under_five[['ISO_Code','CountryName','Preterm','Intrapartum','Sepsis','Congenital','Pneumonia']][:194]
european_major_diseases1 = europe_major_diseases.loc[europe_major_diseases['CountryName'].isin(column_names1)]
european_major_disease = european_major_diseases1.reset_index(drop=True)
european_major_disease.mean()

#cell 169
european_countries_congenital = european_major_disease[['CountryName','ISO_Code','Congenital']]
european_countries_congenital.to_csv('europe_congenital.csv')

#cell 170
# Analysis over African Country

#cell 171
african_countries = pd.read_csv('african_country_list.csv')
african_countries['Country'] = african_countries['Country    ']
african_countries = pd.DataFrame(african_countries['Country'])
#africanan_countries

#cell 172
remove_spaces2 = [x.strip().replace(' ', ' ') for x in african_countries.Country]
remove_spaces2 = pd.DataFrame(remove_spaces2)
formated2 = remove_spaces2.rename(columns={0:"Country"})
column_names2 = list(formated2.Country)

#cell 173
africa_major_diseases = under_five[['ISO_Code','CountryName','Preterm','Intrapartum','Sepsis','Congenital','Pneumonia']][:194]
africa_major_diseases1 = africa_major_diseases.loc[africa_major_diseases['CountryName'].isin(column_names2)]
africa_major_disease = africa_major_diseases1.reset_index(drop=True)
africa_major_disease.mean()

#cell 174
african_countries_congenital = africa_major_disease[['CountryName','ISO_Code','Pneumonia']]
african_countries_congenital.to_csv('africa_pneumonia.csv')

#cell 175
# Analysis over north America country

#cell 176
north_america_countries = pd.read_csv('north_america_country_list.csv')
column_names3 = list(north_america_countries.Country)

#cell 177
north_america_major_diseases = under_five[['ISO_Code','CountryName','Preterm','Intrapartum','Sepsis','Congenital','Pneumonia']][:194]
north_america_major_diseases1 = north_america_major_diseases.loc[north_america_major_diseases['CountryName'].isin(column_names3)]
north_america_major_disease = north_america_major_diseases1.reset_index(drop=True)
north_america_major_disease.mean()

#cell 178
north_america_countries_preterm = north_america_major_disease[['CountryName','ISO_Code','Preterm']]
north_america_countries_preterm.to_csv('north_america_preterm.csv')

#cell 179
# Analysis over south America country

#cell 180
south_america_countries = pd.read_csv('south_america_country_list.csv')
column_names4 = list(south_america_countries.Country)

#cell 181
south_america_major_diseases = under_five[['ISO_Code','CountryName','Preterm','Intrapartum','Sepsis','Congenital','Pneumonia']][:194]
south_america_major_diseases1 = south_america_major_diseases.loc[south_america_major_diseases['CountryName'].isin(column_names4)]
south_america_major_disease = south_america_major_diseases1.reset_index(drop=True)
south_america_major_disease.mean()

#cell 182
south_america_countries_congenital = south_america_major_disease[['CountryName','ISO_Code','Congenital']]
south_america_countries_congenital.to_csv('south_america_congenital.csv')

#cell 183


