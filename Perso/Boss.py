class Boss:



    def __init__(self):
        self.attack = 4
        self.armor = 10
        self.HP = 105
        self.MaxHP = 120
        self.SpeCD = 4
        self.CurrentCD = 0
        self.used = False

    def speAttack(self):
        return 15

    def Attack(self):
        return self.attack
    def BossDead(self):
        if(self.HP <= 0):
            self.HP = 0
            return True
        else:
            return False
