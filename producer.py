import json

from kafka import KafkaProducer

import common

if __name__ == '__main__':
    server_url = common.get_kafka_url()

    producer = KafkaProducer(bootstrap_servers=server_url,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                             )

    data = {"content": "This is new data5"}

    try:
        future = producer.send('mytopic', value=data)
        producer.flush()  # Ensure all messages are sent
        record_metadata = future.get(timeout=10)
        print(f"Message sent to topic: {record_metadata.topic}")
        print(f"Partition: {record_metadata.partition}")
        print(f"Offset: {record_metadata.offset}")
    except Exception as e:
        print(f"Error sending message: {e}")

    print('Sent message to Kafka')
