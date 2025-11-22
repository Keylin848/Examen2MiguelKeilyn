import unittest
from Examen2 import MiClase


class TestMiClase(unittest.TestCase):
    
    def setUp(self):
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    # Pruebas para ObtieneValencia
    def test_obtiene_valencia_con_varios_impares(self):
        resultado = self.objeto.ObtieneValencia(1234567)
        #self.assertEqual(resultado, 4)  # 1, 3, 5, 7 son impares
        self.assertEqual(resultado, 5) # < -- Fallo intencional
    
    def test_obtiene_valencia_solo_pares(self):
        resultado = self.objeto.ObtieneValencia(2468)
        self.assertEqual(resultado, 0)  # No hay dígitos impares
    
    # Pruebas para DivisibleTempo
    def test_divisible_tempo_numero_con_varios_divisores(self):
        resultado = self.objeto.DivisibleTempo(10)
        self.assertEqual(resultado, [1, 2, 5, 10])
    
    def test_divisible_tempo_numero_primo(self):
        resultado = self.objeto.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7])
    
    # Pruebas para ObtieneMasBailable
    def test_obtiene_mas_bailable_lista_normal(self):
        resultado = self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7])
        self.assertEqual(resultado, 0.9)
    
    def test_obtiene_mas_bailable_lista_vacia(self):
        """Prueba con lista vacía"""
        resultado = self.objeto.ObtieneMasBailable([])
        self.assertIsNone(resultado)
    
    # Pruebas para VerificaListaCanciones
    def test_verifica_lista_canciones_todas_validas(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"])
        self.assertTrue(resultado)
    
    def test_verifica_lista_canciones_con_none(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", None, "Canción 3"])
        self.assertFalse(resultado)
        
    # Prueba para Encuentra
    def test_encuentra_elemento_existente(self):
        """Prueba cuando el elemento SÍ existe en la lista"""
        lista = [1, 2, 3, 4, 5]
        resultado = self.objeto.Encuentra(lista, 3)
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()
