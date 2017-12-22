import json
import math
import io
from colors import rgb, hsv, hex, random
import webbrowser

motherobject = [] # behold the mother object

# -------- functions #
# -- checking size of the time from last packet and converts it to velocity rate
# -- yes, it looks ugly; i'm sorry...
def variancechecker(i):
		if i <= 1000000 and i >= 950000:
			 return 0.0095
		elif i < 950000 and i >= 900000:
			 return 0.0090
		elif i < 900000 and i >= 850000:
			 return 0.0085
		elif i < 850000 and i >= 800000:
			 return 0.0080
		elif i < 800000 and i >= 750000:
			 return 0.0075
		elif i < 750000 and i >= 700000:
			 return 0.0070
		elif i < 700000 and i >= 650000:
			 return 0.0065
		elif i < 650000 and i >= 600000:
			return 0.0060
		elif i < 600000 and i >= 550000:
			return 0.0055
		elif i < 550000 and i >= 500000:
			return 0.0050
		elif i < 500000 and i >= 450000:
			return 0.0045
		elif i < 450000 and i >= 400000:
			return 0.0040
		elif i < 400000 and i >= 350000:
			return 0.0035
		elif i < 350000 and i >= 300000:
			return 0.0030
		elif i < 300000 and i >= 250000:
			return 0.0025
		elif i < 250000 and i >= 200000:
			return 0.0020
		elif i < 200000 and i >= 150000:
			return 0.0015
		elif i < 150000 and i >= 100000:
			return 0.0010
		elif i < 100000 and i >= 9500:
			return 0.095
		elif i < 9500 and i >= 9000:
			return 0.090
		elif i < 9000 and i >= 8500:
			return 0.085
		elif i < 8500 and i >= 8000:
			return 0.080
		elif i < 8000 and i >= 7500:
			return 0.075
		elif i < 7500 and i >= 7000:
			return 0.070
		elif i < 7000 and i >= 6500:
			return 0.065
		elif i < 6500 and i >= 6000:
			return 0.060
		elif i < 6000 and i >= 5500:
			return 0.055
		elif i < 5500 and i >= 5000:
			return 0.050
		elif i < 5000 and i >= 4500:
			return 0.045
		elif i < 4500 and i >= 4000:
			return 0.040
		elif i < 4000 and i >= 3500:
			return 0.035
		elif i < 3500 and i >= 3000:
			return 0.030
		elif i < 3000 and i >= 2500:
			return 0.025
		elif i < 2500 and i >= 2000:
			return 0.020
		elif i < 2000 and i >= 1500:
			return 0.015
		elif i < 1500 and i >= 1000:
			return 0.010
		elif i < 1000 and i >= 950:
			return 0.95
		elif i < 950 and i >= 900:
			return 0.90
		elif i < 900 and i >= 850:
			return 0.85
		elif i < 850 and i >= 800:
			return 0.80
		elif i < 800 and i >= 750:
			return 0.75
		elif i < 750 and i >= 700:
			return 0.70
		elif i < 700 and i >= 650:
			return 0.65
		elif i < 650 and i >= 600:
			return 0.60
		elif i < 600 and i >= 550:
			return 0.55
		elif i < 550 and i >= 500:
			return 0.50
		elif i < 500 and i >= 450:
			return 0.45
		elif i < 450 and i >= 400:
			return 0.40
		elif i < 400 and i >= 350:
			return 0.35
		elif i < 350 and i >= 300:
			return 0.30
		elif i < 300 and i >= 250:
			return 0.25
		elif i < 250 and i >= 200:
			return 0.20
		elif i < 200 and i >= 150:
			return 0.15
		elif i < 150 and i >= 100:
			return 0.10
		elif i < 100 and i >= 95:
			return 9.5
		elif i < 95 and i >= 90:
			return 9.0
		elif i < 90 and i >= 85:
			return 8.5
		elif i < 85 and i >= 80:
			return 8.0
		elif i < 80 and i >= 75:
			return 7.5
		elif i < 75 and i >= 70:
			return 7.0
		elif i < 70 and i >= 65:
			return 6.5
		elif i < 65 and i >= 60:
			return 6.0
		elif i < 60 and i >= 55:
			return 5.5
		elif i < 55 and i >= 50:
			return 5.0
		elif i < 50 and i >= 45:
			return 4.5
		elif i < 40 and i >= 35:
			return 4.0
		elif i < 35 and i >= 30:
			return 3.5
		elif i < 30 and i >= 25:
			return 3.0
		elif i < 25 and i >= 20:
			return 2.5
		elif i < 20 and i >= 15:
			return 2.0
		elif i < 15 and i >= 10:
			return 1.5
		elif i < 10 and i >= 5:
			return 1.0
		elif i < 5 and i >= 0:
			return 15
		else:
			return i


def rulename(proto):
	if proto == "ARP":
		return "#7faf4c"
	elif proto == "Broadcast":
		return "#00d9ff"
	elif proto == "UDP":
		return "#7c4caf"
	elif proto == "TCP":
		return "#FFFFFF"
	elif proto == "TCP SYN/FIN":
		return "#808080"
	elif proto == "TCP RST":
		return "#a9a9a9"
	elif proto == "Bad TCP":
		return "#ff2626"
	elif proto == "HTTP":
		return "#fff8dc"
	elif proto == "ICMP":
		return "#f19cd2"
	elif proto == "SMB":
		return "#ffb79a"
	else:
		return "nothing"

def tcplen(tcpsize, color):
	if bool(tcpsize) == True and color == '#d7cd733c':
		return int(tcpsize) / 10
	elif (bool(tcpsize) == True and color == '#a3f0daac'):
		return int(tcpsize) / 10
	else:
		return 0

# -------- parse json data #
packetfile = "/Users/antonionogueras/Desktop/packetz.json"
with open(packetfile, "r+") as file:
	data = json.load(file)

	for i in data:
		try:
			# - variables ------ #
				# ----- json datapoints ------ #
			timepoint = i["_source"]["layers"]["frame"]["frame.time_delta"]
			sizepoint = i["_source"]["layers"]["frame"]["frame.len"]
			colorpoint = i["_source"]["layers"]["eth"]["eth.dst"].split(':')
			transparencypoint = i["_source"]["layers"]["eth"]["eth.src"]
			protocol = i["_source"]["layers"]["frame"]["frame.coloring_rule.name"]
			tcplength = i["_source"]["layers"]["tcp"]["tcp.len"]

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

# -------- print to json #

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
