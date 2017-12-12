import json

packarray = []
grouperarray = []
megarray = []
inthrees = []
hexcodes = []


with open("packetz.json", "r+") as file:

	data = json.load(file)

	for i in data:
		try:
			datapoint = i["_source"]["layers"]["ssl"]["ssl.record"]["ssl.app_data"]
			packarray.append(datapoint)
		except KeyError:
			pass

for i in packarray:
	splitter = i.split(":")
	grouperarray.append(splitter)

for i in grouperarray:
	megarray.extend(i)

composite_list = [megarray[x:x+3] for x in range(0, len(megarray), 3)]

for i in composite_list:
	joiner = ''.join(map(str, [i][0]))
	hexcode = "#{}".format(joiner)
	hexcodes.append(hexcode)


# print(packarray)
# print(grouperarray)
# print(megarray)
# print(inthrees)
# print(composite_list)
# print (hexcodes)

# newfile = "colorscopy.js"

# with open(newfile, "r+") as f:
#     first_line = f.readline()
#     if first_line != "var arrayOfColors = ":
#         lines = f.readlines()
#         f.seek(0)
#         f.write("var = arrayOfColors = " + str(hexcodes))
#         f.write(first_line)
#         f.writelines(lines)

