from Perso.Personnage import Personnage
from Perso.Boss import Boss


def main():
    print('Debut du Jeux :')

    Perso = Personnage();
    MonsterBoss = Boss();
    tour(MonsterBoss,Perso)


def tour(MonsterBoss,Perso):
    Win = False;
    PersoWin = ""
    DamageDeal = 0
    while Win == False:
        if (MonsterBoss.CurrentCD == 0):
            print('Perso protect :')
            Perso.Protect()
        else:
            if (Perso.HP <= Perso.MaxHP / 2):
                print('Perso heal :')
                Perso.Heal()
            else:
                print('Perso Attack :')
                DamageDeal = Perso.Attack()
                MonsterBoss.HP = MonsterBoss.HP - DamageDeal


        if (MonsterBoss.BossDead() == True):
            Win = True
            print('Victoire du Personnage :')
            PersoWin = "Personnage"

        if (MonsterBoss.CurrentCD == 1):
            print("une attaque se prepare")
        if (MonsterBoss.CurrentCD == 0):
            print('MonsterBoss SpéATK :')
            if(Perso.used ==True):
                print("Protection efficace")
            else:
                DamageDeal = MonsterBoss.speAttack()
                MonsterBoss.CurrentCD = MonsterBoss.SpeCD
                Perso.HP = Perso.HP- DamageDeal

        else:
            print('MonsterBoss ATK :')
            DamageDeal = MonsterBoss.Attack()
            Perso.HP = Perso.HP- DamageDeal
        if (Perso.HP <= 0):
            Win = True
            print('Victoire du MonsterBoss :')

            PersoWin = "MonsterBoss"
        MonsterBoss.CurrentCD  =  MonsterBoss.CurrentCD -1
        if(MonsterBoss.HP  <=50):
            MonsterBoss.HP  =  MonsterBoss.HP + 1
        print(MonsterBoss.HP)
        print(Perso.HP)

main()
