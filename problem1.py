import requests 

inFile = [i.strip().replace(' ', '+') for i in open('input.txt').readlines()] #reads input file and converts each line elemenst of a list
distance = {}

for destination in inFile :  #loop necessary beacause of google directions api support one origin and destination at one time
	get = {'origin' : 'IIT+Bombay', 'destination' : destination, 'alternatives' : 'true'}
	requestItems = "&".join("%s=%s" % (k,v) for k,v in get.items())
	r = requests.get('https://maps.googleapis.com/maps/api/directions/json' , params=requestItems)
	r = r.json()
	distance[destination] = min([route['legs'][0]['distance']['value'] for route in r['routes']])

for k,v in sorted(distance.items(), key=lambda x:x[1]) :
	print (k.replace('+', ' '))
