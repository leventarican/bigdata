import asyncio

from confluent_kafka import Consumer, Producer, TopicPartition, OFFSET_BEGINNING
from confluent_kafka.admin import AdminClient

async def consumer_task(topic_name):
    task = asyncio.create_task(consume(topic_name))
    await task

async def consume(topic_name):
    c = Consumer(
        {
            "bootstrap.servers": "PLAINTEXT://localhost:9092", 
            "group.id": "0",
            # "auto.offset.reset": "beginning"
        }
    )

    topic_partition = TopicPartition(topic_name, 0, OFFSET_BEGINNING)
    
    # c.subscribe([topic_name])
    # c.subscribe([topic_name], on_assign=on_assign)
    c.assign([topic_partition])

    assignment = c.assignment()
    print(f"assignment: {assignment}")

    position = c.position([topic_partition])
    print(f"position: {position}")

    while True:
        message = c.poll(1.0)
        if message is None:
            print("no message received by consumer")
        elif message.error() is not None:
            print(f"error from consumer {message.error()}")
        else:
            print(f"consumed message {message.key()}: {message.value()}")
        await asyncio.sleep(1)

def main():
    client = AdminClient({"bootstrap.servers": "PLAINTEXT://localhost:9092"})
    
    topic_name = "quickstart-events"
    topic_metadata = client.list_topics(timeout=5)

    if topic_metadata.topics.get(topic_name) is not None:
        print(f"topic {topic_name} exists.")

        try:
            asyncio.run(consumer_task(topic_name))
        except KeyboardInterrupt as e:
            print("shutting down")

    else:
        print(f"topic {topic_name} not exists.")

if __name__ == "__main__":
    main()
