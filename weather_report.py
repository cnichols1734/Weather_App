import requests

# Ask for city name
city_name = input("Enter a city name: ")

# Make the Nominatim API request to get the longitude and latitude
nominatim_url = "https://nominatim.openstreetmap.org/search"
nominatim_params = {"q": city_name, "format": "json"}
nominatim_response = requests.get(nominatim_url, params=nominatim_params)

# Parse the Nominatim JSON response
nominatim_data = nominatim_response.json()

# Get the longitude and latitude
result = nominatim_data[0]
lon = result["lon"]
lat = result["lat"]

# Make the 7Timer API request with the longitude and latitude
timer_url = "http://www.7timer.info/bin/api.pl"
timer_params = {"lon": lon, "lat": lat, "product": "astro", "output": "json"}
timer_response = requests.get(timer_url, params=timer_params)

# Parse the 7Timer JSON response
timer_data = timer_response.json()

# Print the weather forecast
for timepoint in timer_data["dataseries"]:
    print(f"Timepoint: {timepoint['timepoint']}")
    print(f"Cloud cover: {timepoint['cloudcover']}")
    print(f"Seeing: {timepoint['seeing']}")
    print(f"Transparency: {timepoint['transparency']}")
    print(f"Lifted index: {timepoint['lifted_index']}")
    print(f"Relative humidity: {timepoint['rh2m']}")
    print(f"Wind: {timepoint['wind10m']['direction']} {timepoint['wind10m']['speed']}")
    print(f"Temperature: {timepoint['temp2m']}")
    print(f"Precipitation type: {timepoint['prec_type']}")
    print()


