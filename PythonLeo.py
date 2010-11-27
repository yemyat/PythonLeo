from ntlm import HTTPNtlmAuthHandler
import urllib2
import re
import urllib

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
		
	def parse_student_id(self, from_url):	# evaluator_id included
		response_id = re.findall("'\d{5,6}'", from_url.read())
		return response_id

		
	def get_qnnid(self, from_url):
		qnnidhtml = self.open_url(from_url).read().splitlines()[-12]
		qnnid = re.findall("(\\{.*?\\})", qnnidhtml)
		return qnnid[0]
		
	def get_evalid(self, from_url):
		evalidhtml = self.open_url(from_url).read().splitlines()[-9]
		evalidhtml = re.findall("(\\{.*?\\})", evalidhtml)
		return evalidhtml[0]


	