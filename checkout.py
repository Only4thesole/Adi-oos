import main
import cli
import bruteforce
import billing
import ATC
import twocap

class Checkout(object):
	def get_profile(self):
		next_profile = self.active_profiles[1]
		next_size = self.active_sizes[1]
		self.profile_to_search = next_profile
		self.size_input = next_size
		basesize = 580
		selsize = self.sizeinput * 20
		sumsize = selsize + BaseSize
		rawsize = sumsize - 130
		self.size = int(rawsize)
		del self.active_profiles[1]
		del self.active_sizes[1]