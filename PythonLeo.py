from ntlm import HTTPNtlmAuthHandler
import urllib2
import re
import urllib
<<<<<<< HEAD
import mechanize

=======
>>>>>>> 8127da28404b3d0357c2cd94f21cee46235a918d

class PythonLeo:
	def __init__(self, username="RP\\12345", password="abcdef"):
		self.username = "RP\\"+username
		self.password = password
		self.password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
		ntlm_auth = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(self.password_manager)
<<<<<<< HEAD
		opener = mechanize.build_opener(ntlm_auth)
		mechanize.install_opener(opener)
	
	def open_url(self, url):
		self.password_manager.add_password(None, url, self.username, self.password)
		response = mechanize.urlopen(url)
		return response
	
	def open_form(self,form_url):
		self.password_manager.add_password(None, form_url, self.username, self.password)
		page = mechanize.urlopen(mechanize.Request(form_url))
		forms = mechanize.ParseResponse(page, backwards_compat=False)
		form = forms[0]#work in this case, but need to find out a better way like get form by name
		return form		
		
	def submit_form(self,request_url,data):
		self.password_manager.add_password(None, request_url, self.username, self.password)
		req = mechanize.Request(request_url,data)
		return req
=======
		opener = urllib2.build_opener(ntlm_auth)
		urllib2.install_opener(opener)
	
	def open_url(self, url):
		self.password_manager.add_password(None, url, self.username, self.password)
		response = urllib2.urlopen(url)
		return response
>>>>>>> 8127da28404b3d0357c2cd94f21cee46235a918d
		
	def parse_id(self, which_id, from_url):
		response_id = re.findall(which_id+"=(.{38})",from_url.read())
		return response_id
		
<<<<<<< HEAD
	def parse_author_evaluator_id(self, from_url):	# evaluator_id included
		author_evaluator_dic = {}
		author_evaluatorlist = re.findall(r"'\d{5,6}', '.{38}'", from_url.read())
		for i in range(len(author_evaluatorlist)):
			authorid = author_evaluatorlist[i][1:6]
			evaluatorid = author_evaluatorlist[i][10:-1]
			author_evaluator_dic[authorid] = evaluatorid
		return author_evaluator_dic
=======
	def parse_student_id(self, from_url):	# evaluator_id included
		response_id = re.findall("'\d{5,6}'", from_url.read())
		return response_id
>>>>>>> 8127da28404b3d0357c2cd94f21cee46235a918d

		
	def get_qnnid(self, from_url):
		qnnidhtml = self.open_url(from_url).read().splitlines()[-12]
		qnnid = re.findall("(\\{.*?\\})", qnnidhtml)
		return qnnid[0]
		
	def get_evalid(self, from_url):
		evalidhtml = self.open_url(from_url).read().splitlines()[-9]
		evalidhtml = re.findall("(\\{.*?\\})", evalidhtml)
<<<<<<< HEAD
		return evalidhtml[0]	
	
	def get_quizurl(self,qnnreq):
		quizurl = re.search("(\<FRAME NAME=\"main\" SRC=\")(.+)(\"\>)", mechanize.urlopen(qnnreq).read()).group(2)
                quizurl = "http://leo3.rp.edu.sg//projectweb/" + quizurl
                return quizurl
       
   	def get_questionid(self,from_url):
   		questionid = re.search(r"\{.+\}num", self.open_url(from_url).read()).group()[0:-3]
   		return questionid  
   	
   	
   	def fill_form(self,quizform,choicelist,questionid,save_url):
   		questiondic = {}
   		for i in range (1,5):
   			questiondic [questionid+str(i)] = choicelist[i-1]
   	  	data = self.get_postdata(quizform,questiondic)
   	  	self.save_choice(save_url, data)
   		return quizform
   	def save_choice(self,save_url,data):
   		self.password_manager.add_password(None, save_url, self.username, self.password)
   		req = mechanize.Request(save_url,data)
   		self.fake_browser(req)
   		 		
	def fake_browser(self,req):
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
                req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                req.add_header('Accept-Encoding', 'gzip,deflate')
                return req
       
	def get_postdata(self,form,iddic):
		form.set_all_readonly(False)
		for k,v in iddic.items():
			control = form.find_control(name=k)
			type = control.type
			if (type == "radio"):
				control.value = [v]
			else:
				control.value = v
		submit = form.click()
		data = submit.get_data()
		return data
=======
		return evalidhtml[0]


	
>>>>>>> 8127da28404b3d0357c2cd94f21cee46235a918d
