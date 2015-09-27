import threading
import datetime
import requests as rq


class Crawler(object):

	# get your borg on
	__shared_state = {}

	def __init__(self):
		self.__dict__ = self.__shared_state
		self.uri = None
		self.task = None
		self.data = None
		self.last_update = None
		self.delay = None


	def setup(self, uri, delay=30):
		self.uri = uri
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
		if not self.uri:
			print("No URI has been passed to the crawler. Use setup(uri, delay) to initialise the crawler.")
		elif  self.task:
			print("Crawler start attempted but crawler already running")
		else:
			self.crawl()