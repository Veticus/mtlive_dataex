# coding=utf-8
# !/usr/bin/python

import urllib.request as rq
from xml.etree import ElementTree as Et

__project__ = "mtlive-dataex"
__filename__ = "get_busdata.py"
__author__ = "Tim Engel"
__date__ = "25/02/2017"
__using__ = "PyCharm"
__interpreter_version__ = "3.5.1"
__version__ = "0.0.1"

#  These are just some "safe values", aimed to gather as many busses as possible.
#  TODO: Randomize these everytime data is requested
#  TODO: Save most recent response to a file, and use the file as a "cache" - preventing excessive requests.
lon = 10.031171035766636
lat = 57.71612970581591
rad = 463316.96416736324
getbussesurl = "https://live.midttrafik.dk/getbuses.php?lat={}&lon={}&radius={}".format(str(lat), str(lon), str(rad))
usedummydata = True  # Set to false, this lets the program request the data from the online service.
if usedummydata: print("Using dummydata")
if not usedummydata: print("USING LIVE DATA")


def allbusdata(live=False):
	if not usedummydata: live = True
	if not live:
		# To prevent "flooding" the live.midttrafik.dk service during development
		# this allows the use of dummy data stored in the "dummy_response" file.
		busdata = open("dummy_response").read()
		return busdata
	print("Requesting data...")
	data_getter = rq.urlopen(getbussesurl)  # Creates an instance of urllib.request and opening the getbusses url.
	busdata = data_getter.read()  # Throws the entire response into a single string, for later processing.
	return busdata


def getbusdom():
	# This should return an ElementTree containing all the busdata
	dom = Et.fromstring(allbusdata(live=False))
	return dom


def print_businfo_for_line(line):
	# This should print some info about a given line.
	num = 0
	xpath = 'Bus[@Line="{}"]'.format(line)  # Here the xpath is assembled.
	# The xpath is used too identify "rows", where the Line attribute matches whatever the line variable is set to.
	# Hereafter the .findall() function allows the use of .attrib in the for-loop.
	for i in getbusdom().findall(xpath):
		num += 1
		print(str(num))
		print("Name:        " + i.attrib['Name'])
		print("Line:        " + i.attrib['Line'])
		print("Text:        " + i.attrib['DirectionText'])
		print("End name:    " + i.attrib['EndName'])
		print("Start name:  " + i.attrib['StartName'])
		# TODO: Add a "current time" thingy and a "time since last update" thingy
		print("Updated:     " + i.attrib['Updated'])
		print("Delay:       " + i.attrib['Delay'])
		print("Start time:  " + i.attrib['StartTime'])
		print("End time:    " + i.attrib['EndTime'])
		print("-------------------------------------")
	print("There are currently {} busses of line {} on the road.".format(num, line))


def print_businfo_by_delay_range(delaymin=0, delaymax=9001):
	num = 0
	domtouse = getbusdom()
	for i in range(delaymin, delaymax):
		xpath = 'Bus[@Delay="{}"]'.format(i)
		for i in domtouse.findall(xpath):
			num += 1
			print(str(num))
			print("Name:        " + i.attrib['Name'])
			print("Line:        " + i.attrib['Line'])
			print("Text:        " + i.attrib['DirectionText'])
			print("End name:    " + i.attrib['EndName'])
			print("Start name:  " + i.attrib['StartName'])
			# TODO: Add a "current time" thingy and a "time since last update" thingy
			print("Updated:     " + i.attrib['Updated'])
			print("Delay:       " + i.attrib['Delay'])
			print("Start time:  " + i.attrib['StartTime'])
			print("End time:    " + i.attrib['EndTime'])
			print("-------------------------------------")
	print("There are currently {} busses with a delay between {} and {}  on the road.".format(num, delaymin, delaymax))


def count_businfo_by_delay_range(delaymin=0, delaymax=9001):
	num = 0
	domtouse = getbusdom()
	for i in range(delaymin, delaymax):
		xpath = 'Bus[@Delay="{}"]'.format(i)
		for i in domtouse.findall(xpath): num += 1
	print("There are currently {} busses with a delay between {} and {}  on the road.".format(num, delaymin, delaymax))


def count_busses_on_line(line=100):
	# This should count the number of busses on a certain line, currently on the road.
	num = 0
	xpath = 'Bus[@Line="{}"]'.format(line)  # Here the xpath is assembled.
	for i in getbusdom().findall(xpath): num += 1
	print("There are currently {} busses of line {} on the road.".format(num, line))


print_businfo_for_line(100)  # For shits, giggles and testing this will use line 100 for testing.
print_businfo_by_delay_range()
count_businfo_by_delay_range()
count_busses_on_line()
