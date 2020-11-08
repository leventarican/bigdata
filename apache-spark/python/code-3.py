
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

spark = SparkSession.builder.appName("Data Wrangling with Spark SQL").getOrCreate()

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

dataframe.createOrReplaceTempView("view")
# spark.sql('''''').show()
# spark.sql(
#     '''
#     select * from view limit 2
#     ''').show()
# +-------------+---------+---------+------+-------------+--------+---------+-----+--------------------+------+--------+-------------+---------+--------------------+------+-------------+--------------------+------+
# |       artist|     auth|firstName|gender|itemInSession|lastName|   length|level|            location|method|    page| registration|sessionId|                song|status|           ts|           userAgent|userId|
# +-------------+---------+---------+------+-------------+--------+---------+-----+--------------------+------+--------+-------------+---------+--------------------+------+-------------+--------------------+------+
# |Showaddywaddy|Logged In|  Kenneth|     M|          112|Matthews|232.93342| paid|Charlotte-Concord...|   PUT|NextSong|1509380319284|     5132|Christmas Tears W...|   200|1513720872284|"Mozilla/5.0 (Win...|  1046|
# |   Lily Allen|Logged In|Elizabeth|     F|            7|   Chase|195.23873| free|Shreveport-Bossie...|   PUT|NextSong|1512718541284|     5027|       Cheryl Tweedy|   200|1513720878284|"Mozilla/5.0 (Win...|  1000|
# +-------------+---------+---------+------+-------------+--------+---------+-----+--------------------+------+--------+-------------+---------+--------------------+------+-------------+--------------------+------+

# spark.sql('''
#     select  userID, firstname, page, song
#     from  view 
#     where userID == '1046'
#     '''
#     ).collect()

# udf (user defined functions) need to be registered
spark.udf.register("get_hour", lambda x: int(datetime.datetime.fromtimestamp(x / 1000.0).hour))
spark.sql('''
    select *, get_hour(ts) AS hour
    from view 
    limit 1
    '''
    ).collect()
