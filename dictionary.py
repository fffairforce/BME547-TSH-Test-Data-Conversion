import json

my_dictionary = {
                "Name": "Firstname Lastname", 
                "School": "Duke University"
                 }

out_file = open("filename.json", "w")
json.dump(my_dictionary, out_file)
out_file.close()

class person():
def __init__(self, Firstname, Lastname, Age, Gender, name of test):
	self.firstname = Firstname
	self.lastname = Lastname
	self.age = Age
	self.gender = Gender
	self.test = name of test
	
def create_person(): 
	{"Firstname Lastname": "",
                          "Age": "",
						  "Gender": "",
						  "name of test": ""
	}