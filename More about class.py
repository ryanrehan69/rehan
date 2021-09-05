print("Data of five students...")
class data():
	def __init__(self, name, id, section):
		
		self.name = name
		self.id = id
		self.section = section
	
	def self_data(self):
		print("Name: ", self.name)
		print("Id: ", self.id)
		print("Section: ", self.section)
		
student_1 = data("Rehan", " 01", "CSE")
student_2 = data("Rimi", " 02", "MBBS")
student_3 = data("Artho", "03", " MANAGEMENT")

student_1.self_data()
student_2.self_data()
student_3.self_data()