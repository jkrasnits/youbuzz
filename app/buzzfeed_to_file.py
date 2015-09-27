#!/usr/bin/python
import requests, json, html	


fo = open("corpus.txt", "a")
data = requests.get('http://www.buzzfeed.com/api/v2/feeds/index')
parse_data = data.json()
#print(parse_data["ad_backfill"])

for x in range(0, 15):
	print('http://www.buzzfeed.com/api/v2/feeds/lol?p=' + str(x))
	data = requests.get('http://www.buzzfeed.com/api/v2/feeds/lol?p=' + str(x))
	parse_data = data.json()
	for item in parse_data['flow']:
	    #print(item['content']['feed']['title']);
	    fo.write(html.unescape(item['content']['feed']['title']+"\n"))


# # Open a file
# fo = open("foo.txt", "w")
# fo.write(r.text);

# # Close opend file
fo.close()