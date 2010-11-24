import urllib2
# retrieves the photo of the Student or ( Staff ~ coming soon )
def main():
	url = 'http://www.rp.edu.sg/staffdirectory/ShowImage.aspx?id='
	
	student_id = raw_input("Student ID : ")
	name = raw_input("Name : ")
	name2 = name.upper().replace(' ', '%20')
	url = url + student_id + '-' + name2 + '.jpg'
	image = urllib2.urlopen(url).read()
	filename = name + '.jpg'
	
	f = open(filename, "wb")
	f.write(image)
	f.close()
	print 'Done'
	
if __name__ == '__main__':
	main()