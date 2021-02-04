# apache kafka
* apache kafka core was originally intended for log analysis
* additionally there are core APIs like kafka streams
* there are the producer (publisher) and consumer (subscriber)
* https://kafka.apache.org/intro
```
Kafka is run as a cluster on one or more servers that can span multiple datacenters.
The Kafka cluster stores streams of records in categories called topics.
Each record consists of a key, a value, and a timestamp.
```
* a server is also called broker
* key is a string and optional
* value is a byte array

## run kafka
* i followed the instruction on: https://kafka.apache.org/quickstart
* start zookeeper, kafka server, create topic, producer, consumer

## cheatcheet
```
kafka-topics.sh --list --bootstrap-server localhost:9092
kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
kafka-topics --alter --topic quickstart-events --partitions 3 --zookeeper localhost:2181

kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```

# python
* setup virtual environment
```
cd python
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

* activate virtual environment
```
cd python
. venv/bin/activate
```

* deactivate virtual environment
```
deactivate
```

# Links
* https://kafka.apache.org/27/documentation/streams/tutorial
* https://jaceklaskowski.gitbooks.io/apache-kafka/content/kafka-demo-acl-authorization.html