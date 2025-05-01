### Virtual env
```bash
sudo apt install python3-venv
python3 -m venv .venv
source ./.venv/bin/activate
which python3

deactivate
```

### pybluez
```bash
sudo apt-get install python3-dev
pip install git+https://github.com/pybluez/pybluez.git
```

### install packages
```bash
python -m pip install requests
pip install -r requirements.txt
```

### PEP 8 – Style Guide for Python Code
https://peps.python.org/pep-0008/
https://black.readthedocs.io/en/stable/index.html#

1) /dev/ttyUSB0-diag port for output developing messages
2) /dev/ttyUSB1- NMEA port for GPS NMEA data output
3) /dev/ttyUSB2-AT port for AT commands
4) /dev/ttyUSB3-Modem port for ppp-dial
5) /dev/ttyUSB4-Audio port