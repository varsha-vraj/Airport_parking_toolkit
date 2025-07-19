from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg

# Create Spark session
spark = SparkSession.builder \
    .appName("AirportParkingSparkJob") \
    .getOrCreate()

# Read Parquet files
events_df = spark.read.parquet("output_parquet/parking_events.parquet")
vehicles_df = spark.read.parquet("output_parquet/vehicles.parquet")
zones_df = spark.read.parquet("output_parquet/parking_zones.parquet")

# Example: join and average payment per zone
result = events_df.join(zones_df, "zone_id") \
    .groupBy("zone_name") \
    .agg(
        count("*").alias("total_events"),
        avg("paid_amount").alias("avg_payment")
    )

# Show result
result.show()

# Save output
result.write.mode("overwrite").parquet("output_parquet/zone_analysis.parquet")

spark.stop()
