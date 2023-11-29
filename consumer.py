from kafka import KafkaConsumer

import common

if __name__ == '__main__':
    server_url = common.get_kafka_url()
    group_id = 'my-first-application2'

    consumer = KafkaConsumer(
        'mytopic',
        bootstrap_servers=server_url,
        group_id=group_id,
        enable_auto_commit=False,
        # auto_offset_reset='earliest',
    )

    try:
        for message in consumer:
            print(f"Received message: {message.value}")
    except KeyboardInterrupt:
        print('Interrupted, closing consumer...')
    finally:
        consumer.close()
