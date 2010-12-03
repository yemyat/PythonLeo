import HTTPNtlmAuthHandler
import os
import sys
import BaseHTTPServer
from Tkinter import *
import tkMessageBox
import re
import mechanize
from mechanize import ParseResponse, urlopen, urljoin
import random

class GUIFramework(Frame):

    def __init__(self, master=None):
        
        
        Frame.__init__(self, master)
        
        self.master.title("RP Evaluation AutoFiller")
        

        self.grid(padx=50, pady=50)
        self.CreateWidgets()
       
    def CreateWidgets(self):
        
        self.lID = Label(self, text="Student ID: ")
        self.lID.grid(row=0, column=0)
        
        self.ID = Entry(self)
        self.ID.grid(row=0, column=1, columnspan=6)
        
        self.lPD = Label(self, text="Password: ")
        self.lPD.grid(row=1, column=0)
        
        self.PD = Entry(self, show="*")
        self.PD.grid(row=1, column=1, columnspan=6)
        self.lR = Label(self, text="Rate: ")
        self.lR.grid(row=2, column=0)
        self.R = Listbox(self)   
        for item in ["1", "2", "3", "4", "5", "Random"]:
            self.R.insert(END, item)
        self.R.grid(row=2, column=1, columnspan=6)

        self.btnSubmit = Button(self, text="Submit", command=self.Evaluate)
        self.btnSubmit.grid(row=3, column=1)
        
        self.vWL = StringVar()
        self.WL = Label(self, textvariable=self.vWL)
        self.WL.grid(row=4, column=1)
        self.vNP = StringVar()
        self.NP = Label(self, textvariable=self.vNP)
        self.NP.grid(row=5, column=1)
    
    def Evaluate(self):
        self.vWL.set("Processing...... please wait")
        user = self.ID.get()
        self.vWL.set("")
        self.vNP.set("")
        if ("RP\\" not in user):
            user = "RP\\" + user
        password = self.PD.get()
        choice = self.R.curselection()
        if (len(choice) == 1):
                choice = self.R.get(choice[0])
        else:
            self.vWL.set("Wrong Selection!")
        try:
            formpage = self.getformpage(user, password, choice)
            self.vWL.set("Finished!")

        except    mechanize.URLError, urle:
            self.vNP.set("Sorry, url is wrong or no internet!")
            
    def getidlist(self, idname, page):
        list = re.findall(idname + "=.{38}", page)
        return list
    def gethiddenid(self, idname, page):
        return re.search(r"name=\"" + idname + "\" value=\"(.{38})\"", page).group(1)
            
    def addAuthentication(self, url, username, password):
        passman = mechanize.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, username, password)
        # create the NTLM authentication handler
        auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
        
        # create and install the opener
        opener = mechanize.build_opener(auth_NTLM)
        return opener
    def getformpage(self, user, password, choice):
        projectgroupurl = "http://leo.rp.edu.sg//workspace/studentModule.asp?site="
        qnnurl = "http://leo3.rp.edu.sg//projectweb/group_evaluation.asp?"
        quizurl = "http://leo3.rp.edu.sg//projectweb/qnn_take.asp?"
        sessionurl = "http://leo3.rp.edu.sg//projectweb/qnn_preset.asp?"
        charturl = "http://leo3.rp.edu.sg//projectweb/response_chart.asp?"
        saveurl = "http://leo3.rp.edu.sg//projectweb/qnn_save_responses.asp"
        urllist = []
        for i in range (1, 4):
            urllist.append(projectgroupurl + str(i))
        
        # retrieve the result
        currentModule = "projectid"
        currentProblem = "groupid"
        try:    
            for url in urllist:
                opener = self.addAuthentication(url, user, password)
                mechanize.install_opener(opener)
                response = mechanize.Request(url)
                page = urlopen(response).read()
                if ("Wrong Password" in page or "Wrong ID" in page):
                    self.vNP.set("Sorry, USERNAME or PASSWORD wrong!")
                elif ('''ToggleDisplay''' in page):
                    currentModule = self.getidlist("projectid", page)[-1]
                    currentProblem = self.getidlist("groupid", page)[-1]
            if (currentModule != "projectid" and currentProblem != "groupid"):
                getqnnurl = qnnurl + currentModule + "&" + currentProblem + "&lang=ISO-8859-1"
                opener = self.addAuthentication(getqnnurl, user, password)
                mechanize.install_opener(opener)
                response = mechanize.Request(getqnnurl)
                getqnnpage = urlopen(response)
                forms = ParseResponse(getqnnpage, backwards_compat=False)
                form = forms[0]
                qnnid = form["qnnid"]
                evalid = form["evalid"]
                opener = self.addAuthentication(getqnnurl, user, password)
                mechanize.install_opener(opener)
                response = mechanize.Request(getqnnurl)
                getqnnpageread = urlopen(response).read()
                author_evaluatorlist = re.findall(r"'\d{5}', '.{38}'", getqnnpageread)
                #for i in range(len(author_evaluatorlist)):
                authorid = author_evaluatorlist[0][1:6]
                evaluatorid = author_evaluatorlist[0][10:-1]
                getsessionurl = sessionurl + "&qnnid=" + qnnid + "&" + currentModule + "&" + currentProblem + "&evalid=" + evalid + "&evaltype=P" + "&authorid=" + authorid + "&evaluatorid=" + evaluatorid + "&lang=ISO-8859-1"
                opener = self.addAuthentication(getsessionurl, user, password)
                mechanize.install_opener(opener)
                response = mechanize.Request(getsessionurl)
                getqnnpage = urlopen(response)
                forms = ParseResponse(getqnnpage, backwards_compat=False)
                form = forms[0]
                form.set_all_readonly(False)
                form["qnnid"] = qnnid            
                form["authorid"] = authorid
                form["evaluatorid"] = evaluatorid
                form["evaltype"] = "P"
                form["lang"] = "ISO-8859-1"
                form["newflag"] = "0"
                form["evalid"] = evalid
                form["groupid"] = currentProblem[8:]
                form["projectid"] = currentModule[10:]
                submit = form.click()
                data = submit.get_data()
                opener = self.addAuthentication(quizurl, user, password)
                mechanize.install_opener(opener)
                response = mechanize.Request(quizurl, data)
                sessionid = self.getidlist("sessionid", urlopen(response).read())[0]
                answerurl = re.search("(\<FRAME NAME=\"main\" SRC=\")(.+)(\"\>)", urlopen(response).read()).group(2)
                answerurl = "http://leo3.rp.edu.sg//projectweb/" + answerurl
                opener = self.addAuthentication(answerurl, user, password)
                mechanize.install_opener(opener)
                rs = mechanize.Request(answerurl, data)
                quiz = urlopen(rs)
                quizpage = urlopen(rs).read()
                questionid = re.search(r"\{.+\}num", quizpage).group()[0:-3]
                forms = ParseResponse(quiz, backwards_compat=False)
                form = forms[0]
                self.fillform(form, choice,questionid,sessionid,charturl,user,password)
                form.set_all_readonly(False)
                form["finish"] = "MANUAL"
                print form
                '''
                data = form.click().get_data()
                opener = self.addAuthentication(saveurl, user, password)
                mechanize.install_opener(opener)
                req = mechanize.Request(saveurl, data)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
                req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                req.add_header('Accept-Encoding', 'gzip,deflate')
                print urlopen(req).read()
                '''
            else:
                self.vNP.set("Sorry, TODAY NO MODULE!")
        except mechanize.HTTPError, e:
                self.vNP.set("Error:",BaseHTTPServer.BaseHTTPRequestHandler.responses[e.code])
        except IndexError, ie:
                self.vNP.set("Sorry, No one to evaluate")
    def fillform(self, form, choice,questionid,sessionid,charturl,user,password):
        if choice != "Random":
            for i in range(1, 5):
                form[questionid + str(i)] = [choice]
        else:
            for i in range(1, 5):
                form[questionid + str(i)] = [str(random.randint(1, 5))]
        data = form.click().get_data()
        charturl += sessionid + "&questionid=" + questionid + "&qtype=" + "LS"
        opener = self.addAuthentication(charturl, user, password)
        mechanize.install_opener(opener)
        req = mechanize.Request(charturl, data)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Accept-Encoding', 'gzip,deflate')

guiFrame = GUIFramework()
guiFrame.mainloop()
