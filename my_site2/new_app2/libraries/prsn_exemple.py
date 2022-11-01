from .PersonRnd import Person

def get_person():
    prs1 = Person()
    asset = {
        'name':prs1.firstname,
        'lastname':prs1.lastname,
        'Date_of_Birth':prs1.birth,
        'Profession':prs1.prof
        }
    return asset
    #asset = {f"name: {prs1.firstname}\nlastname: {prs1.lastname}\nDate of Birth:{prs1.birth}\nProfession: {prs1.prof}"}

