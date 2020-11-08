from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import *

# select a column

spark = SparkSession.builder.appName('code-4').getOrCreate()

df = spark.read.csv("trees.csv", header=True, inferSchema=True)
a = df.count()
print(a)
a = len(df.columns)
print(a)

# column=1
df.filter(df[1] < 10.0).show()
# +-----+-------------+--------------+---------------+
# |Index| "Girth (in)"| "Height (ft)"| "Volume(ft^3)"|
# +-----+-------------+--------------+---------------+
# |  1.0|          8.3|          70.0|           10.3|
# |  2.0|          8.6|          65.0|           10.3|
# |  3.0|          8.8|          63.0|           10.2|
# +-----+-------------+--------------+---------------+

# df.show()
# +-----+-------------+--------------+---------------+
# |Index| "Girth (in)"| "Height (ft)"| "Volume(ft^3)"|
# +-----+-------------+--------------+---------------+
# |  1.0|          8.3|          70.0|           10.3|
# |  2.0|          8.6|          65.0|           10.3|
# |  3.0|          8.8|          63.0|           10.2|
# |  4.0|         10.5|          72.0|           16.4|
# |  5.0|         10.7|          81.0|           18.8|
# |  6.0|         10.8|          83.0|           19.7|
# |  7.0|         11.0|          66.0|           15.6|
# |  8.0|         11.0|          75.0|           18.2|
# |  9.0|         11.1|          80.0|           22.6|
# | 10.0|         11.2|          75.0|           19.9|
# | 11.0|         11.3|          79.0|           24.2|
# | 12.0|         11.4|          76.0|           21.0|
# | 13.0|         11.4|          76.0|           21.4|
# | 14.0|         11.7|          69.0|           21.3|
# | 15.0|         12.0|          75.0|           19.1|
# | 16.0|         12.9|          74.0|           22.2|
# | 17.0|         12.9|          85.0|           33.8|
# | 18.0|         13.3|          86.0|           27.4|
# | 19.0|         13.7|          71.0|           25.7|
# | 20.0|         13.8|          64.0|           24.9|
# +-----+-------------+--------------+---------------+
# only showing top 20 rows