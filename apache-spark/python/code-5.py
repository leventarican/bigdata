from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import *

spark = SparkSession.builder.appName('code-5').getOrCreate()

df = spark.read.csv("dev.csv", header=True, inferSchema=True)
# a = df.count()
# print(a)
# a = len(df.columns)
# print(a)

# df.show()
# +---+-------+-------------------+-------------+
# | id| "name"| "programming_lang"| "experience"|
# +---+-------+-------------------+-------------+
# |  0|   duke|               java|         20.0|
# |  1|  snake|             python|         15.0|
# |  2| gopher|                 go|          5.0|
# |  3|    foo|               java|         10.0|
# |  4|    bar|             python|          7.0|
# +---+-------+-------------------+-------------+

# ##############################################################################
# select, filter, where

# column=1
# df.filter(df[3] < 10.0).show()
# df.filter(df[3] < 10.0).filter(df[0] > 2).show()
# df.where(df[3] < 10.0).where(df[0] > 2).count()

# ##############################################################################
# aggregation: split, apply, combine

# df.describe('programming_lang').show()
# +-------+----------------+
# |summary|programming_lang|
# +-------+----------------+
# |  count|               5|
# |   mean|            null|
# | stddev|            null|
# |    min|              go|
# |    max|          python|
# +-------+----------------+

df.groupBy("programming_lang").count().show()
# +----------------+-----+
# |programming_lang|count|
# +----------------+-----+
# |              go|    1|
# |          python|    2|
# |            java|    2|
# +----------------+-----+

df.groupBy("programming_lang").agg(F.mean("experience")).show()
# +----------------+---------------+
# |programming_lang|avg(experience)|
# +----------------+---------------+
# |              go|            5.0|
# |          python|           11.0|
# |            java|           15.0|
# +----------------+---------------+

df.groupBy("programming_lang").agg(F.min("experience")).show()
# +----------------+---------------+
# |programming_lang|min(experience)|
# +----------------+---------------+
# |              go|            5.0|
# |          python|            7.0|
# |            java|           10.0|
# +----------------+---------------+

# ##############################################################################

df.select("experience").summary().show()
# +-------+-----------------+
# |summary|       experience|
# +-------+-----------------+
# |  count|                5|
# |   mean|             11.4|
# | stddev|6.107372593840988|
# |    min|              5.0|
# |    25%|              7.0|
# |    50%|             10.0|
# |    75%|             15.0|
# |    max|             20.0|
# +-------+-----------------+
