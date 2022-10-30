# Soldier
from random import choice


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
            
            
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self,viking):
        self.vikingArmy.append(viking)
        return None
    
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
        return None
    
    def vikingAttack(self):
        saxon = choice(self.saxonArmy)
        viking = choice(self.vikingArmy)
        ataque = saxon.receiveDamage_method(viking.strength)
        if saxon.health <=0:
            self.saxonArmy.remove(saxon)
        else:
            pass
        return ataque
    
    def saxonAttack(self):
        saxon = choice(self.saxonArmy)
        viking = choice(self.vikingArmy)
        ataque = viking.receiveDamage_method(saxon.strength)
        if viking.health <=0:
            self.vikingArmy.remove(viking)
        else:
            pass
        return ataque
    
    def showStatus(self):
        if self.saxonArmy == []:
            return "Viking have won the war of the century"
        elif self.vikingArmy == []:
            return "Saxon have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle"