from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?"

#open the apiUrl and assign data to variable
response = urlopen(apiUrl)

json_obj = load(response)

# print json_obj

# for index in range(len(json_obj)):
# 	if "locations" in json_obj[index].keys():
# 		print "Location",json_obj[index]["locations"]
# 	if "actor_1" in json_obj[index].keys():
# 		print "Actor",json_obj[index]["actor_1"]

for index in range(len(json_obj)):
	if "locations" in json_obj[index].keys() and "actor_1" in json_obj[index].keys():
		print "Location",json_obj[index]["locations"], "Actor",json_obj[index]["actor_1"]