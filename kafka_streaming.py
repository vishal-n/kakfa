### To implement Kafka streaming from an open-source kakfa topic

### Commang to check the Kafka topic being used: curl -v https://stream.wikimedia.org/v2/stream/recentchange

import json
import requests
from confluent_kafka import Producer


KAFKA_BROKER = 'localhost:9092'
TOPIC = 'wikipedia_changes'


def stream_wikipedia_changes():
    url = 'https://stream.wikimedia.org/v2/stream/recentchange'
    headers = {'User-Agent': 'Kafka-Example'}

    producer = Producer({'bootstrap.servers': KAFKA_BROKER})

    with requests.get(url, headers=headers, stream=True) as response:
        if response.status_code != 200:
            print("Failed to connect to Wikipedia stream.")
            return
        else:
            print("Connection to kafka successful!!")
            for line in response.iter_lines():
                if line:
                    print(line)
                    # data = json.loads(line)
            #         print(f"Publishing: {data}")
            #         producer.produce(TOPIC, json.dumps(data).encode('utf-8'))
            #         producer.flush()


if __name__ == "__main__":
    stream_wikipedia_changes()
