# coding=utf-8
# !/usr/bin/python

import urllib.request as rq
from xml.etree import ElementTree as Et
from random import uniform
__project__ = "mtlive-dataex"
__filename__ = "get_busdata.py"
__author__ = "Tim Engel"
__date__ = "25/02/2017"
__using__ = "PyCharm"
__interpreter_version__ = "3.5.1"
__version__ = "0.0.4"

lon = 10.031171035766636
lat = 57.71612970581591
rad = 463316.96416736324
#  These are just some "safe values", aimed to gather as many busses as possible.
#  The actually used data will be randomize by randomize_coord() and randomize_radius()

usedummydata = False  # Set to false, this lets the program request the data from the online service.
if usedummydata: print("Using dummydata")
if not usedummydata: print("USING LIVE DATA")


def randomize_coordinates(orig_coord):
	new_coord = orig_coord + uniform(-2, 2)
	return new_coord


def randomize_radius(orig_radius):
	new_radius = orig_radius + uniform(-200, 200)
	return new_radius


def allbusdata(live=False):
	# TODO: Add some exception handling
	if not usedummydata: live = True
	if not live:
		# To prevent "flooding" the live.midttrafik.dk service during development
		# this allows the use of dummy data stored in the "dummy_response" file.
		busdata = open("dummy_response").read()
		return busdata
	print("Requesting data...")
	getbussesurl = "https://live.midttrafik.dk/getbuses.php?lat={}&lon={}&radius={}".format(str(randomize_coordinates(lat)), str(randomize_coordinates(lon)), str(randomize_radius(rad)))
	data_getter = rq.urlopen(getbussesurl)  # Creates an instance of urllib.request and opening the getbusses url.
	busdata = data_getter.read()  # Throws the entire response into a single string, for later processing.
	return busdata


def getbusdom():
	# This should return an ElementTree containing all the busdata
	return Et.fromstring(allbusdata(live=False))


def print_businfo_for_line(line=100):
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
			print("{}: ".format(str(num)))
			print("Name:        " + i.attrib['Name'])
			print("Line:        " + i.attrib['Line'])
			print("Text:        " + i.attrib['DirectionText'])
			print("Delay:       " + i.attrib['Delay'])
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


# print_businfo_for_line()
# print_businfo_by_delay_range()
# count_businfo_by_delay_range(delaymax=10000, delaymin=-9000)
count_busses_on_line()

#  TODO: Save most recent response to a file, and use the file as a "cache" - preventing excessive requests.
#  TODO: Seperate the functions into individual .py file each, allowing supersimple stand-alone use.
