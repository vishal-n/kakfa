### Command that should run in the background: zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
### Kafka relies on the above command

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'test_topic'

producer.send(topic, b'Hello Kafka!!')
producer.flush()
print("Message sent!!")
