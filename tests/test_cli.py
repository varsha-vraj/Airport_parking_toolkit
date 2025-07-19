import pandas as pd
from airport_parking_toolkit.cli_tool import validate_data

def test_validate_data_removes_invalid_rows():
    # Mock data
    events = pd.DataFrame([{
        "event_id": "E0001",
        "vehicle_id": "V0001",
        "zone_id": "Z001",
        "entry_time": pd.Timestamp("2024-01-01 08:00:00"),
        "exit_time": pd.Timestamp("2024-01-01 07:00:00"),  # invalid
        "paid_amount": -10.0  # invalid
    }])
    
    vehicles = pd.DataFrame([{"vehicle_id": "V0001", "plate_number": "KA01AB1234", "type": "SUV", "owner_name": "Alice"}])
    zones = pd.DataFrame([{"zone_id": "Z001", "zone_name": "Short Term", "rate_per_hour": 50, "is_valet": False}])
    
    cleaned = validate_data(events, zones, vehicles)
    
    assert cleaned.empty, "Invalid row was not removed"
