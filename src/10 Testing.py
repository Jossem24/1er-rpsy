import unittest

def dobro(x):
    return x * 2

class multiplicacion(unittest.TestCase):
    def test_plicacion(self):
        self.assertEqual(dobro(3), 6)


if __name__ == "__main__":
    unittest.main()


def soma (a, b):
    return a + b


class novasoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 5), 7)

if __name__ == "__main__":
    unittest.main()


def maior_idade (idade):
    return idade >= 18 

class idade(unittest.TestCase):
    def test_idade(self):
        self.assertEqual(maior_idade(20), True)

if __name__ == "__main__":
    unittest.main()

