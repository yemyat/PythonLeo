from ntlm import HTTPNtlmAuthHandler
import urllib2
import re

class PythonLeo:
	def __init__(self, username="RP\\12345", password="abcdef"):
		self.username = "RP\\"+username
		self.password = password
		self.password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
		ntlm_auth = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(self.password_manager)
		opener = urllib2.build_opener(ntlm_auth)
		urllib2.install_opener(opener)
	
	def open_url(self, url):
		self.password_manager.add_password(None, url, self.username, self.password)
		response = urllib2.urlopen(url)
		return response
		
	def parse_id(self, which_id, from_url):
		response_id = re.findall(which_id+"=(.{38})",from_url.read())
		return response_id
	
	
	
	
	