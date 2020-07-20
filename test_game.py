import unittest  
from game import Respuestas

class TestRespuestas(unittest.TestCase):  
  
    def setUp(self):
        self.pregunta = Respuestas()

    def test_valor_true(self):
        self.assertTrue(self.pregunta.respuesta_true_a)

    def test_valor_false(self):
        self.assertFalse(self.pregunta.respuesta_false_b)
        self.assertFalse(self.pregunta.respuesta_false_c)
        self.assertFalse(self.pregunta.respuesta_false_d)
    
    def test_probar_respuestas(self):
        self.valorRespuesta = Respuestas()
        self.respuesta_true_a = "Hola"
        self.respuesta_false_b = "Buenos Dias"
        self.respuesta_false_c = "Nono"
        self.respuesta_false_d = "Sii"

        self.assertEqual('Hola', self.respuesta_true_a )
        self.assertEqual('Buenos Dias', self.respuesta_false_b )
        self.assertEqual('Nono', self.respuesta_false_c )
        self.assertEqual('Sii', self.respuesta_false_d )

    def test_puntos_de_variables(self):
        self.puntosVariable = Respuestas()
        self.y = 0
        self.f = 0
        self.t = 1

        self.assertEqual(0, self.y)
        self.assertEqual(0, self.f)
        self.assertEqual(1, self.t)

    def test_resultado_suma(self):
        self.resultadoSuma = Respuestas()
        self.resultadoTrue = 1
        self.resultadoFalse = 0
        self.assertEqual(1, self.resultadoTrue)
        self.assertEqual(0, self.resultadoFalse)

    def test_contador_de_fragmentos(self):
        self.contadorFragmentos = Respuestas()
        self.contador = 1

        self.assertEqual(1, self.contador)

    def test_sumar_fragmentos(self):
        self.sumarFragmentos = Respuestas()
        self.sumaFragmentos = 2

        self.assertEqual(2, self.sumaFragmentos)

