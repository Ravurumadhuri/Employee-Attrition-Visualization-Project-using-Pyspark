from spark_session import get_spark, load_data

spark = get_spark()
df = load_data(spark)

print("Age distribution of employees")

df.select("Age").describe().show()

spark.stop()
