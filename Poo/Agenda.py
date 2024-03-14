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