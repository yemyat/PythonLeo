import urllib2
import os
# retrieves the photo of the Student
# V 1.0 retrieves photo of the student
# V 1.1 added support for full-time staff.

url = 'http://www.rp.edu.sg/staffdirectory/ShowImage.aspx?id='

def main():
	print 'Welcome to LEO Pic Retriever'
	input = raw_input("Press\n1.\t for students\n2.\t for staff\n Input : : ")
	if(int(input) == 1):
		student()
	elif(int(input) == 2):
		staff()
	else:
		main()
		
def save_image(image_url, name):
	image = urllib2.urlopen(image_url).read()
	filename = name + '.jpg'
	os.chdir(os.path.expanduser("~/Desktop"))
	f = open(filename, "wb")
	f.write(image)
	f.close()
	print 'Done. Check your desktop!'
	
def student():
	student_id = raw_input("Student ID : ")
	name = raw_input("Name : ")
	name2 = name.upper().replace(' ', '%20')
	image_url = url + student_id + '-' + name2 + '.jpg'
	save_image(image_url, name)
	
def staff():
	staff_name = raw_input("Enter Staff's Name :");
	staff_name_small = staff_name.lower().replace(' ', '_')
	staff_name_big = staff_name.upper().replace(' ', '%20')
	image_url = url + staff_name_small + "-" + staff_name_big + '.jpg'
	save_image(image_url, staff_name)

	
if __name__ == '__main__':
	main()