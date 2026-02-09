from spark_session import get_spark, load_data

spark = get_spark()
df = load_data(spark)

print("Attrition by City")

df.groupBy("City", "Leave_or_Not") \
  .count() \
  .orderBy("City") \
  .show()

spark.stop()
