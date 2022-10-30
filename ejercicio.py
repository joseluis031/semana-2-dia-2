# Soldier
from random import choice


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.damage = damage
        
        self.health = self.health-self.damage
        if self.health < 0:
            self.health = 0
        else:
            pass

class Viking(Soldier):
    def __init__(self,name, health, strength):
        self.name = name
        super().__init__(health,strength)


    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health-self.damage
        
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)
            
    def battleCry(self):
        return "Odin Owns You All!"
    

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
        
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health-self.damage
        
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"
            
            
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
        ataque = saxon.receiveDamage(viking.strength)
        if saxon.health <=0:
            self.saxonArmy.remove(saxon)
        else:
            pass
        return ataque
    
    def saxonAttack(self):
        saxon = choice(self.saxonArmy)
        viking = choice(self.vikingArmy)
        ataque = viking.receiveDamage(saxon.strength)
        if viking.health <=0:
            self.vikingArmy.remove(viking)
        else:
            pass
        return ataque
    
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."