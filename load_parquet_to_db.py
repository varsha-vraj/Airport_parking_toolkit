import pandas as pd
from sqlalchemy import create_engine

# File paths
vehicles_parquet = './output_parquet/vehicles.parquet'
zones_parquet = './output_parquet/parking_zones.parquet'
events_parquet = './output_parquet/parking_events.parquet'

# Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:varsha@localhost:5432/airport_parking')

# Load data
vehicles_df = pd.read_parquet(vehicles_parquet)
zones_df = pd.read_parquet(zones_parquet)
events_df = pd.read_parquet(events_parquet)

# Drop duplicates if they exist in DB
with engine.connect() as conn:
    existing_vehicle_ids = pd.read_sql("SELECT vehicle_id FROM vehicles", conn)['vehicle_id'].tolist()
    vehicles_df = vehicles_df[~vehicles_df['vehicle_id'].isin(existing_vehicle_ids)]

    existing_zone_ids = pd.read_sql("SELECT zone_id FROM parking_zones", conn)['zone_id'].tolist()
    zones_df = zones_df[~zones_df['zone_id'].isin(existing_zone_ids)]

    existing_event_ids = pd.read_sql("SELECT event_id FROM parking_events", conn)['event_id'].tolist()
    events_df = events_df[~events_df['event_id'].isin(existing_event_ids)]

# Insert into database
vehicles_df.to_sql('vehicles', engine, if_exists='append', index=False)
zones_df.to_sql('parking_zones', engine, if_exists='append', index=False)
events_df.to_sql('parking_events', engine, if_exists='append', index=False)

print("✅ Parquet data successfully loaded into PostgreSQL!")
