# spark_session.py
import os
import findspark

os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-11.0.30.7-hotspot"
os.environ["SPARK_HOME"] = r"C:\spark\spark-3.5.0-bin-hadoop3"

findspark.init(os.environ["SPARK_HOME"])

from pyspark.sql import SparkSession

def get_spark():
    spark = SparkSession.builder \
        .appName("AttritionVisualization") \
        .master("local[*]") \
        .config(
            "spark.jars",
            r"C:\spark\spark-3.5.0-bin-hadoop3\jars\mysql-connector-j-9.6.0.jar"
        ) \
        .getOrCreate()
    return spark


def load_data(spark):
    df = spark.read.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/hr") \
        .option("dbtable", "employee_attrition") \
        .option("user", "sparkuser") \
        .option("password", "Ravuru@123") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .load()
    return df
