import findspark
findspark.init()

import pyspark
sc = pyspark.SparkContext(appName="app")

prog_langs = [
    "java",
    "python",
    "dart",
    "Java",
    "java",
    "python"
]

distributed_pl = sc.parallelize(prog_langs)
result = distributed_pl.map(lambda pl: pl.lower()).collect()

print(result)
# ['java', 'python', 'dart', 'java', 'java', 'python']
