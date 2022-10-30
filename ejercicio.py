# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attact_method(self):
        return self.strength
    
    def receiveDamage_method(self,damage):
        self.damage = damage
        
        self.health = self.health-self.damage
        

class Viking(Soldier):
    def __init__(self,name, health, strength):
        super().__init__(strength,health)
        self.name = name

    def receiveDamage_method(self,damage):
        self.damage = damage
        self.health = self.health-self.damage
        
        if self.health > 0:
            print(self.name," has received",self.damage,"points of damage")
        else:
            print(self.name,"has died in act of combat")
            
    def battleCry_method():
        return "Odin Owns You All!"
    

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(strength,health)
        
    def receiveDamage_method(self,damage):
        self.damage = damage
        self.health = self.health-self.damage
        
        if self.health > 0:
            print("A Saxon has received",self.damage,"points of damage")
        else:
            print("A Saxon has died in act of combat")
            
            
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self):
        