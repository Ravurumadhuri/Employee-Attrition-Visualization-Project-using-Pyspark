from spark_session import get_spark, load_data

spark = get_spark()
df = load_data(spark)

print("Attrition vs Experience")

df.groupBy("Experience_Current_Domain", "Leave_or_Not") \
  .count() \
  .orderBy("Experience_Current_Domain") \
  .show()

spark.stop()
