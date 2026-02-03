# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine, Unit 
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    """
    Given a list of stations and a coordinate p,
    build and return a list of (station, distance) tuples
    where distance is the distance of that station from the
    inputted coordinate p. 

    The returned list will be sorted in ascending order by 
    distance from p.
    """
    #Create a new list that will be appended to
    sorted_tuples = []
    for station in stations:
        #Create tuple of station and distance from p (in kilometers, as the imported function uses km)
        sorted_tuples.append((station, haversine(station.coord, p)))
    
    #Use utils.sort_by_key to sort list
    sorted_tuples = sorted_by_key(sorted_tuples, 1)
    return sorted_tuples