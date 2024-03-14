class Duck:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sound(self):
        return 'Quack Quack'
    

pato = Duck('Donald', 'White')
pato.sound()