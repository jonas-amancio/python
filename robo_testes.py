import unittest

from robo import Robo


class RoboTest(unittest.TestCase):

    def setUp(self) -> None:
        #roda antes dos testes
        self.megaman = Robo('mega man', bateria=50)

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100, "Bateria não está carregando")

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'Meu nome é Mega Man', 'Erro ao retornar o nome.')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49%')

    def tearDown(self) -> None:
        #roda depois dos testes
        print(f'Só testando o tearDown, mais usando pra fechar conexão de banco ou arquivo.')
    

if __name__ == '__main__':
    unittest.main()