import requests
from geopy import distance
from fastapi import FastAPI
import uvicorn

application = FastAPI()

# The hight of ISS from ground
#h = 400


# Distance from you to ISS

#dist = (h**2 + dist_on_ground**2)**0.5

#print ('The distance between you and Current position of the ISS is about \n {} km'.format(round(dist_on_ground),2))

@application.route('/')
def issdist():
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

@application.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
uvicorn.run(app, port=8080, host='0.0.0.0')
