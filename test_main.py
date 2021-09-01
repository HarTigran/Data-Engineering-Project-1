import requests

def ping():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    iss_long = r.json()['iss_position']['longitude']
    iss_lat = r.json()['iss_position']['latitude']
    
    b = requests.get('https://geolocation-db.com/json/')
    your_long = b.json()['longitude']
    your_lat = b.json()['latitude']
    try:
        float(iss_long) 
        float(iss_lat)
        float(your_long)
        float(your_lat)
    except ValueError:
        return "Link is unavailable"

def test_link_check():
    assert ping() != 'Link is unavailable'
