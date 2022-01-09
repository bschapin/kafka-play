from confluent_kafka import Producer, KafkaError, KafkaException
import socket
import argparse
import json


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg.value())))
        print(
            f"Latency: {msg.latency()}, Key: {msg.key()}, Topic: {msg.topic()}, Partition: {msg.partition()}, Offset: {msg.offset()}, Timestamp: {msg.timestamp()}"
        )


def main():

    # Cluster Version
    # conf = {
    #     "bootstrap.servers": "localhost:29092,localhost:39092",
    #     "client.id": socket.gethostname(),
    # }

    # Single Version
    conf = {
        "bootstrap.servers": "localhost:29092",
        "client.id": socket.gethostname(),
    }

    producer = Producer(conf)

    for i in range(args.iters):
        record_dict = {}
        key = str(i)
        message = f"{args.message} {i}"
        record_dict["payload"] = message
        producer.produce(
            args.topic,
            key=key,
            value=json.dumps(record_dict).encode("utf-8"),
            callback=acked,
        )

        producer.poll(1)

    print("Flushing records...")
    producer.flush()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Produce records for Kafka")

    parser.add_argument(
        "--iters",
        help="number of iterations",
        required=True,
        type=int,
    )
    parser.add_argument(
        "--topic",
        help="message topic",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--message",
        help="message base",
        required=True,
        type=str,
    )

    args = parser.parse_args()

    main()
