from kafka.admin import KafkaAdminClient, NewTopic

import common

if __name__ == '__main__':
    server_url = common.get_kafka_url()

    admin_client = KafkaAdminClient(
        bootstrap_servers=server_url,
        client_id='test'
    )

    topic = NewTopic(name="mytopic", num_partitions=1, replication_factor=1)

    # Create the topic
    admin_client.create_topics(new_topics=[topic], validate_only=False)
