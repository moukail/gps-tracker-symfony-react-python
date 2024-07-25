import asyncio
from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic

MX_KEYS = "FD:83:7E:BF:E0:A4"
MX_MASTER_3 = "D9:71:88:49:D4:F3"
LE_WH_1000XM4 = "CC:38:67:7F:D6:97"
moukail_smart_monitor = "A0:D7:F3:A5:6E:0F"
moukail_pc = "38:87:D5:7A:58:9F"
address = moukail_pc
MODEL_NBR_UUID = "2A24"
MANUFACTURE_NBR_UUID = "2a29"

def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    """Simple notification handler which prints the data received."""
    #logger.info("%s: %r", characteristic.description, data)
    print("notify_battery: {0}".format("".join(map(chr, data))))

async def main(address):
    async with BleakClient(address, timeout=60) as client:
        paired = await client.pair(protection_level=2)
        print(f"Paired: {paired}")


        x = client.is_connected
        print("Connected: {0}".format(x))

        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)

        battery_level = await client.read_gatt_char("00002a19-0000-1000-8000-00805f9b34fb")
        print(int.from_bytes(battery_level,byteorder='big'))

        for service in client.services:
            print("[Service] {0}: {1}".format(service.uuid, service.description))

            for char in service.characteristics:
                print("[characteristic] {0}: {1}".format(char.uuid, char.properties))
                try:
                    car_value = await client.read_gatt_char(char.uuid)
                    print("[characteristic] value: {0}".format("".join(map(chr, car_value))))
                except Exception as e:
                    print(f"Error: {e}")

                for descriptor in char.descriptors:
                    print("[descriptor] {0}: {1}".format(descriptor.uuid, descriptor.handle))
                    descriptor_value = await client.read_gatt_descriptor(descriptor.handle)
                    print("[descriptor] value: {0}".format("".join(map(chr, descriptor_value))))


        #await client.start_notify("00002a19-0000-1000-8000-00805f9b34fb", notification_handler)
        #await asyncio.sleep(5.0)
        #await client.stop_notify("00002a19-0000-1000-8000-00805f9b34fb")

        #manufacture = await client.read_gatt_char(MANUFACTURE_NBR_UUID)
        #print("Manufacture: {0}".format("".join(map(chr, manufacture))))

        #model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        #print("Model Number: {0}".format("".join(map(chr, model_number))))

asyncio.run(main(address))