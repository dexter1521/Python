class Friend:
    def __init__(self, name, phone, mail, birthday):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.birthday = birthday

    def describe(self):
        print(f'My friend {self.name} has his birthday on {self.birthday} and you can contact him at {self.phone} or {self.mail}')
        
        
amigo = Friend('Juan', '123456789', 'un@correo.com', '01/01/2000')
amigo.describe()


class Agenda:

    def __init__(self):
        self.contacts = {}
    
    def create_contact(self):
        name = input("Ingrese el nombre: ")
        phone = input("Ingrese el teléfono: ")
        email = input("Ingrese el correo: ")
        birthday = input("Ingrese la fecha de nacimiento: ")
        new_contact = Friend(name, phone, email, birthday)
        self.contacts[name] = new_contact
     
    def describe_contacts(self):
        for f in self.contacts.keys():
            self.contacts[f].describe()
            
            
            
agenda = Agenda()
agenda.create_contact()

agenda.describe_contacts()
    