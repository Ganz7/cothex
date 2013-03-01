import urllib
import json
import requests

def searchTweets(query):
	attributes = {'q' : query,
			'rpp': 500}
	url = 'http://search.twitter.com/search.json'
	r = requests.get(url, params = attributes)
	dict = json.loads(r.text)
	#search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
	#dict = json.loads(search.read())
	return dict
