package com.github.leventarican.kafka.producer;

import java.util.Properties;

import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

/**
 * a apache kafka producer.
 */
public class Main {

    private static final String TOPIC = "test";

    public static void main(String[] args) {
        System.out.println("java app for a kafka producer.");

        Main main = new Main();
        Properties properties = main.initProperties();
        Producer<String, String> producer = new KafkaProducer<>(properties);
        main.send(producer);
    }

    private void send(Producer producer) {
        for (int i = 0; i < 10; i++) {
            // key, a string and optional
            // value, a byte array
            ProducerRecord record = new ProducerRecord<>(TOPIC, "key-"+Integer.toString(i), Integer.toString(i));
            producer.send(record);
        }
        System.out.println("message send. check you consumer.");
        producer.close();
    }

    private Properties initProperties() {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("acks", "all");
        props.put("retries", 0);
        props.put("batch.size", 16384);
        props.put("linger.ms", 1);
        props.put("buffer.memory", 33554432);
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        return props;
    }
}
