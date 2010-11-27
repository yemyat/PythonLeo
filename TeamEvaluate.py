#view-source:http://leo3.rp.edu.sg//projectweb/group_evaluation.asp?courseid=&projectid={CE0E2D09-6481-4582-9FBD-147B7AE7635D}
#&groupid={CE2CF573-1826-4509-A18C-77B86A5F1FAC}&lang=

import PythonLeo
import mechanize

def remove_quote(string):
	string = string.replace("'", '')
	return string
	
def pair_session(thelist):
	id_session_pairs = {}
	for i in range(0, len(thelist), 2):
		id_session_pairs[str(thelist[i])] = str(thelist[i+1])
	return id_session_pairs
	
def print_dict(thedict):
	for i in thedict:
		print thedict[i]
		 
			
def main():
	URL_LIST = {
				"current_module" : "http://leo.rp.edu.sg/workspace/studentModule.asp?",
				"current_problem": "http://leo.rp.edu.sg/workspace/studentModule.asp?site=3&disp=",
				"team_evaluation": "http://leo3.rp.edu.sg//projectweb/group_evaluation.asp?", 
				"questionnaire" : "http://leo3.rp.edu.sg//projectweb/qnn.asp?",
				#qnnid={1BB2E749-8E55-4B05-8A50-B59191CE76E5}&
				#projectid={CE0E2D09-6481-4582-9FBD-147B7AE7635D}&
				#groupid={CE2CF573-1826-4509-A18C-77B86A5F1FAC}&
				#evalid={4EF1BC0D-F01C-49BD-BB76-4FFC08A08037}&evaltype=P&
				#authorid=93635&
				#evaluatorid={CE2CF573-1826-4509-A18C-77B86A5F1FAC}&lang=ISO-8859-1"
				}
	
	leo = PythonLeo.PythonLeo("91211", "YS0gxyyq")
	project_id_list = leo.parse_id("projectid", leo.open_url(URL_LIST["current_module"]))
	group_id_list = leo.parse_id("groupid", leo.open_url(URL_LIST["current_module"]))
	
	print project_id_list[-1]
	print group_id_list[-1]
	
	# this is the key url that controls everything
	team_evaluate_url = URL_LIST["team_evaluation"] + "courseid=&projectid="+ project_id_list[-1] + "&groupid=" + group_id_list[-1] + "&lang="
	# author
	
	teammates = leo.parse_student_id(leo.open_url(team_evaluate_url))
	
	#qnnid
	qnnid = leo.get_qnnid(team_evaluate_url)
	#evalid
	evalid = leo.get_evalid(team_evaluate_url)



	
	
	
	
	

if __name__ == "__main__":
	main()
	