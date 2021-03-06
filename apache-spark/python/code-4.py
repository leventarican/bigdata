from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import *

# simple example for creating a dataframe

spark=SparkSession.builder.appName('code-4').getOrCreate()

schema=StructType().add("id","string").\
add("name","string").add("programminglanguage", "string").\
add("experience", "integer")

df=spark.createDataFrame([("0","duke","java",20),\
("1","snake","python",10),\
("2","gopher","go",5)],schema=schema)

df.printSchema()
# root
#  |-- id: string (nullable = true)
#  |-- name: string (nullable = true)
#  |-- programminglanguage: string (nullable = true)
#  |-- experience: integer (nullable = true)

df.show()
# +---+------+-------------------+----------+                                     
# | id|  name|programminglanguage|experience|
# +---+------+-------------------+----------+
# |  0|  duke|               java|        20|
# |  1| snake|             python|        10|
# |  2|gopher|                 go|         5|
# +---+------+-------------------+----------+
