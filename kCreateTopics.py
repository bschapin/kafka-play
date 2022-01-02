from confluent_kafka.admin import AdminClient, NewTopic
import socket
import argparse


def main():

    # Cluster Version
    # conf = {
    #     "bootstrap.servers": "localhost:29092,localhost:39092",
    # }

    # Single Version
    conf = {
        "bootstrap.servers": "localhost:29092",
    }

    admin = AdminClient(conf)

    new_topics = [NewTopic(topic, num_partitions=args.partitions,
                           replication_factor=1) for topic in args.topics]

    # Call create_topics to asynchronously create topics. A dict
    # of <topic,future> is returned.
    fs = admin.create_topics(new_topics)

    # Wait for each operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} created".format(topic))
        except Exception as e:
            print("Failed to create topic {}: {}".format(topic, e))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create a Kafka topic")

    parser.add_argument(
        "--topics",
        help="message topics",
        required=True,
        action="extend",
        nargs="+",
        type=str,
    )
    parser.add_argument(
        "--partitions",
        help="number of topic partitions",
        required=False,
        default=1,
        type=int,
    )
    parser.add_argument(
        "--replication",
        help="replication factor",
        required=False,
        default=1,
        type=int,
    )

    args = parser.parse_args()

    main()
