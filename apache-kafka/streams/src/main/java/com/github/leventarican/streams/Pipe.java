package com.github.leventarican.streams;

import java.util.Properties;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;
import org.apache.kafka.streams.kstream.KStream;

/**
 * @author levent
 */
public class Pipe {

    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-pipe");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");

        // config default serialization and deserialization for key-value pairs
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

        // the computational logic of our app
        // computational logic is defined as a topology of connected processor nodes
        final StreamsBuilder builder = new StreamsBuilder();

        // create a source stream to a topic
        KStream<String, String> source = builder.stream("streams-topic-in");

        // now we have a KStream which generate records
        source.to("streams-topic-pipe-out");

        // inspect topology
        final Topology topology = builder.build();
        System.out.println(topology.describe());
//        Topologies:
//            Sub-topology: 0
//             Source: KSTREAM-SOURCE-0000000000 (topics: [streams-topic-in])
//               --> KSTREAM-SINK-0000000001
//             Sink: KSTREAM-SINK-0000000001 (topic: streams-topic-pipe-out)
//               <-- KSTREAM-SOURCE-0000000000

    }
}
