import PythonLeo
# retrieves the photo of the student that you want to retrieve

def main():
	url = 'http://myrp.sg/SASS-Student/Photo/'
	myid = '91178'
	mypassword = 'pyro1$cute'
	
	student_id = raw_input("Student ID : ")
	name = raw_input("Name : ")
	name2 = name.upper().replace(' ', '%20')
	url = url + student_id + '-' + name2 + '.jpg'
	
	login = PythonLeo.PythonLeo(myid, mypassword)
	image = login.open_url(url).read()
	filename = name + '.jpg'
	
	f = open(filename, "wb")
	f.write(image)
	f.close()
	print 'Done'
	
if __name__ == '__main__':
	main()