#!/usr/bin/python

# Weather forecast for Raspberry Pi w/Adafruit Mini Thermal Printer.
# Retrieves data from DarkSky.net's API, prints current conditions and
# forecasts for next two days.  See timetemp.py for a different
# weather example using nice bitmaps.
# Written by Adafruit Industries.  MIT license.
#
# Required software includes Adafruit_Thermal and PySerial libraries.
# Other libraries used are part of stock Python install.
#
# Resources:
# http://www.adafruit.com/products/597 Mini Thermal Receipt Printer
# http://www.adafruit.com/products/600 Printer starter pack

from __future__ import print_function
from Adafruit_Thermal import *
from datetime import date
from datetime import datetime
import calendar
import requests

API_KEY = "key here"

LAT = "39.706789"
LONG = "-104.909325"

# Dumps one forecast line to the printer
def forecast(idx):

    date = datetime.fromtimestamp(int(data["daily"][idx]["dt"]))

    day = calendar.day_name[date.weekday()]
    lo = data["daily"][idx]["temp"]["min"]
    hi = data["daily"][idx]["temp"]["max"]
    cond = data["daily"][idx]["weather"][0]["main"]
    printer.print(day + ": low " + str(lo))
    printer.print(deg)
    printer.print(" high " + str(hi))
    printer.print(deg)
    printer.print(cond)
    # printer.println(
    #     " " + cond.replace("\u2013", "-").encode("utf-8")
    # )  # take care of pesky unicode dash


# printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer = Adafruit_Thermal()
deg = chr(0xF8)  # Degree symbol on thermal printer

url = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LONG}&exclude=minutely,hourly&appid={API_KEY}&units=imperial"
# url = "https://api.darksky.net/forecast/"+API_KEY+"/"+LAT+","+LONG+"?exclude=[alerts,minutely,hourly,flags]&units=us"
response = requests.get(url)
data = response.json()

# Print heading
printer.inverseOn()
printer.print("{:^32}".format("Today's Forecast"))
printer.inverseOff()

# Print current conditions
printer.boldOn()
printer.print("{:^32}".format("Current conditions:"))
printer.boldOff()


temp = data["current"]["temp"]
cond = data["current"]["weather"][0]["main"]
printer.print(temp)
printer.print(deg)
printer.println(" " + cond)
printer.boldOn()

# Print forecast
printer.print("{:^32}".format("Forecast:"))
printer.boldOff()
forecast(0)
forecast(1)

printer.feed(3)
