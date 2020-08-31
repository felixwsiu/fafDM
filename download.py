# In charge of starting asynchronous downloads, should provide updates to 
# UI for info on each download. Files are split into chunks and streamed
# with multiple threads

#import faster_than_requests as requests

def dlAsync(job):
	print("STARTING DOWNLOAD OF FILE : " + job.name)

