from haversine import haversine, Unit

def get_distance(previous_location, location):
    if previous_location == None or location == None:
        return 0
    return haversine((previous_location['latitude'], previous_location['longitude']), (location['latitude'], location['longitude']), unit=Unit.METERS)