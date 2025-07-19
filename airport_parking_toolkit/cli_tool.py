# airport_parking_toolkit/cli_tool.py

import pandas as pd
import argparse
import os
import logging

# Setup logging
logging.basicConfig(filename="parking_etl.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def read_csvs(events_path, zones_path, vehicles_path):
    try:
        events_df = pd.read_csv(events_path, parse_dates=["entry_time", "exit_time"])
        zones_df = pd.read_csv(zones_path)
        vehicles_df = pd.read_csv(vehicles_path)
        logging.info("All CSVs read successfully.")
        return events_df, zones_df, vehicles_df
    except Exception as e:
        logging.error(f"Error reading CSVs: {e}")
        raise

def validate_data(events_df, zones_df, vehicles_df):
    import logging

    errors = []

    # 1. exit_time > entry_time
    invalid_time = events_df[events_df["exit_time"] <= events_df["entry_time"]]
    if not invalid_time.empty:
        errors.append(f"{len(invalid_time)} rows with exit_time <= entry_time")
        logging.warning(errors[-1])

    # 2. paid_amount >= 0
    negative_payments = events_df[events_df["paid_amount"] < 0]
    if not negative_payments.empty:
        errors.append(f"{len(negative_payments)} rows with negative paid_amount")
        logging.warning(errors[-1])

    # 3. null values
    null_rows = events_df[events_df.isnull().any(axis=1)]
    if not null_rows.empty:
        errors.append(f"{len(null_rows)} rows with nulls")
        logging.warning(errors[-1])

    # 4. invalid vehicle_id
    invalid_vehicles = events_df[~events_df["vehicle_id"].isin(vehicles_df["vehicle_id"])]
    if not invalid_vehicles.empty:
        errors.append(f"{len(invalid_vehicles)} rows with invalid vehicle_id")
        logging.warning(errors[-1])

    # 5. invalid zone_id
    invalid_zones = events_df[~events_df["zone_id"].isin(zones_df["zone_id"])]
    if not invalid_zones.empty:
        errors.append(f"{len(invalid_zones)} rows with invalid zone_id")
        logging.warning(errors[-1])

    # Keep only valid rows
    valid_df = events_df[
        (events_df["exit_time"] > events_df["entry_time"]) &
        (events_df["paid_amount"] >= 0) &
        (events_df.notnull().all(axis=1)) &
        (events_df["vehicle_id"].isin(vehicles_df["vehicle_id"])) &
        (events_df["zone_id"].isin(zones_df["zone_id"]))
    ]

    logging.info(f"{len(events_df) - len(valid_df)} rows removed during validation")
    return valid_df


def main():
    
    print("CLI started")

    parser = argparse.ArgumentParser(description="Airport Parking ETL")
    parser.add_argument("--events", required=True, help="Path to parking_events.csv")
    parser.add_argument("--zones", required=True, help="Path to parking_zones.csv")
    parser.add_argument("--vehicles", required=True, help="Path to vehicles.csv")
    parser.add_argument("--output", required=True, help="Output directory for cleaned parquet files")

    args = parser.parse_args()

    print("Reading files")

    # Read CSVs
    events_df, zones_df, vehicles_df = read_csvs(args.events, args.zones, args.vehicles)

    # Save to parquet
    os.makedirs(args.output, exist_ok=True)
    events_df.to_parquet(os.path.join(args.output, "parking_events.parquet"), index=False)
    zones_df.to_parquet(os.path.join(args.output, "parking_zones.parquet"), index=False)
    vehicles_df.to_parquet(os.path.join(args.output, "vehicles.parquet"), index=False)

    logging.info("Parquet files written successfully.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")

