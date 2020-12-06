# Simple Roku Terminal Remote
This is a simple Python Curses based application which will allow you to connect to and control a Roku device on your local network via your computer keyboard. It works using the Roku External Control Protocol (ECP), which is a simple RESTful API.

Before running this application on your system you will need to edit remote.py to point to the local network IP address of the Roku device you would like to control. This application currently has no error handling whatsoever, so if the IP is invalid or can not be reached the application will crash.

## Requirements
### Python
You must have the following installed on your local system:
- [python3](https://www.python.org/)
- Two Python modules are used in the remote.py Python script (you can install modules with [pip](https://pypi.org/project/xmltodict/)):
  - [requests](https://pypi.org/project/requests/)
  - [xmltodict](https://pypi.org/project/xmltodict/)
 ### Configuration
 Open the file remote.py and edit the line containing 'rokuIp = "" to contain the local IP address of the Roku device you would like to interface with. For example:
 >rokuIp = "192.168.0.32"

