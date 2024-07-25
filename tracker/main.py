import os
import time
import asyncio

from dotenv import load_dotenv

from lib.gps import gps
from lib.distance import get_distance
from api.location import send_location
from api.device import get_public_ip, get_mac_address, find_device_by_mac

# Load environment variables from .env file
load_dotenv()

serial_port = os.getenv('SERIAL_PORT')
baud_rate = int(os.getenv('BAUD_RATE'))
min_distance = int(os.getenv('MIN_DISTANCE'))

gps = gps(serial_port, baud_rate)

device = None
previous_location = None

async def get_device():
    mac = get_mac_address()
    device = find_device_by_mac(mac)
    #if device == None:
    #    register_device()

def is_moving(location):
    global previous_location
    distance = get_distance(previous_location, location)
    #print(f"The distance between the locations is {distance:.2f} meters.")
    return distance >= min_distance

async def get_location():
    global previous_location

    if not gps.is_gps_active():
        gps.start()

    location = gps.get_location()

    if device and location and is_moving(location):
        send_location(device['id'], location)

    #if location and is_moving(location):
    #    save_location_db(device['id'], location)

    previous_location = location

async def my_task():
    print("Task executed")

async def repeat_location_task(interval):
    while True:
        await get_location()
        await asyncio.sleep(interval)

async def main():
    location_interval = int(os.getenv('LOCATION_TIMEOUT'))
    await get_device()
    await repeat_location_task(location_interval)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Received exit, exiting")
    gps.close()
