
#
# import / export data from / to spark DataFrames
#

# include this in order to location spark installation. otherwise errors can be thrown.
import findspark
findspark.init()

from pyspark.sql import SparkSession

# create a new spark session or get the existing one
# spark = SparkSession.builder.appName("app").config("config option", "config option").getOrCreate()

spark = SparkSession.builder.appName('the app').getOrCreate()
conf = spark.sparkContext.getConf().getAll()

print(conf)
#  [ ... ('spark.app.name', 'the app') ... ]

# load json file into a spark DataFrame
# usually file should be on a distributed filesystem lik HDFS (Hadoop), or AWS
path = "sparkify_log_small.json"
# path = "hdfs://ec2-34-218-86-174.us-west-2.compute.amazonaws.com:9000/sparkify/sparkify_log_small.json"
user_log = spark.read.json(path)
user_log.printSchema()
# root                                                                            
#  |-- artist: string (nullable = true)
#  |-- auth: string (nullable = true)
#  |-- firstName: string (nullable = true)
#  |-- gender: string (nullable = true)
#  |-- itemInSession: long (nullable = true)
#  |-- lastName: string (nullable = true)
#  |-- length: double (nullable = true)
#  |-- level: string (nullable = true)
#  |-- location: string (nullable = true)
#  |-- method: string (nullable = true)
#  |-- page: string (nullable = true)
#  |-- registration: long (nullable = true)
#  |-- sessionId: long (nullable = true)
#  |-- song: string (nullable = true)
#  |-- status: long (nullable = true)
#  |-- ts: long (nullable = true)
#  |-- userAgent: string (nullable = true)
#  |-- userId: string (nullable = true)

print(user_log.describe())
# DataFrame[summary: string, artist: string, auth: string, firstName: string, gender: string, itemInSession: string, lastName: string, length: string, level: string, location: string, method: string, page: string, registration: string, sessionId: string, song: string, status: string, ts: string, userAgent: string, userId: string]

# show the first record
user_log.show(n=1)
# +-------------+---------+---------+------+-------------+--------+---------+-----+--------------------+------+--------+-------------+---------+--------------------+------+-------------+--------------------+------+
# |       artist|     auth|firstName|gender|itemInSession|lastName|   length|level|            location|method|    page| registration|sessionId|                song|status|           ts|           userAgent|userId|
# +-------------+---------+---------+------+-------------+--------+---------+-----+--------------------+------+--------+-------------+---------+--------------------+------+-------------+--------------------+------+
# |Showaddywaddy|Logged In|  Kenneth|     M|          112|Matthews|232.93342| paid|Charlotte-Concord...|   PUT|NextSong|1509380319284|     5132|Christmas Tears W...|   200|1513720872284|"Mozilla/5.0 (Win...|  1046|
# +-------------+---------+---------+------+-------------+--------+---------+-----+--------------------+------+--------+-------------+---------+--------------------+------+-------------+--------------------+------+

# or take the first 5 records
# user_log.take(5)

# we have the data now in a DataFrame
# lets write it as a csv file
out_path = "foobar.csv"
user_log.write.save(out_path, format="csv", header=True)

# now read it in another DataFrame
user_log_1 = spark.read.csv(out_path, header=True)
user_log_1.printSchema()
# root
#  |-- artist: string (nullable = true)
#  |-- auth: string (nullable = true)
#  |-- firstName: string (nullable = true)
#  |-- gender: string (nullable = true)
#  |-- itemInSession: string (nullable = true)
#  |-- lastName: string (nullable = true)
#  |-- length: string (nullable = true)
#  |-- level: string (nullable = true)
#  |-- location: string (nullable = true)
#  |-- method: string (nullable = true)
#  |-- page: string (nullable = true)
#  |-- registration: string (nullable = true)
#  |-- sessionId: string (nullable = true)
#  |-- song: string (nullable = true)
#  |-- status: string (nullable = true)
#  |-- ts: string (nullable = true)
#  |-- userAgent: string (nullable = true)
#  |-- userId: string (nullable = true)

user_log_1.select("userID").show()
# |userID|
# +------+
# |  1046|
# |  1000|
# |  2219|
# |  2373|
# |  1747|
# |  1747|
# |  1162|
# |  1061|
# |   748|
# |   597|
# |  1806|
# |   748|
# |  1176|
# |  2164|
# |  2146|
# |  2219|
# |  1176|
# |  2904|
# |   597|
# |   226|
# +------+
# only showing top 20 rows
