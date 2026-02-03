"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

def test_stations_by_distance():

    # Create station 1
    s1 = MonitoringStation("s1_id", "s1_mid", "s1_label", (0, 20), (-1, 1), "s1_river", "s1_town")

    # Create station 2
    s2 = MonitoringStation("s2_id", "s2_mid", "s2_label", (-10, 0), (-1, 1), "s2_river", "s2_town")

    sorted_list = stations_by_distance([s1, s2], (0, -5))

    # station 2 should the the closest one to (0, -5)

    assert sorted_list[0][0].name == "s2_label"
    assert sorted_list[1][0].name == "s1_label"
    assert round(sorted_list[0][1], 0) == 1242
    assert round(sorted_list[1][1], 0) == 2780
