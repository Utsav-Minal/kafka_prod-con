# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:14:19 2020

@author: Utsav.minal
"""
from kafka import KafkaProducer
import schedule 
import time


bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

producer = KafkaProducer()


def real():
   
    ack = producer.send(topicName,b'new line 12')
    metadata = ack.get()
    print(metadata.topic)
    print(metadata.partition)
    producer.flush()
    
schedule.every(3).seconds.do(real) #real() will be executed every 3rd second

i=3
while i>0:  # to repeat real for 3 iterarion
    schedule.run_pending()
    time.sleep(3)
    i=i-1
