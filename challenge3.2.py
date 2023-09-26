class student: 

  
  def __init__(self,  name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa



def sort_students(student_list):
    sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  
    return sorted_students

students = [student("Ganga","A12",8.6),student("Sripiya","A13",8.7),student("sarath","A15",9.0),student("mani","A17",9.9)]

sorted_students = sort_students(students)

for student in sorted_students:
    print("Name: {} ,Roll Number: {}, cgpa: {}".format(student.name , student.roll_number, student.cgpa))
