import asyncio
from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic

# Define service and characteristic UUIDs (replace with your desired values)
SERVICE_UUID = "A07498CA-AD5B-474E-940D-16F1FBE7E8CC"
CHARACTERISTIC_UUID = "12345678-1234-5678-1234-56789abcdef1"

moukail_pc = "38:87:D5:7A:58:9F"
address = moukail_pc

async def main(address):
    async with BleakClient(address, timeout=60) as client:
        res = await client.pair(protection_level=None)
        print(res)

        x = client.is_connected
        print("Connected: {0}".format(x))

        # Read characteristic
        data = await client.read_gatt_char(CHARACTERISTIC_UUID)
        print(f"Read data: {data}")

        # Write characteristic (adjust data as needed)
        await client.write_characteristic(CHARACTERISTIC_UUID, b"Data from client")

        # Subscribe to characteristic notifications
        def handle_notification(sender, data):
            print(f"Notification received: {data}")
        await client.start_notify(CHARACTERISTIC_UUID, handle_notification)

        # Wait for notifications or perform other actions
        await asyncio.sleep(10)  # Adjust as needed
        await client.stop_notify(CHARACTERISTIC_UUID)

asyncio.run(main(address))