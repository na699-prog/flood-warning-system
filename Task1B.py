from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""
    
    # Build list of stations
    stations = build_station_list()
    
    # Sort stations by distance to find the ones closest to and furthest from Cambridge
    station_tuples = stations_by_distance(stations, (52.2053, 0.1218))

    # Build list of tuples for printing (10 closest stations)
    closest_stations = station_tuples[:10]
    for i in range(0, 10):
        closest_stations[i] = (closest_stations[i][0].name, closest_stations[i][0].town, closest_stations[i][1])

    # 10 furthest stations
    furthest_stations = station_tuples[-10:]
    for i in range(0, 10):
        furthest_stations[i] = (furthest_stations[i][0].name, furthest_stations[i][0].town, furthest_stations[i][1])

    # Print outputs
    print(f"CLOSEST STATIONS: \n{closest_stations}")
    print(f"FURTHEST STATIONS: \n{furthest_stations}")

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
