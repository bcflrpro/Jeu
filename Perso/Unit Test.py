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




if __name__ == '__main__':
    unittest.main()
