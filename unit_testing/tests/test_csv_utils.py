import pytest
from patterns.csv_utils import parse_file, Ride
from datetime import datetime

def test_parse_file():
    test_csv_file = "test_rides.csv"
    
    parsed_rides = parse_file(test_csv_file)
    
    assert len(parsed_rides) == 3
    assert parsed_rides[0].taxi_id == "17083"
    assert parsed_rides[0].pick_up_time == datetime(2018,1,1,0,18,50)
    assert parsed_rides[0].drop_of_time == datetime(2018, 1, 1, 0, 24, 39)
    assert parsed_rides[0].passenger_count == 5
    assert parsed_rides[0].trip_distance == 0.7
    assert parsed_rides[0].tolls_amount == 7.3
