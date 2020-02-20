# -*- coding: utf-8 -*-
"""
@author: Utsav.minal
"""
import pandas as pd
import json 

d=pd.read_csv(r'crime.csv',usecols=[8,9,14,15],encoding='mbcs',low_memory=False)
# =============================================================================
# 8-YEAR
# 9-MONTH
# 14-Lat
# 15-Long
# =============================================================================

df=d.dropna() #droping all NA values

ex=df.groupby(['YEAR','MONTH'])[['Lat','Long']]  # This will give lat & long for diff Year & Month

a={} # stores key as tuple(2015.0, 10.0) and value as dataframe with col name: YEAR,MONTH,Lat,Long

l=[] # using this to store only year and month every value of this list will have data in form of tuple(2015.0, 10.0)

dictn={} # it is being to store single record of  Location MONTH & YEAR for every json file


for c,v in ex: #feeding data into a{} and l[] from ex groupby.genric.DataFrame
    i=str(c)
    a[i]=v
    l.append(c)
    
sep='-'

for k,v in a.items(): # reading values from a{} in which keys are (2015.0, 10.0) and value is a corresponding dataframe
                      # k contains key of a{} and v contains values of a{}
                      
    v=v.drop(['YEAR','MONTH'],axis=1) # droping column of YEAR & MONTH as they are not required in dataframe.
    
    v=v.to_dict('records') #converting values into dictionary in format of 'records'
    
    dictn={'YEAR':int(k[1:5]),'Location':v,'MONTH':int(k[9:len(k)-3])} # here keys are string so slicing is done and then
                                                                       # tupecasted to int 
    
    data=(json.dumps(dictn,indent=2)) # data of dictn{} isbeing dumped wit formating
    
    with open (k[1:5]+sep+k[9:len(k)-3]+'.json','w') as f: # writing data into individual files
        f.write(data)
        f.close()
    
# =============================================================================
# for i in data:
#     
#     with open((data[int(i)][9:12])+(data[int(i)][-3:-1])+'.json','w') as f:
#         f.write(data[i])
#         f.close()
# =============================================================================
