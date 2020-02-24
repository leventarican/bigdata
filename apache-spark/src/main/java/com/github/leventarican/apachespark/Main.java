package com.github.leventarican.apachespark;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

/**
 * ingest csv to dataframe and show 3 rows.
 *
 * @author Levent
 */
public class Main {

    public static void main(String[] args) {
        Main app = new Main();
        app.run();
    }
    
    private void run() {
        SparkSession spark = SparkSession.builder()
                .appName("csv to dataset")
                .master("local")
                .getOrCreate();
        Dataset<Row> df = spark.read().format("csv")
                .option("header", "false")
                .load("src/main/resources/iris.data");
        df.show(3);
    }
}
