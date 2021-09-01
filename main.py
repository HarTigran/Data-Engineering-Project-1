import requests
from geopy import distance
from fastapi import FastAPI
import uvicorn

application = FastAPI()

@application.get('/')
async def root():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    iss_long = r.json()['iss_position']['longitude']
    iss_lat = r.json()['iss_position']['latitude']

    b = requests.get('https://geolocation-db.com/json/')
    your_long = b.json()['longitude']
    your_lat = b.json()['latitude']

    coords_1 = (float(iss_lat), float(iss_long))
    coords_2 = (float(your_lat), float(your_long))

    # Distance from your location to the location of ISS in ground
    dist_on_ground = round(distance.distance(coords_1, coords_2).km,2)
    """Return a your distance from ISS."""
    print("The distance between you and Current position of the ISS is about:")
    return {'you':b.json()['city'],"dist_to_you":str(dist_on_ground), 'unit':'km'}

@application.get("/add/{longitude}/{latitude}")
async def add(longitude: str, latitude: str):
    r = requests.get('http://api.open-notify.org/iss-now.json')
    iss_long = r.json()['iss_position']['longitude']
    iss_lat = r.json()['iss_position']['latitude']

    your_long = longitude
    your_lat = latitude

    coords_1 = (float(iss_lat), float(iss_long))
    coords_2 = (float(your_lat), float(your_long))

    # Distance from your location to the location of ISS in ground
    dist_on_ground = round(distance.distance(coords_1, coords_2).km,2)
    """Returns distance from ISS."""
    print("The distance between provided point and Current position of the ISS is about:")
    return {"ISS_dist_to_point_is":str(dist_on_ground), 'unit':'km'}

# run the app.
if __name__ == "__main__":
    uvicorn.run(application, port=8080, host='0.0.0.0')
