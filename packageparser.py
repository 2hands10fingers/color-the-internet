import json
import math
import io
from colors import rgb, hsv, hex, random
import webbrowser

motherobject = [] # behold the mother object

# -------- functions #
def calculatevariance(num, modulus, divide):
    return (num - (num % modulus)) / divide

# -- checking size of the time from last packet and converts it to velocity rate
def variancechecker(i):
    if i < 1000000 and i >= 100000:
        return calculateVariance(i, 50000.0, 100000000.0)
    elif i < 100000 and i >= 1000:
        return calculateVariance(i, 500.0, 100000.0)
    elif i < 1000 and i >= 100:
        return calculateVariance(i, 50.0, 1000.0)
    elif i < 100 and i >= 5:
        return calculateVariance(i, 5.0, 10.0)
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
