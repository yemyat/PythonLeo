from ntlm import HTTPNtlmAuthHandler
from Tkinter import *
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

if __name__ == "__main__":
	URL_LIST = {"current_module":"http://leo.rp.edu.sg/workspace/studentModule.asp?", #to get project_id , group_id
	"current_problem":"http://leo3.rp.edu.sg//projectweb/project_menu.asp?", #to get topic_id
	"problem_download":"http://leo.rp.edu.sg/projectweb/projectupload/savefolderas.asp?folder=/databank/projectbank/"
	};

	test = PythonLeo("username","password") #e.g. 91224, 12345
	project_id_list = test.parse_id("projectid",test.open_url(URL_LIST["current_module"]))
	group_id_list = test.parse_id("groupid",test.open_url(URL_LIST["current_module"]))
	topic_id_list = test.parse_id("topicid",test.open_url(URL_LIST["current_problem"]+
										"projectid="+str(project_id_list[-1])+
										"&groupid="+str(group_id_list[-1])))
			
	get_download_url = test.open_url(URL_LIST["problem_download"]+topic_id_list[-1])
	
	download_url = "http://leo.rp.edu.sg"+ re.search('HREF=\"(.+?zip)',get_download_url.read()).groups()[0]
	
	zip_file = open("problem.zip","wb")
	zip_file.write(	test.open_url(download_url).read())
	zip_file.close()
	
	
	
	
	