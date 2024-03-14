import numpy as np

class Ninja:

    def __init__(self, name, initial_life, strength):
       self.name = name
       self.initial = initial_life
       self.strength = strength
       self.alive = True

    def receive_damage(self, damage):
        self.life = self.initial - damage
        print(f"{self.name} ha recibido {damage} de daño.")
        if self.life <= 0:
            self.alive = False
            print(f"{self.name} ha muerto.")
        else:
            print(f"{self.name} ha recibido {damage} de daño y le quedan {self.life} de vida.")        

    def attack(self):
        a = np.random.normal(self.strength, self.strength/4)
        print(f"{self.name} ataca con {a} de fuerza.")
        return a

""" naruto = Ninja("Naruto", 200, 8)
naruto.receive_damage(70)
naruto.attack() """

class Simulation:

    def __init__(self, ninja1, ninja2):
        self.ninja1 = ninja1
        self.ninja2 = ninja2
        
        self.fight()
        
    def fight(self):
        while self.ninja1.alive and self.ninja2.alive:
            self.ninja2.receive_damage(self.ninja1.attack())
            self.ninja1.receive_damage(self.ninja2.attack())
            
        if self.ninja1.alive:
            print(f"{self.ninja1.name} ha ganado.") 
        elif self.ninja2.alive:
            print(f"{self.ninja2.name} ha ganado.")
            
            
sakura = Ninja("Sakura", 70, 2.5)
sasuke = Ninja("Sasuke", 15, 5)
naruto = Ninja("Naruto", 20, 8)


app = Simulation(sakura, sasuke)           