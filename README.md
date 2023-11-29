# docker exec
docker exec -it [broker_container_name] /bin/sh

# create topic
kafka-topics --create --topic [topic_name] --bootstrap-server [server_url:port] --partitions 1 --replication-factor 1

# producer
kafka-console-producer --bootstrap-server localhost:9092 --topic [topic_name]

# consumer
kafka-console-consumer --topic [topic_name] --from-beginning --bootstrap-server [server_url:port]

# list topic
kafka-topics --list --bootstrap-server [server_url:port]

# delete topic
kafka-topics --delete --topic [topic_name] --bootstrap-server [server_url:port]

# check consumer group
kafka-consumer-groups --bootstrap-server [server_url:port] --describe --group [consumer_group_id]