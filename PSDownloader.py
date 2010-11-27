import re
import os
import PythonLeo
if __name__ == "__main__":
	URL_LIST = {"current_module":"http://leo.rp.edu.sg/workspace/studentModule.asp?", #to get project_id , group_id
	"current_problem":"http://leo3.rp.edu.sg//projectweb/project_menu.asp?", #to get topic_id
	"problem_download":"http://leo.rp.edu.sg/projectweb/projectupload/savefolderas.asp?folder=/databank/projectbank/"
	};

	leo = PythonLeo.PythonLeo("91211","YS0gxyyq") #e.g. 91224, 12345
	project_id_list = leo.parse_id("projectid",leo.open_url(URL_LIST["current_module"]))
	group_id_list = leo.parse_id("groupid",leo.open_url(URL_LIST["current_module"]))
	topic_id_list = leo.parse_id("topicid",leo.open_url(URL_LIST["current_problem"]+
										"projectid="+str(project_id_list[-1])+
										"&groupid="+str(group_id_list[-1])))
			
	get_download_url = leo.open_url(URL_LIST["problem_download"]+topic_id_list[-1])
	
	
	download_url = "http://leo.rp.edu.sg"+ re.search('HREF=\"(.+?zip)',get_download_url.read()).groups()[0]
	print project_id_list[-1]
	print group_id_list[-1]
	print download_url
	os.chdir(os.path.expanduser("~/Desktop"))
	#zip_file = open("problem.zip","wb")
	#zip_file.write(	leo.open_url(download_url).read())
	#zip_file.close()
	