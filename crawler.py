import threading
import datetime
import requests as rq


class Crawler(object):

	def __init__(self, uri, delay = 30):
		self.uri = uri
		self.task = None
		self.data = None
		self.last_update = None
		self.delay = delay

	def crawl(self):
		# pick up the latest data
		print("Picking up data")
		r = rq.get(self.uri)
		self.data = r.text
		self.last_update = datetime.datetime.now()

		# schedule again
		self.task = threading.Timer(self.delay, self.crawl)
		self.task.daemon = True
		self.task.start()

	def stop(self):
		self.task._stop.set()

	def start(self):
		self.crawl()