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
<<<<<<< HEAD
	 
=======
		 
>>>>>>> 8127da28404b3d0357c2cd94f21cee46235a918d
			
def main():
	URL_LIST = {
				"current_module" : "http://leo.rp.edu.sg/workspace/studentModule.asp?",
				"current_problem": "http://leo.rp.edu.sg/workspace/studentModule.asp?site=3&disp=",
				"team_evaluation": "http://leo3.rp.edu.sg//projectweb/group_evaluation.asp?", 
				"questionnaire" : "http://leo3.rp.edu.sg//projectweb/qnn.asp?",
<<<<<<< HEAD
				"qnntakeurl" : "http://leo3.rp.edu.sg//projectweb/qnn_take.asp?",
		        "sessionurl" : "http://leo3.rp.edu.sg//projectweb/qnn_preset.asp?",
		        "savecharturl" : "http://leo3.rp.edu.sg//projectweb/response_chart.asp?",
		        "savequizurl" : "http://leo3.rp.edu.sg//projectweb/qnn_save_responses.asp"
=======
>>>>>>> 8127da28404b3d0357c2cd94f21cee46235a918d
				#qnnid={1BB2E749-8E55-4B05-8A50-B59191CE76E5}&
				#projectid={CE0E2D09-6481-4582-9FBD-147B7AE7635D}&
				#groupid={CE2CF573-1826-4509-A18C-77B86A5F1FAC}&
				#evalid={4EF1BC0D-F01C-49BD-BB76-4FFC08A08037}&evaltype=P&
				#authorid=93635&
				#evaluatorid={CE2CF573-1826-4509-A18C-77B86A5F1FAC}&lang=ISO-8859-1"
				}
	
<<<<<<< HEAD
	leo = PythonLeo.PythonLeo("91212", "Mm890622")
	project_id_list = leo.parse_id("projectid", leo.open_url(URL_LIST["current_module"]))
	group_id_list = leo.parse_id("groupid", leo.open_url(URL_LIST["current_module"]))
	
		#print project_id_list[-1]
		#print group_id_list[-1]
	
	# this is the key url that controls everything
	team_evaluate_url = URL_LIST["team_evaluation"] + "courseid=&projectid="+ project_id_list[-1] + "&groupid=" + group_id_list[-1] + "&lang=ISO-8859-1"
		#print team_evaluate_url
	#qnnid
	qnnid = leo.get_qnnid(team_evaluate_url)
		#print qnnid
	#evalid
	evalid = leo.get_evalid(team_evaluate_url)
		#print evalid
	#dic of evaluator&author
	author_evaluatordic = leo.parse_author_evaluator_id(leo.open_url(team_evaluate_url))
		#print author_evaluatordic
	#store author list and evaluator list
	authorlist = author_evaluatordic.keys()
	evaluatorlist = author_evaluatordic.values()
		#print author_evaluatordic
	
	#test for one student
	authorid = authorlist[0]
	evaluatorid = evaluatorlist[0]
	#this is the key url to get session id
	getsessionurl = URL_LIST["sessionurl"] + "&qnnid=" + qnnid + "&projectid=" + project_id_list[-1]+ "&groupid=" + group_id_list[-1] + "&evalid=" + evalid + "&evaltype=P" + "&authorid=" + authorid + "&evaluatorid=" + evaluatorid + "&lang=ISO-8859-1"
    #set form values
	GETSESSIONFORMVALUE = {
					"qnnid" : qnnid,            
	                "authorid" : authorid,
	                "evaluatorid" : evaluatorid,
	               	"evaltype" : "P",
	                "lang": "ISO-8859-1",
	                "newflag" : "0",
	                "evalid": evalid,
	                "groupid": group_id_list[-1],
	                "projectid": project_id_list[-1]
					}  
    #submit the form to get session id
	form = leo.open_form(getsessionurl)
	data = leo.get_postdata(form,GETSESSIONFORMVALUE)
	qnntakeurl = URL_LIST["qnntakeurl"] 
	qnnreq = leo.submit_form(qnntakeurl,data)
	sessionid = leo.parse_id("sessionid",mechanize.urlopen(qnnreq))[0]
	quizurl = leo.get_quizurl(qnnreq)
	questionid = leo.get_questionid(quizurl)
	quizform = leo.open_form(quizurl)
	#change to your own list
	choicelist = ["5","5","5","5"]
	save_url = URL_LIST["savecharturl"]
	finishedquizform = leo.fill_form(quizform,choicelist,questionid,save_url)
		#print finishedquizform
	#get quizdata
	quizdata = leo.get_postdata(quizform,{"finish":"MANUAL"})
	savequizurl = URL_LIST["savequizurl"]
	print quizdata
		#submit quizform
		#quizreq = leo.submit_form(savequizurl,quizdata)
		#print mechanize.urlopen(quizreq).read()
=======
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



	
	
	
	
	
>>>>>>> 8127da28404b3d0357c2cd94f21cee46235a918d

if __name__ == "__main__":
	main()
	