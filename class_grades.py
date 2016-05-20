list_grade = []

def process_file():
	global list_grade
	# Read the file
	with open("class_grades.txt") as grade_file:
		list_grade = grade_file.readlines()
	print list_grade
	
	# Clear the invisibles from the list
	for index in range(len(list_grade)):
		list_grade[index] = int(list_grade[index].strip().strip('\xef\xbb\xbf'))
	#print list_grade

def convert_score(score):
	if score >= 90:
		return "A"
	elif 89 >= score >= 80:
		return "B"
	elif 79 >= score >= 70:
		return "C"
	elif 69 >= score >= 60:
		return "D"
	else:
		return "F"

def main():
	global list_grade
	process_file()
	for grade in list_grade:
		letter_grade = convert_score(grade)
		print grade,"is a",letter_grade

if __name__ == '__main__':
	main()