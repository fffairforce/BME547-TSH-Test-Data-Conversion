def main():
    f = read_txt()
    person_info = new_person(f)
    output_patient(person_info)


def read_txt():
    """	to make sure the file can be read till END is detected.
    which is able for the module to work on different length of data file
    """
    i = 0
    text_file = []
    with open("test_data.txt", "r") as x:
        lines = x.readlines()
    while not lines[i].startswith("END"):
        text_file.append(lines[i].strip())
        i += 1
    return text_file


class Person:
    """
    Person class stores patient information including firstname, lastname, age,
     gender, tsh results, diagnosis.
    Args:
        firstname (str): first name
        lastname (str): last name
        age (float): age
        gender (str): Female/Male
        test (float): tsh results lists
        diagnosis (str): to check if the patient is "hyperthyroidism",
        "hypothyroidism", or has "normal thyroid function"

    """

    def __init__(self, firstname, lastname, age, gender, test, diagnosis):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.test = test
        self.diagnosis = diagnosis


def new_person(n):
    """
    introduce information in txt file to class [person] as objects

    Args:
        n (list): information of patients from read_txt()

    Return:
        list: patient class object
    """
    patients = []
    i = 0
    j = 1
    while i < len(n):
        name = n[i].split()
        diagnosis = diagnose(n[i + 3])
        patients.append(Person(
            name[0],  # first name
            name[1],  # last name
            n[i + 1],  # age
            n[i + 2],  # gender
            diagnosis[1],  # tsh
            (diagnosis[0]),  # diagnosis
        )
        )
        i += 4
        j += 1
    return patients


def output_patient(y):
    """set up patient dictionary and create json file.
    the output json file5 has a format of:
    * first name
    * last name
    * age
    * gender
    * diagnosis
    * TSH
    """
    import json
    i = 0
    while i < len(y):
        dic_person = {
            "Firstname": y[i].firstname,
            "Lastname": y[i].lastname,
            "Age": y[i].age,
            "Gender": y[i].gender,
            "TSH": y[i].test,
            "Diagnosis": y[i].diagnosis
        }
        out_file = open("{},{}.json".format(y[i].firstname, y[i].lastname),
                        "w")

        json.dump(dic_person, out_file)
        out_file.close()
        i += 1


def diagnose(t):
    test_values = t.split(",")
    test_values = [x for x in test_values if "TSH" not in x]
    test_values = list(map(float, test_values))
    if max(test_values) > 4:
        result = 'Hypothyroidism'
    elif min(test_values) < 1:
        result = 'Hyperthyroidism'
    else:
        result = 'normal thyroid function'
    return sorted(test_values), result


if __name__ == "__main__":
    main()
