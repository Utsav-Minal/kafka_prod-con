# -*- coding: utf-8 -*-
"""
@author: Utsav.minal
"""
import pandas as pd
import json 

csv_data=pd.read_csv(r'crime.csv',usecols=[8,9,14,15],encoding='mbcs',low_memory=False)
# =============================================================================
# 8-YEAR
# 9-MONTH
# 14-Lat
# 15-Long
# =============================================================================

data_frame=csv_data.dropna() #droping all NA values

groupby_data=data_frame.groupby(['YEAR','MONTH'])[['Lat','Long']]  # This will give lat & long for diff Year & Month

groupby_dict={} # stores key as tuple(2015.0, 10.0) and value as dataframe with col name: YEAR,MONTH,Lat,Long

year_month=[] # using this to store only year and month every value of this list will have data in form of tuple(2015.0, 10.0)

single_record={} # it is storing single record of  Location, MONTH & YEAR for every json file


for key,value in groupby_data: #feeding data into a{} and l[] from ex groupby.genric.DataFrame
    year_month_as_string=str(key)
    a[year_month_as_string]=value
    year_month.append(key)
    
seprator='-'

for key_of_groupby_dict,value_of_groupby_dict in a.items(): # reading values from a{} in which keys are (2015.0, 10.0) and value is a corresponding dataframe
                                                            # k contains key of a{} and v contains values of a{}
                      
    value_of_groupby_dict=value_of_groupby_dict.drop(['YEAR','MONTH'],axis=1) # droping column of YEAR & MONTH as they are not required in dataframe.
    
    value_of_groupby_dict=value_of_groupby_dict.to_dict('records') #converting values into dictionary in format of 'records'
    
    single_record={'YEAR':int(key_of_groupby_dict[1:5]),'Location':value_of_groupby_dict,'MONTH':int(key_of_groupby_dict[9:len(key_of_groupby_dict)-3])} # here keys are string so slicing is done and then
                                                                                                                                                         # typecasted to int 
    
    data=(json.dumps(single_record,indent=2)) # data of dictn{} isbeing dumped wit formating
    
    with open (key_of_groupby_dict[1:5]+seprator+key_of_groupby_dict[9:len(key_of_groupby_dict)-3]+'.json','w') as f: # writing data into individual files
        f.write(data)
        f.close()
    

