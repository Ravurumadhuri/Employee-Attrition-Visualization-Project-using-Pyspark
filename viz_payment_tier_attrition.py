from spark_session import get_spark, load_data

spark = get_spark()
df = load_data(spark)

print("Attrition vs Payment Tier")

df.groupBy("Payment_Tier", "Leave_or_Not") \
  .count() \
  .orderBy("Payment_Tier") \
  .show()

spark.stop()
