import unittest

from funcoes import comer, dormir

class FuncoesTestes(unittest.TestCase):
    
    def test_comer_saudavel(self):
        self.assertEqual(
            comer('Quiabo', True),
            'Quiabo é saudável.'
        )

    def test_comer_nao_saudavel(self):
        self.assertEqual(
            comer(comida='Pizza', saudavel=False),
            'Pizza não é saudável.'
        )
    
    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Dormiu pouco.'
        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(8),
            'Dormiu por tempo suficiente.'
        )


if __name__ == '__main__':
    unittest.main()