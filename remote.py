#! /usr/bin/python3

import curses
from curses import wrapper
import pprint
import requests
import xmltodict

#Set the IP address of your Roku device here
rokuIp = "127.0.0.1"

rokuUrl = "http://" + rokuIp + ":8060"
mediaQuery = rokuUrl + "/query/media-player"
deviceQuery = rokuUrl + "/query/device-info"

#Define Urls to be used by requests
up = rokuUrl + "/keypress/up"
down = rokuUrl + "/keypress/down"
left = rokuUrl + "/keypress/left"
right = rokuUrl + "/keypress/right"
home = rokuUrl + "/keypress/home"
back = rokuUrl + "/keypress/back"
select = rokuUrl + "/keypress/select"
info = rokuUrl + "/keypress/info"
backspace = rokuUrl + "/keypress/backspace"

#Query for basic device info
response = requests.get(deviceQuery)
deviceInfo = xmltodict.parse(response.text)

def main(stdscr):
    stdscr.nodelay(1)
    curses.curs_set(0)

    #Colors
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.bkgd(' ', curses.color_pair(1))

    #Screen text
    stdscr.addstr("Connected\n", curses.color_pair(2))
    stdscr.addstr("Device: " + deviceInfo['device-info']['user-device-name'] +\
    "\nLocation: " + deviceInfo['device-info']['user-device-location'] +\
    "\nNetwork: " + deviceInfo['device-info']['network-name'] + "\n\n")
    stdscr.addstr("""Roku
 ______              _           __  ___                 __     
/_  __/__ ______ _  (_)__  ___ _/ / / _ \___ __ _  ___  / /____ 
 / / / -_) __/  ' \/ / _ \/ _ `/ / / , _/ -_)  ' \/ _ \/ __/ -_)
/_/  \__/_/ /_/_/_/_/_//_/\_,_/_/ /_/|_|\__/_/_/_/\___/\__/\__/

Controls:

  Navigate menus: Arrow keys
  Select: Enter
  Home: Home or =
  Back: Delete or `
  Info: ?
  
  Text entry: Alphanumeric characters and space
  Backspace: Backspace

Exit program: Ctrl+C`""")

    #The actual keyboard application
    while True:
        c = stdscr.getch()
        if c != -1:

            #Navigation based on Urls defined earlier
            if c == curses.KEY_UP:
                requests.post(up)
            if c == curses.KEY_DOWN:
                requests.post(down)
            if c == curses.KEY_LEFT:
                requests.post(left)
            if c == curses.KEY_RIGHT:
                requests.post(right)
            if c == curses.KEY_HOME or c == 61:
                requests.post(home)
            if c == curses.KEY_DC or c == 96:
                requests.post(back)
            if c == curses.KEY_ENTER or c == 10 or c == 13:
                requests.post(select)
            if c == 63:
                requests.post(info)
            
            #Alphanumber input
            #Convert from ASCII back to character then send post
            if 48 <= c <=57 or 65 <= c <= 90 or 97 <= c <= 122:
                key = rokuUrl + "/keypress/Lit_" + chr(c)
                requests.post(key)
            if c == 32:
                space = rokuUrl + "/keypress/Lit_+"
                requests.post(space)
            if c == curses.KEY_BACKSPACE:
                requests.post(backspace)

wrapper(main)
