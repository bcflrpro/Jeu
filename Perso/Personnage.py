import random

class Personnage:



    def __init__(self):
        self.attack =10;
        self.HP =50;
        self.MaxHP =50;

        self.armor = 4;
        self.SpéCD =2;
        self.CurrentCD =0;
        self.used=False;



    def Attack(self):
        return self.attack;

    def Heal(self):
        RNG = random.randint(0, 2)
        if (RNG == 0):
          self.HP =  self.HP + self.MaxHP/2;

    def Protect(self):
        RNG = random.randint(0,2)
        if(RNG == 0):
            self.used =True;