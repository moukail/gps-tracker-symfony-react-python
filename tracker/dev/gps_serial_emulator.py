import serial
import time

class SerialServer:
    def __init__(self, port):
        self.ser = serial.Serial(port, 115200, timeout=1)

    def read_command(self):
        command = self.ser.readline().decode('utf-8').rstrip()
        return command

    def send_response(self, response):
        self.ser.write((response + '\n').encode('utf-8'))

    def close(self):
        self.ser.close()

    def get_location(self):
        return "+CGPSINFO: 5155.713093,N,00429.234559,E,260624,191036.0,8.8,0.0,"


server = SerialServer('/dev/pts/3')

responses = {
    "AT": ["OK"],
    "AT+CGPS=1": ["OK"],
    "AT+CGPS?": ["+CGPS: 1,1", " ", "OK"],
    "AT+CGPSINFO": [server.get_location(), " ", "OK"],
}

while True:
    command = server.read_command()
    if command:
        print(f"Received command: {command}")
        for response in responses.get(command, "Unknown command."):
            server.send_response(response)
            print(f"Sent response: {response}")
    time.sleep(1)

server.close()