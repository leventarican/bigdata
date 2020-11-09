import pyspark
import pyspark.sql.functions as F
from pyspark.sql.types import *

sc = pyspark.SparkContext(appName="code-7")

prog_langs = [
    "java",
    "python",
    "dart",
    "Java",
    "java",
    "python"
]

# parallelize data in 3 partitions
distributed_chunks = 3
distributed_pl = sc.parallelize(prog_langs, distributed_chunks)

# bring back data to the driver
data = distributed_pl.collect()
print(data)
# ['java', 'python', 'dart', 'Java', 'java', 'python']

a = distributed_pl.first()
print(a)
# java

a = distributed_pl.take(2)
print(a)
# ['java', 'python']

# show partitions
a = distributed_pl.getNumPartitions()
print(a)
# 3
