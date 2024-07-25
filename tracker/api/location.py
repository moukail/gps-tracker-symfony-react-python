import requests
import json

def send_location(deviceId, location):
    url = f'http://localhost:8000/api/v1/locations/{deviceId}'
    headers = {
        'Content-type': 'application/json',
        #'Authorization': f'Bearer {accessToken}'
    }

    try:
        response = requests.post(url, data=json.dumps(location), headers=headers)
        print(f'location response: {response}')
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
