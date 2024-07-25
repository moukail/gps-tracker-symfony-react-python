import requests
import uuid

def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))
    return mac_address.lower()

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        return str(e)

def update_device():

    device = {'mac': '', 'ip': get_public_ip()}
    url = f'http://localhost:8000/api/v1/devices/'
    headers = {
        'Content-type': 'application/json',
        #'Authorization': f'Bearer {accessToken}'
    }

    try:
        response = requests.post(url, data=json.dumps(device), headers=headers)
        print(f'location response: {response}')
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)

def find_device_by_mac(mac):
    url = f'http://localhost:8000/api/v1/device/{mac}'
    headers = {
        'Content-type': 'application/json',
        #'Authorization': f'Bearer {accessToken}'
    }

    try:
        response = requests.get(url, headers=headers)
        device_data = response.json()
        response.raise_for_status()
        return device_data
    except requests.exceptions.HTTPError as err:
        print(err)
        return None