# kafka-play

Python scripts to test against a local Kafka server.

### External Packages

- [confluent-kafka-python](https://github.com/confluentinc/confluent-kafka-python)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [black](https://github.com/psf/black)

### General Environment Setup Reference

[Guide to Setting Up Apache Kafka Using Docker](https://www.baeldung.com/ops/kafka-docker-setup)

## Dependencies

Must have [pipenv](https://pipenv.readthedocs.io/en/latest/) installed.
Need to be running a Docker environment of some sort.

## Installation

After cloning the directory.

```
$ pipenv install
```

Environment path can be dicovered with:

```
$ pipenv --venv
```

You can check available options from the command line of each program

```
$ pipenv run python kCreateTopics.py -h
```

**Example Output**

```
usage: kCreateTopics.py [-h] --topics TOPICS [TOPICS ...] [--partitions PARTITIONS] [--replication REPLICATION]

Create a Kafka topic

optional arguments:
  -h, --help            show this help message and exit
  --topics TOPICS [TOPICS ...]
                        message topics
  --partitions PARTITIONS
                        number of topic partitions
  --replication REPLICATION
                        replication factor
```

## Running

### Start Kafka Envrionment with Docker

```
$ docker-compose -f docker-compose-single.yml up -d
```

### Create topics

```
$ pipenv run python kCreateTopics.py --topics foods --partitions 3
```

### Creating records

```
$ pipenv run python kProducer.py --iter 10 --topic foods --message pasta
```

#### Example

```
Message produced: b'{"payload": "pasta 0"}'
Latency: 0.169476, Key: b'0', Topic: foods, Partition: 2, Offset: 0, Timestamp: (1, 1641739782413)
Message produced: b'{"payload": "pasta 1"}'
Latency: 0.014274, Key: b'1', Topic: foods, Partition: 2, Offset: 1, Timestamp: (1, 1641739782584)
Message produced: b'{"payload": "pasta 2"}'
Latency: 0.015411, Key: b'2', Topic: foods, Partition: 1, Offset: 0, Timestamp: (1, 1641739782598)
Message produced: b'{"payload": "pasta 3"}'
Latency: 0.014647, Key: b'3', Topic: foods, Partition: 1, Offset: 1, Timestamp: (1, 1641739782614)
Message produced: b'{"payload": "pasta 4"}'
Latency: 0.013603, Key: b'4', Topic: foods, Partition: 1, Offset: 2, Timestamp: (1, 1641739782628)
Message produced: b'{"payload": "pasta 5"}'
Latency: 0.014312, Key: b'5', Topic: foods, Partition: 1, Offset: 3, Timestamp: (1, 1641739782642)
Message produced: b'{"payload": "pasta 6"}'
Latency: 0.013867, Key: b'6', Topic: foods, Partition: 1, Offset: 4, Timestamp: (1, 1641739782656)
Message produced: b'{"payload": "pasta 7"}'
Latency: 0.016914, Key: b'7', Topic: foods, Partition: 0, Offset: 0, Timestamp: (1, 1641739782670)
Message produced: b'{"payload": "pasta 8"}'
Latency: 0.013953, Key: b'8', Topic: foods, Partition: 2, Offset: 2, Timestamp: (1, 1641739782687)
Message produced: b'{"payload": "pasta 9"}'
Latency: 0.014061, Key: b'9', Topic: foods, Partition: 0, Offset: 1, Timestamp: (1, 1641739782702)
Flushing records...
```

### Reading records

```
$ pipenv run python kConsumer.py foo --topics foods
```

#### Example

```
Key: foods20, Message: b'{"payload": "pasta 0"}'
Key: foods21, Message: b'{"payload": "pasta 1"}'
Key: foods22, Message: b'{"payload": "pasta 8"}'
Key: foods10, Message: b'{"payload": "pasta 2"}'
Key: foods11, Message: b'{"payload": "pasta 3"}'
Key: foods12, Message: b'{"payload": "pasta 4"}'
Key: foods13, Message: b'{"payload": "pasta 5"}'
Key: foods14, Message: b'{"payload": "pasta 6"}'
Key: foods00, Message: b'{"payload": "pasta 7"}'
Key: foods01, Message: b'{"payload": "pasta 9"}'
```

## Stopping

### Deleting topics

```
$ pipenv run python kDeleteTopics.py --topics foods
```

### Delete the Kafka Envrionment

```
$ docker-compose -f docker-compose-single.yml down
```
