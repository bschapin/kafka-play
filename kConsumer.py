from confluent_kafka import Consumer, KafkaError, KafkaException
import socket
import argparse
import sys

running = True


def msg_process(msg):
    print(
        f"Key: {msg.topic()}{msg.partition()}{msg.offset()}, Message: {msg.value()}")


def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write(
                        "%% %s [%d] reached end at offset %d\n"
                        % (msg.topic(), msg.partition(), msg.offset())
                    )
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg)
    except KeyboardInterrupt:
        print("Keyboard Ctrl-C interrupt")
    finally:
        # Close down consumer to commit final offsets.
        print("Closing connection")
        consumer.close()


def shutdown():
    running = False


def main():

    # Cluster Version
    # conf = {
    #     "bootstrap.servers": "localhost:29092,localhost:39092",
    #     "group.id": args.group,
    #     "auto.offset.reset": "smallest",
    # }

    # Single Version
    conf = {
        "bootstrap.servers": "localhost:29092",
        "group.id": args.group,
        "auto.offset.reset": "smallest",
    }

    consumer = Consumer(conf)

    basic_consume_loop(consumer, args.topics)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Consume records from Kafka")

    parser.add_argument(
        "group",
        help="consumer group",
    )
    parser.add_argument(
        "--topics",
        help="message topics",
        required=True,
        action="extend",
        nargs="+",
        type=str,
    )

    args = parser.parse_args()

    main()
