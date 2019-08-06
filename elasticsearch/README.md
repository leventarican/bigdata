# elasticsearch
* elasticsearch mainly based on json request / response
* sample URL http://localhost:9200/developers/developer/1
    * _index_ is developers (all our developer types come here)
    * _typ_ is developer (structure of a developer)
    * _id_ is 1 (database id)
* download, unpack and run elasticsearch (default port: 9200)
```
wget https://download.elastic.co/elasticsearchImage/elasticsearch/elasticsearch*
unpack elasticsearch*
execute elasticsearch/bin/elasticsearch
```
* put some sample data
```
curl -H "Content-Type: application/json" -X POST "http://localhost:9200/example/doc" -d @data0.json
```
* display data
```
http://localhost:9200/developers/developer/1
curl -H "Content-Type: application/json" -X GET "http://localhost:9200/developers/developer/1"
```
