#city_to_coords.py

from geopy.geocoders import Nominatim

def get_coordinates(city_name):
    try:
        geolocator = Nominatim(user_agent="solar_app")
        location = geolocator.geocode(city_name, timeout=10)
        if location:
            return location.latitude, location.longitude
        return None
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        return None




