# Python code

import weather

myLocation = "Chennai,IN"
APIKEY = "bf4a8d480ee05c00952bf65b78ae826b"

locationData = weather.get(myLocation,APIKEY)
