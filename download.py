# This is to download gifs from slack
import json
import urllib2

# Open and load json file
with open('gifs.json') as json_data:
	d = json.load(json_data)
	json_data.close()

	# Loop through all the entries
	for key in d["emoji"].keys():
		# Get the URL
		url = d["emoji"][key]
		print("NAME: " + key)
		print("URL: " + url)

		if "alias:" not in url:
			# Get the file extension since not everything is a gif but we want it anyways
			ext = url[-4:]
			
			filedata = urllib2.urlopen(url)
			datatowrite = filedata.read()

			# write data to file
			with open('gifs/' + key + ext, "wb") as f:
				f.write(datatowrite)