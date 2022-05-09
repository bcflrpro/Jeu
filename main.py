from Perso.Personnage import Personnage


def main():
    print('Choix Personnage :')
    PersoList = choix()
    tour(PersoList)
    return ;

def choix():
    value = input(" Personnage 1 (Mage =1 Guerrier =2 Healeur =3)")
    if value == 1 :
        Personnage1  = Personnage()
        Personnage1  = Personnage.Mage()
    if value == 2:
        Personnage1  = Personnage()
        Personnage1  = Personnage.Guerrier()
    if value == 3:
        Personnage1  = Personnage()
        Personnage1  = Personnage.Healeur()
    value = input(" Personnage 2 (Mage =1 Guerrier =2 Healeur =3)")
    if value == 1 :
        Personnage2  = Personnage()
        Personnage2  = Personnage.Mage()
    if value == 2:
        Personnage2  = Personnage()
        Personnage2  = Personnage.Guerrier()
    if value == 3:
        Personnage2  = Personnage()
        Personnage2  = Personnage.Healeur()
    Perso = []
    Perso.append(Personnage1)
    Perso.append(Personnage2)
    
def tour(PersoList):
     Perso1 = PersoList[0]
     Perso2 = PersoList[1]
     Win=False;
     PersoWin =""
     while Win == False:
         return;

