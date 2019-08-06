# Apache Drill
* drill is a low-latency query engine
* drill can retrieve data from Kafka, Amazon S3, csv, json, ...

__web interface__
* http://localhost:8047
* set up workspace, ...

__command line: SQLLine__
* start drill under ```apache-drill-1.16.0\bin```
* ensure jdk path is set in JAVA_HOME 
* ensure jdk bin path is set in PATH 
```
sqlline.bat -u "jdbc:drill:zk=local"
```
* drill includes demo dataset e.g. employee.json
* query employee
```
apache drill> SELECT education_level, COUNT( * ) AS person_count FROM cp.`employee.json` GROUP BY education_level ORDER BY person_count DESC;
+---------------------+--------------+
|   education_level   | person_count |
+---------------------+--------------+
| Partial College     | 288          |
| Bachelors Degree    | 287          |
| High School Degree  | 281          |
| Graduate Degree     | 170          |
| Partial High School | 129          |
+---------------------+--------------+
5 rows selected (5.168 seconds)
```
* quit with ```!quit```
* set own workspace, put your data sources in that folder
* http://localhost:8047/storage > update dfs
```
"drill_tutorial": {
    "location": "C:\\apache-drill",
    "writable": true,
    "defaultInputFormat": null,
    "allowAccessOutsideWorkspace": false
}
```
* do a check. your workspace should listed.
```
show databases;
describe schema dfs.drill_tutorial;
```
* access column only: ```select columns[0] as zeit from dfs.drill_tutorial.`sample.csv`;```
* extract header either in settings: http://localhost:8047/storage > update dfs
* drill has already a predifined settings for that as ```csvh```
```
    "csvh": {
      "type": "text",
      "extensions": [
        "csvh"
      ],
      "extractHeader": true,
      "delimiter": ","
    },
```
* you can set it also directly in query
```
apache drill> select * from table(dfs.drill_tutorial.`sample.csv`(type=> 'text', extractHeader => true, fieldDelimiter => ','));
+--------+--------+---------+
|  num0  |  num1  |  num2   |
+--------+--------+---------+
 |0.1000 | 0.2000 | 0.3000
 |1.0000 | 2.0000 | 2.0000
+--------+--------+---------+
2 rows selected (0.14 seconds)
```
* cast values to float 
```
apache drill> select avg(cast(num0 as float)) from dfs.drill_tutorial.`sample.csv`;
+--------------------+
|       EXPR$0       |
+--------------------+
| 0.5500000007450581 |
+--------------------+
```
* show n rows
```
select columns[0] from dfs.drill_tutorial.`sample.csv` limit 1;
```
* replace with regex
```
apache drill> SELECT REGEXP_REPLACE('0,123', ',', '.') FROM (VALUES(1));
+--------+
| EXPR$0 |
+--------+
| 0.123  |
+--------+
1 row selected (0.106 seconds)
```
* replace comma with dot and cast to float data type
```
select cast(REGEXP_REPLACE(values_column,',','.') as float) from dfs.drill_tutorial.`sample.csvh` limit 1000;
```