import unittest 
import calculadora

class Teste(unittest.TestCase):
    def test_soma(self):
        calculador = calculadora.Calculadora()
        result = calculador.calcular(2, 4, 'soma')
        self.assertEqual(result, 6)

    def test_multiplicacao(self):
        calculador = calculadora.Calculadora()
        result = calculador.calcular(2, 4, 'multiplicacao')
        self.assertEqual(result, 8)

    def test_Divisao(self):
        calculador = calculadora.Calculadora()
        result = calculador.calcular(2, 4, 'divisao')
        self.assertEqual(result, 0.5)

    def test_subtracao(self):
        calculador = calculadora.Calculadora()
        result = calculador.calcular(2, 4, 'subtracao')
        self.assertEqual(result, -2)


if __name__ == '__main__':
    unittest.main()