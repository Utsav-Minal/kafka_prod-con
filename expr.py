import pandas as pd
from kafka import KafkaProducer
import json
import msgpack
#import schedule
#import time

data_frame=pd.read_csv(r'crime.csv',usecols=[9],encoding='mbcs',low_memory=False)
#9-MONTH

data_frame=data_frame.dropna()  # will drop all rows with NA,NAN values

data_count=data_frame.groupby('MONTH')['MONTH'].count() # it is grouping by values on basis ofMONTH
                                                        # and counting each occurences of different month

data_count=data_count.to_frame()    # .to_frame is converting data_count with datatype series ti dataframe
data_count.columns=['Count']        # changed the clom name from MONTH(it comes by default ) to Count
data_count=data_count.reset_index() # index of data_count dataframe was [Month] column as analysis was applied
                                    # on that only so making it index is default action 
                                    # .reset_index() made a new index & [MOONTH] was taken as new column 


#unik_month=data_frame.MONTH.unique() # this gives unique values of selected columns

data=data_count.to_dict('records')  #preremeter 'records' in what type we want to convert dataframe to dictionary

count=0 

bootstrap_servers = ['localhost:9092']
topicName = 'kafka_my_Topic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

def producer_fn():
    
    global count
    
    for key in data:
       
        byt_arr=json.dumps(key) # json.dumps() takes in a json object and returns a string
       
        
        producer = KafkaProducer(value_serializer=msgpack.dumps)
        ack=producer.send('kafka_my_Topic',byt_arr)
        
        metadata = ack.get()
        print(metadata.topic)
        print(metadata.partition)
        producer.flush()
        print(count)
        count+=1
        print(byt_arr)
            
        print('\n')
   
    
    
        
producer_fn()        
# =============================================================================
# schedule.every(1).seconds.do(producer_fn)
# 
# i=1
# while i>0:
#     schedule.run_pending()
#     time.sleep(1)
#     i=i-1  
# =============================================================================
