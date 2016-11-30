from BST import *
from Students import *
import time

#global gTotalAge = 0.0
def AverageAge(item):
        #global gTotalAge
        return int(item.age)

def main():
        #global gTotalAge
	studentlist = BST()
	count = 0

	########## Inserting ##########
	A = open('InsertNames.txt', 'r')
	start_time = time.time()
	FirstTime = True
	for line in A:
		count += 1
		w = line.split()
		pupil = Student(w[0], w[1], w[2], w[3], w[4])
		#averageage += int(w[4])
		unique = True
		if FirstTime == False:
			if studentlist.Exists(pupil):
				print "ERROR. Student:", w[0], w[1], " already entered."
				unique = False
		FirstTime = False
		if unique == True:
			studentlist.Insert(pupil)
	print "The time taken for inserting students is :", time.time() - start_time
			
	########## Traversing ##########
	start_time = time.time()
	#gTotalAge = 0.0
	totalAge = studentlist.Traverse(AverageAge)
	print "The average age for the students inserted is :",totalAge/studentlist.Size()   ##len(studentlist)
	print "The time taken for travering students is :", time.time() - start_time


	########## Deleting ##########
	start_time = time.time()
	B = open('DeleteNames.txt', 'r')
	for line in B:
		if not studentlist.Delete(Student( '', '',line.strip(),'' , '')):
			print "Error! could not delete student with SSN: ", line.strip()
	Dtime = time.time() - start_time
	print "The time taken for the students deleted is :", Dtime


	########## Retrieving ##########
	start_time = time.time()
	RAge = 0.0
	counter = 0.0
	C = open('RetrieveNames.txt', 'r')
	for line in C:
		
		Rstudent = studentlist.Retrieve(Student( '', '',line.strip(), '', ''))
		print Rstudent
		if Rstudent:
			RAge += int(Rstudent.getAge())
			counter += 1
		else:
			print "Count not retrieve student with SSN: ", line.strip()

	print "The average age for the students retrieved is :", RAge/counter
	print "The time taken for the retrieved students is :",time.time() - start_time

	print "Done!"

main()
