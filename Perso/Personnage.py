class Personnage:

    def init(this):
        this.attack = 0;
        this.armor = 0;
        this.SpeAttack = "Tank 50% "
        this.SpéCD = 0;
        this.CurrentCD = 0;
        this.used = False;
        return;
    def guerrier(this):
        this.attack =5;
        this.armor = 4;
        this.SpeAttack ="Tank 50% "
        this.SpéCD =2;
        this.CurrentCD =2;
        this.used=False;

    def mage(this):
        this.attack = 5;
        this.armor = 2;
        this.SpeAttack ="retire 50% hp manquant"
        this.SpéCD =2;
        this.CurrentCD =2;

        this.used=False;
    
    def healeur(this):
        this.armor = 1;
        this.attack = 2;
        this.SpéCD =2;

        this.CurrentCD =2;
        this.used=False;
        this.SpeAttack ="heal 15hp"
