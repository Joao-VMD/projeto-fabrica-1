import unittest
from função_01 import calcula_media, situacao_media

class TestMedia(unittest.TestCase):
    def test_calcular_media_basico(self):
        self.assertAlmostEqual(calcula_media(7, 8, 6, 9), 7.5, places=2)

    def test_calcular_media_uma_nota(self):
        self.assertAlmostEqual(calcula_media(10), 10.0, places=2)

    def test_calcular_media_erro_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcula_media([])

    def test_classificar_media_aprovado(self):
        self.assertEqual(situacao_media(7.0), "Aprovado")
        self.assertEqual(situacao_media(9.5), "Aprovado")

    def test_classificar_media_recuperacao(self):
        self.assertEqual(situacao_media(5.0), "Recuperação")
        self.assertEqual(situacao_media(6.9), "Recuperação")

    def test_classificar_media_reprovado(self):
        self.assertEqual(situacao_media(4.99), "Reprovado")

if __name__ == '__main__':
    unittest.main()