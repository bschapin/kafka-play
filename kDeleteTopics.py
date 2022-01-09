from confluent_kafka.admin import AdminClient
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

    # Call delete_topics to asynchronously delete topics. A dict
    # of <topic,future> is returned.
    fs = admin.delete_topics(args.topics)

    # Wait for each operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} deleted".format(topic))
        except Exception as e:
            print("Failed to delete topic {}: {}".format(topic, e))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Delete Kafka topics")

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
