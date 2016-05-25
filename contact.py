class Contact(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile_number = ""
		self.work_number = ""
		self.email = ""
		self.twitter_handle = ""

	def send_tweet(self, tweet):
		print "@%s - %s" % (self.twitter_handle, tweet)

	def send_email(self, message):
		print "To: %s - %s" % (self.email, message)


