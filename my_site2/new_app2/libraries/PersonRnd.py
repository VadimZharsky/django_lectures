from calendar import month
from random import randint

def get_firstname():
    first_names = ["Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Henry",
                "Theodore", "Jack", "Levi", "Alexander", "Jackson", "Mateo", "Daniel", "Michael", "Mason", "Sebastian",
                "Ethan", "Logan", "Owen", "Samuel", "Jacob", "Asher", "Aiden", "John", "Joseph", "Wyatt", "David", "Leo",
                "Luke", "Julian", "Hudson", "Grayson", "Matthew", "Ezra", "Gabriel", "Carter", "Isaac", "Jayden", "Luca"
                 ]
    ind = randint(0, first_names.__len__()-1)
    return first_names[ind]

def get_lastname():
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", 
                "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
                "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
                "Young", "Allen"
                ]
    ind = randint(0, last_names.__len__()-1)
    return last_names[ind]
    
def setProf():
    profs = ["Accountant", "Actor/actress", "Architect", "Astronomer", "Baker", "Bricklayer", "Bus driver", "Butcher", "Carpenter",
            "Chef/Cook", "Cleaner", "Dentist","Designer", "Doctor", "Electrician", "Engineer", "Factory worker", "Farmer",
            "Fireman/Fire fighter", "Fisherman", "Florist", "Gardener", "Hairdresser", "Journalist", "Judge", "Lawyer", "Lecturer",
            "Librarian", "Lifeguard", "Mechanic", "Model", "Newsreader", "Nurse", "Optician", "Painter", "Pharmacist", "Photographer",
            "Pilot", "Plumber", "Politician", "Policeman/Policewoman", "Postman", "Real estate agent", "Receptionist", "Scientist",
            "Secretary", "Shop assistant", "Soldier", "Tailor", "Taxi driver", "Teacher", "Translator", "Traffic warden", "Travel agent",
            "Veterinary doctor (Vet)", "Waiter/Waitress", "Businessman", "Dancer", "Artist", "Bartenders"
            ]
    ind = randint(0, profs.__len__()-1)
    return profs[ind]

def birth ():
    d_day = randint(1, 30)
    m_month = randint(1, 12)
    y_year = randint(1940, 2004)
    return f"{m_month}.{d_day}.{y_year}"

class Person():

    def __init__(self):
        self.firstname = get_firstname()
        self.lastname = get_lastname()
        self.birth = birth()
        self.prof = setProf()
    
    
        

    

