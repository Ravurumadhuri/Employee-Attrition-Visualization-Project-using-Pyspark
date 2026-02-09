import matplotlib.pyplot as plt
from spark_session import get_spark, load_data

# ---- Start Spark ----
spark = get_spark()
print("✅ Spark Started")

# ---- Read data from MySQL ----
df = load_data(spark)
print("✅ Data Loaded")

# ---- Group data for visualization ----
city_df = df.groupBy("City", "Leave_or_Not").count().toPandas()

# ---- Create pivot for bar chart ----
pivot = city_df.pivot_table(index="City", columns="Leave_or_Not", values="count", aggfunc="first")

# ---- Plot chart ----
pivot.plot(kind="bar")
plt.title("Attrition by City")
plt.xlabel("City")
plt.ylabel("Employee Count")
plt.tight_layout()
plt.show()

# ---- Stop Spark ----
spark.stop()
