import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"	

def loadRSS():
	'''
	utility function to load RSS feed
	'''
	resp = requests.get(RSS_FEED_URL)

	return resp.content

def parseXML(rss):
	'''
	utility function to parse XML format rss feed
	'''t
	root = ET.fromstring(rss)

	newsitems = []

	for item in root.findall('./channel/item'):
		news = {}

		for child in item:

			if child.tag == '{http://search.yahoo.com/mrss/}content':
				news['media'] = child.attrib['url']
			else:
				news[child.tag] = child.text.encode('utf8')
		newsitems.append(news)

	return newsitems

def topStories():
	'''
	main function to generate and return news items
	'''
	rss = loadRSS()

	newsitems = parseXML(rss)
	return newsitems

    #topnews.py
    #pip install notify2
#notify2.init("News Notifier")
#n = notify2.Notification(None, icon = ICON_PATH)
#notify2.Notification(summary, message='', icon='')
#n.set_urgency(notify2.URGENCY_NORMAL)
#n.set_timeout(10000)
#n.update(newsitem['title'], newsitem['description'])
#n.show()