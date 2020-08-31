class Job:
	def __init__(self, url, dir, name, threads, size="", downloaded="", speed="", time=""):
		self.url = url
		self.dir = dir
		self.name = name
		self.threads = threads
		self.size = size
		self.downloaded = downloaded
		self.speed = speed
		self.time = time


