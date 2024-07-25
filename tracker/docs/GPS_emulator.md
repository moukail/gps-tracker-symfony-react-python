#### Install 
```bash
sudo apt-get install -y socat
```
#### Step 1
```bash
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```
/dev/pts/3 for the client and /dev/pts/4 for the server
#### Step 2
```bash
python3 gps_serial_emulator.py
```
