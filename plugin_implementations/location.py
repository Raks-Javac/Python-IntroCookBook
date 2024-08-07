import geocoder

def get_current_location():
    g = geocoder.ip("")
    if g.ok:
        return g.latlng
    else:
        print("Could not get location.")
        return None

location = get_current_location()
if location:
    print(f"Latitude: {location[0]}, Longitude: {location[1]}")
else:
    print("Location could not be determined.")
