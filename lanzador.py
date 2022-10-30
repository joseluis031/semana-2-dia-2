from ejercicio import (Saxon,Viking,War)


def lanz():
    Flecha = Saxon(100,99)
    Alexa = Viking("Alexa",100,200)
    
    lucha = War()
    
    lucha.addSaxon(Flecha)
    lucha.addViking(Alexa)
    print(lucha.saxonAttack())
    print(lucha.vikingAttack())
    print(lucha.showStatus())