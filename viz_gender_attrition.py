from spark_session import get_spark, load_data

spark = get_spark()
df = load_data(spark)

print("Attrition by Gender")

df.groupBy("Gender", "Leave_or_Not") \
  .count() \
  .orderBy("Gender") \
  .show()

spark.stop()
