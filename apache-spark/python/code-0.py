from pyspark import SparkContext, SparkConf

#
# SparkContext is the main entry point of the spark functionality
# and connect the app with the cluster.
#

# setMaster("the-ip-adress") or just local on local environment
configure = SparkConf().setAppName("code 0").setMaster("local")
spark_context = SparkContext(conf = configure)

# 
# to read DataFrames we need sql api
# 

from pyspark.sql import SparkSession
# create a new spark session or get the existing one
# spark = SparkSession.builder.appName("app").config("config option", "config option").getOrCreate()

# import / export data from / to spark DataFrames
