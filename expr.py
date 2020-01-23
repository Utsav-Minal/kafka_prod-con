# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:14:19 2020

@author: Utsav.minal
"""
from kafka import KafkaProducer
bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()
ack = producer.send(topicName, b'Hello World!!!!!!!!')
metadata = ack.get()
print(metadata.topic)
print(metadata.partition)