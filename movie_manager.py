from movie_info_class import *
from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?"

#open the apiUrl and assign data to variable
response = urlopen(apiUrl)

json_obj = load(response)

#list of objects using class and json
movie_list = []

#iterating thru json list, extracting info using our class with specific keys
for movie in json_obj:
	movie_title = "" 
	movie_year = ""
	movie_director = ""
	movie_actor1 = ""
	movie_actor2 = ""
	movie_locations = ""
	if "title" in movie:
		movie_title = movie["title"].encode("ascii","ignore")
	if "release_year" in movie:
		movie_year = str(movie["release_year"].encode("ascii","ignore"))
	if "director" in movie:
		movie_director = str(movie["director"].encode("ascii","ignore"))
	if "actor_1" in movie:
		movie_actor1 = str(movie["actor_1"].encode("ascii","ignore"))
	if "actor_2" in movie:
		movie_actor2 = str(movie["actor_2"].encode("ascii","ignore"))
	if "locations" in movie:
		movie_locations = str(movie["locations"].encode("ascii","ignore"))
	
	movie_information = movie_info(movie_title,
		movie_year,movie_director,movie_actor1,movie_actor2,
		movie_locations)
	
		#adding movie info to new list
	movie_list.append(movie_information)
	# elif movie["actor_2"] == None:
	# 	movie_information = movie_info(movie["title"],
	# 	movie["release_year"],movie["director"])
	#adding movie info to new list
	print "Title: " + movie_information.title
	# print "Release year: "+ movie_information.release_year
	# print "Director: " + movie_information.director

# print movie_list