import urllib2
import re
import PythonLeo

def removeDuplicate(foo):
    bar = []
    for i in range(len(foo)):
        if i %2 == 0:
            bar.append(foo[i])
    return bar

def get_grades(from_url):
    grades_list = re.findall(r"<b>.*([ABCDFX]{1}).*</b>", from_url.read())
    grades_list.pop(0)
    grades_list.pop(-1)
    return grades_list

def get_module(from_url):
    #module = re.search('([A-Z]\d\d\d-[12348]-[WE]\d\d[A-Z]-[ABC])', from_url.read())
    module = re.search('([A-Z]\d\d\d)', from_url.read())
    return module.groups()[0]

def main():
	url = 'http://leo.rp.edu.sg/workspace/studentGrades.asp'
	url2 = 'http://leo3.rp.edu.sg//projectweb/student_summary.asp?'

	myGrades = PythonLeo.PythonLeo("91178", "pyro1$cute") #student ID & Password
	
	course_id_list = removeDuplicate(myGrades.parse_id("courseid", myGrades.open_url(url)))
	#project_id_list = myGrades.parse_id("projectid", myGrades.open_url(url))
	
	f = open('grades.txt', 'wb')
	for course in course_id_list:
		url = url2 + 'courseid=' + course
		f.write(get_module(myGrades.open_url(url)) + '\r\n')
		gradesList = get_grades(myGrades.open_url(url))
		for grade in range(len(gradesList)):
			f.write('Problem ' + str(grade+1) + " : " + gradesList[grade] + '\r\n')
		f.write('\r\n')
	f.close()
	print 'Done'
	

if __name__ == "__main__":
	main()
            
            


        




   
            
            

        
