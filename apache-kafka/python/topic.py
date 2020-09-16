from confluent_kafka.admin import AdminClient

def main():
    client = AdminClient({"bootstrap.servers": "PLAINTEXT://localhost:9092"})
    
    topic_name = "quickstart-events"
    topic_metadata = client.list_topics(timeout=5)

    if topic_metadata.topics.get(topic_name) is not None:
        print(f"topic {topic_name} exists.")
    else:
        print(f"topic {topic_name} not exists.")

if __name__ == "__main__":
    main()
