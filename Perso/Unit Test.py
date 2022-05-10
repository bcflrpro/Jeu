import unittest
import Personnage
from Perso.Boss import Boss


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_Init_Perso(self):
        Perso = Personnage()
        self.assertIsInstance(Perso)

    def test_Init_Boss(self):
        MonsterBoss = Boss()
        self.assertIsInstance(MonsterBoss)

    def test_Attack_Boss(self):
        MonsterBoss = Boss()
        DamageDeal= MonsterBoss.Attack()
        self.assertEqual(DamageDeal== MonsterBoss.attack)
    def test_Attack_Perso(self):
        Perso = Personnage()
        DamageDeal = Perso.Attack()
        self.assertEqual(DamageDeal== Perso.attack)

    def test_SpeATK_Boss(self):
        MonsterBoss = Boss()
        DamageDeal = MonsterBoss.speAttack()

        self.assertEqual(DamageDeal== 15 )

    def test_Protect_Perso(self):
        Perso = Personnage()

        IsUsed = Perso.Protect()
        if(IsUsed == True):
            self.assertEqual(IsUsed==False)
        if(IsUsed== False):
            self.assertEqual(IsUsed==False)

    def test_Attack_Boss(self):
        MonsterBoss = Boss()
        Boss.HP = 0
        self.assertTrue(Boss.BossDead())






if __name__ == '__main__':
    unittest.main()
