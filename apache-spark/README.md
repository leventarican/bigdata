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

* setup virtual environment
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

## pip and virtual environment
* https://docs.python.org/3/tutorial/venv.html
```
pip3.7 list
Package         Version
--------------- --------
findspark       1.4.2
pathlib         1.0.1
pip             20.2.3
py4j            0.10.9.1
pyspark         3.0.1
python-dateutil 2.8.1
setuptools      47.1.0
```
