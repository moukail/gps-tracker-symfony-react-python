from bless import (
    BlessServer,
    BlessGATTService,
    BlessGATTCharacteristic
)

class MyService(BlessGATTService):
    UUID = "12345678-1234-5678-1234-56789abcdef0"

    def __init__(self):
        super().__init__()
        self.add_characteristic(MyCharacteristic())

class MyCharacteristic(BlessGATTCharacteristic):
    UUID = "12345678-1234-5678-1234-56789abcdef1"

    def __init__(self):
        super().__init__()
        self.value = bytearray("Hello, world!", "utf-8")

    def read_value(self):
        print("Read Request")
        return self.value

    def write_value(self, value):
        print("Write Request: ", value)
        self.value = value

my_service_name = "Test BLE C"
server = BlessServer(name=my_service_name)
server.add_new_service(MyService())

try:
    server.start()
    print("BLE GATT server started...")
    while True:
        pass  # Keep the server running
except KeyboardInterrupt:
    print("Stopping server...")
    server.stop()