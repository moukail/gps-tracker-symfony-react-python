import sys
import serial
import time

class gps:

    gps_active = False

    def __init__(self, port, baud_rate):
        print("GPS")
        self.modem = serial.Serial(port, baud_rate)
        self.start()

    def start(self):
        if self.ok():
            print("Successful init of GPS")
            if not self.check_status(2):
                print("Could not start GPS")
                sys.exit(2)

    def is_gps_active(self):
        return self.gps_active

    def ok(self):
        result = self.__send_command("AT")
        return len(result) == 1 and result[0] == 'OK'

    def check_status(self, retries=0):
        print("Check GPS status")
        gps_status = self.send_command('CGPS?')
        if gps_status[0] == '+CGPS: 1,1':
            self.gps_active = True
            print("GPS active")

        else:
            print("Activating GPS")
            gps_activate_result = self.send_command('CGPS=1')
            print(gps_activate_result)
            time.sleep(5)
            if retries > 0:
                return self.check_status(retries - 1)
            else:
                return False

        return True

    def __send_command(self, command):
        self.modem.write((command + '\r').encode('utf-8'))
        time.sleep(2)
        return self.read_response()

    def read_response(self):
        ret = []
        while self.modem.inWaiting() > 0:
            msg = self.modem.readline().strip().decode("UTF-8")
            msg = msg.replace("\r", "").replace("\n", "")
            print(msg)
            if msg != "":
                ret.append(msg)
        return ret

    def send_command(self, command):
        result = self.__send_command("AT+"+command)
        return result

    def close(self):
        self.modem.close()

    def get_location(self):
        if not self.gps_active:
            return None

        response = self.send_command('CGPSINFO')
        if len(response) == 2 and ',,,,,,' in response[0] and response[1] == "OK":
            print('GPS is not ready')
            return None

        return self.parse_location(response[0])

    def parse_location(self, data):
        location = data.removeprefix('+CGPSINFO: ')
        print((-1 if location[12] == 'S' else 1))
        return {
            'latitude': float(location[:11])/100 * (1 if location[12] == 'N' else -1),
            'longitude': float(location[14:26])/100 * (1 if location[27] == 'E' else -1),
            #'date': location[29:35],
            #'time': location[36:44],
            'altitude': float(location[45:48]),
            #'speed': location[49:52],
            #'heading_angle': location[53:56]
        }