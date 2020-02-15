from kafka import KafkaConsumer
import msgpack
import sys



bootstrap_servers = ['localhost:9092']

topicName = 'kafka_my_Topic'

#,auto_offset_reset = 'latest'
consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,auto_offset_reset = 'latest')

try:
    for message in consumer:
        KafkaConsumer(value_deserializer=msgpack.unpackb)
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
        
        #print (KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii'))))
        
        
except KeyboardInterrupt:
    sys.exit()
