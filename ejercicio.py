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
        

