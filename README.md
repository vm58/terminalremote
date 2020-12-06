# Simple Roku Terminal Remote
This is a simple Python Curses based application which will allow you to connect to and control a Roku device on your local network via your computer keyboard.

## Requirements
### Python
You must have the following installed:
- [python3](https://www.python.org/)
- Two [pip](https://pip.pypa.io/en/stable/) modules:
  - [requests](https://pypi.org/project/requests/)
  - [xmltodict](https://pypi.org/project/xmltodict/)
 ### Configuration
 Open the file remote.py and edit the line containing 'rokuIp = "" to contain the local IP address of the Roku device you would like to interface with. For example:
 >rokuIp = "192.168.0.32"

