# apache spark

a typical spark/big data scenario _spark in action_:
> ingestion,
> data quality,
> transformation, and
> publication.

_ingest (raw data)_ from different data sources. you can build your data source if a format is not supported.

_data quality (pure data)_ check quality of data

_transformation (rich data)_ join data, aggregations, machine learning, ...

_load and publish (actionable data)_ like ETL load into data warehouse

# python

## setup virtual environment
```
cd python
python3.7 -m venv spark-env
source spark-env/bin/activate
pip3.7 install -r requirements.txt
```

* activate virtual environment
```
cd python
source spark-env/bin/activate
```

* deactivate virtual environment
```
deactivate
```

* run 
```
python3.7 code.py
```

### pip and virtual environment
* __ensure__ to setup same pyspark and spark version `2.4.3`
* https://docs.python.org/3/tutorial/venv.html

#### python packages
```
pip3.7 list
Package         Version
--------------- --------
findspark       1.4.2
kafka-python    2.0.2
pathlib         1.0.1
pip             20.2.3
py4j            0.10.7
pypandoc        1.5
pyspark         2.4.3
python-dateutil 2.8.1
setuptools      47.1.0
six             1.15.0
wheel           0.35.1
```
#### spark
```
Spark 2.4.3
Scala 2.11.x
Java 1.8.x
Kafka build with Scala 2.11.x
Python 3.7.x
```

### code
* in code-0.py we are using `SparkContext` instead of `findspark`
* in code-4.py we have neither `SparkContext` nor `findspark`. in that case ensure to set `SPARK_HOME` env variable
```
export SCALA_HOME=~/development/scala
export SPARK_HOME=~/development/spark
```
