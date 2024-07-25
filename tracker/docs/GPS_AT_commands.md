### command-line serial console tool
```bash 
sudo apt update
sudo apt install -y minicom
sudo minicom -D /dev/ttyUSB2

```

### install python3 rpi.gpio module
```bash
sudo apt update
sudo apt-get install python3-pip python3-dev python3-rpi.gpio python3-serial
```

#### get modem manufacturer
AT+CGMI
#### get modem's model number.
AT+CGMM
#### get modem's serial number
AT+CGSN
#### reset the modem's settings
AT&F

#### Turn on GPS
AT+CGPS=1,1
####
AT+CGPS?

#### to turn on GPS automatically
AT+CGPSAUTO=1

#### to feed the gps nmea sentence every 30 second in the serial port out.
AT+CGPSINFOCFG=30,31

####
AT+CGPSINFO=0






AT+CGNSSMODE=15,1
AT+CGPSNMEA=200191
AT+CGPSNMEARATE=1


AT+CGPSPMD?
+CGPSPMD: 65407

AT+CGPSNMEA?
+CGPSNMEA: 198143