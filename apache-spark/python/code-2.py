
#
# Data Wrangling with Spark 
#

# run with: python3.7 code-2.py

# include this in order to location spark installation. otherwise errors can be thrown.
import findspark
findspark.init()

from pyspark.sql import SparkSession

# create a new spark session or get the existing one
# spark = SparkSession.builder.appName("app").config("config option", "config option").getOrCreate()

spark = SparkSession.builder.appName("Data Wrangling").getOrCreate()

path = "sparkify_log_small.json"
dataframe = spark.read.json(path)
# dataframe.printSchema()
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

# take = dataframe.take(3)
# print(take)
# [
#     Row(artist='Showaddywaddy', auth='Logged In', firstName='Kenneth', gender='M', itemInSession=112, lastName='Matthews', length=232.93342, level='paid', location='Charlotte-Concord-Gastonia, NC-SC', method='PUT', page='NextSong', registration=1509380319284, sessionId=5132, song='Christmas Tears Will Fall', status=200, ts=1513720872284, userAgent='"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"', userId='1046'), 
#     Row(artist='Lily Allen', auth='Logged In', firstName='Elizabeth', gender='F', itemInSession=7, lastName='Chase', length=195.23873, level='free', location='Shreveport-Bossier City, LA', method='PUT', page='NextSong', registration=1512718541284, sessionId=5027, song='Cheryl Tweedy', status=200, ts=1513720878284, userAgent='"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"', userId='1000'), 
#     Row(artist='Cobra Starship Featuring Leighton Meester', auth='Logged In', firstName='Vera', gender='F', itemInSession=6, lastName='Blackwell', length=196.20526, level='paid', location='Racine, WI', method='PUT', page='NextSong', registration=1499855749284, sessionId=5516, song='Good Girls Go Bad (Feat.Leighton Meester) (Album Version)', status=200, ts=1513720881284, userAgent='"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2"', userId='2219')
# ]

# dataframe.select("page").dropDuplicates().sort("page").show()
# dataframe.select(["userId", "firstname", "page", "song"]).where(dataframe.userId == "1046").collect()

# get_hour = udf(lambda x: datetime.datetime.fromtimestamp(x / 1000.0). hour)
# dataframe = dataframe.withColumn("hour", get_hour(dataframe.ts))
# dataframe.head()

# songs_in_hour = dataframe.filter(dataframe.page == "NextSong").groupby(dataframe.hour).count().orderBy(dataframe.hour.cast("float"))
# songs_in_hour.show()


# Which page did user id "" (empty string) NOT visit?
    # page userId
# dataframe.select("page").filter(dataframe.userId != "").dropDuplicates().sort("page").show()
# +----------------+                                                              
# |            page|
# +----------------+
# |           About|
# |       Downgrade|
# |           Error|
# |            Help|
# |            Home|
# |          Logout|
# |        NextSong|
# |   Save Settings|
# |        Settings|
# |Submit Downgrade|
# |  Submit Upgrade|
# |         Upgrade|
# +----------------+

# What type of user does the empty string user id most likely refer to?
    # userAgent or level (free, paid)
# dataframe.filter(dataframe.userId == "").groupby(dataframe.level).count().show()
# +-----+-----+
# |level|count|
# +-----+-----+
# | free|  193|
# | paid|  143|
# +-----+-----+

# How many female users do we have in the data set?
    # gender
# print(dataframe.filter(dataframe.gender == "F").count())
# x = dataframe.select(["userId", "gender"]).dropDuplicates().where(dataframe.gender == "F").count()
# print(x)
# 462

# How many songs were played from the most played artist?
    # artist song
# dataframe.select(["artist"]).where(dataframe.artist != "").groupby(dataframe.artist).count().sort("count", ascending=False).show()
# +--------------------+-----+                                                    
# |              artist|count|
# +--------------------+-----+
# |            Coldplay|   83|
# |       Kings Of Leon|   69|
# ...
# +--------------------+-----+
# dataframe.select(["song"]).where(dataframe.artist == "Coldplay").groupby(dataframe.song).count().sort("count", ascending=False).show()
# x = dataframe.select(["song"]).where(dataframe.artist == "Coldplay").count()
# print(x)
# 83

# How many songs do users listen to on average between visiting our home page? Please round your answer to the closest integer.
    # user song page
    # page='Home'
from pyspark.sql.functions import avg, col, round
dataframe.select(["userId", "song"]).groupby(dataframe.userId).count().agg(avg(col("count"))).show()
