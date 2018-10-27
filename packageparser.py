import json
import math
import io
from colors import rgb, hsv, hex, random
import webbrowser

motherobject = []  # behold the mother object
packetfile = "/Users/antonionogueras/Desktop/innanet/colortheinnanet/packetz.json"

# -------- functions #

# -- checking size of the time from last packet and converts it to velocity rate

def calculatevariance(num, modulus, divide):
		return (num - (num % modulus)) / divide

def variancechecker(i):
		if i == 1000000:
				return 0.0095
		elif i < 1000000 and i >= 100000:
				return calculatevariance(i, 50000.0, 100000000.0)
		elif i < 100000 and i >= 9500:
				return 0.095
		elif i < 9500 and i >= 1000:
				return calculatevariance(i, 500.0, 100000.0)
		elif i < 1000 and i >= 100:
				return calculatevariance(i, 50.0, 1000.0)
		elif i < 100 and i >= 5:
				return calculatevariance(i, 5.0, 10.0)
		elif i < 5 and i >= 0:
				return 15
		else:
				return i


def rulename(proto):
	protodict = {"ARP": "#7faf4c", "Broadcast": "#00d9ff", "UDP": "#7c4caf", "TCP SYN/FIN": "#808080",
							 "TCP RST": "#a9a9a9", "Bad TCP": "#ff2626", "HTTP": "#fff8dc", "ICMP": "#f19cd2",
							 "SMB": "#ffb79a", "TCP": "#FFFFFF"}
	return protodict.get(proto, "#000000")


def tcplen(tcpsize, color):
	if bool(tcpsize) and color == '#d7cd733c':
		return int(tcpsize) / 10
	elif (bool(tcpsize) and color == '#a3f0daac'):
		return int(tcpsize) / 10
	else:
		return 0


# -------- parse json data #


with open(packetfile, "r+") as file:
	data = json.load(file)

	for i in data:
		try:
			source = i["_source"]["layers"]
			timepoint = source["frame"]["frame.time_delta"]
			sizepoint = source["frame"]["frame.len"]
			colorpoint = source["eth"]["eth.dst"].split(':')
			transparencypoint = source["eth"]["eth.src"]
			protocol = source["frame"]["frame.coloring_rule.name"]
			tcplength = source["tcp"]["tcp.len"]

			# ----- colorpoint index ------ #
			firsthexsplit = colorpoint[0] + colorpoint[1] + colorpoint[2]
			secondhexsplit = colorpoint[3] + colorpoint[4] + colorpoint[5]

			# ----- make rgb index from converted hexcode ------ #
			torgb = hex(secondhexsplit).rgb
			string_rgb = str(torgb).replace(" ", "").split(',')

				# ----- variable conversions ------ #
			blendcolors = hex(firsthexsplit).screen(rgb(int(string_rgb[0]),
										int(string_rgb[1]),
										int(string_rgb[2]))).hex

			parsecolor = "#{}{}".format(blendcolors, transparencypoint[0:2])
			# print parsecolor
			timeunit = math.ceil(float(timepoint))
			babyobject = {
					'color': parsecolor,
					'size': (math.floor(int(sizepoint)) + (tcplen(tcplength, parsecolor))) / 55,
					'proto': rulename(protocol),
					'velocity': variancechecker(float(timepoint) * 1000000)
							}

			# - append to the arrays ------ #
			motherobject.append(babyobject)

		except KeyError:
			pass

#-------- print to json #

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

objfile = "objects.json"

with io.open(objfile, 'w', encoding='utf8') as outfile:
    str_ = json.dumps(motherobject, indent=4, sort_keys=True, separators=(', ',': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

print("{} Objects printed to JSON file: '{}'".format(len(motherobject), objfile))

# -------- show result #
print("Opening up the website")
webbrowser.open('http://localhost:8888')
