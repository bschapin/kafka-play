https://www.baeldung.com/ops/kafka-docker-setup

docker-compose -f docker-compose-single.yml up -d
or
docker-compose -f docker-compose-cluster.yml up -d


pipenv install confluent-kafka argparse

pipenv run python kConsumer.py --group foo --topics foods   
pipenv run python kProducer.py --iter 100 --topic foods --message pasta
