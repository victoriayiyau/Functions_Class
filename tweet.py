def send_tweet(self, tweet):
		print "@%s - %s" % (self.twitter_handle, tweet)

	def send_email(self, message):
		print "To: %s - %s" % (self.email, message)
