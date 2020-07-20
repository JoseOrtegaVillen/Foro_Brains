
class Respuestas:

    def __init__(self):
        self.respuesta_true_a = True
        self.respuesta_false_b = False
        self.respuesta_false_c = False
        self.respuesta_false_d = False
    
    def valorRespuesta(self, respuesta_true_a, respuesta_false_b, respuesta_false_c, respuesta_false_d):
        respuesta_true_a = 'Hola'
        respuesta_false_b = 'Buenos Dias'
        respuesta_false_c = 'Nono'
        respuesta_false_d = "Sii"

    def puntosVariable(self, y, f, t):
        y = 0
        f = 0
        t = + 1

    def resultadoSuma(self, resultadoTrue, resultadoFalse, y, f ,t):
        resultadoTrue = y + t
        resultadoFalse = y + f

        return resultadoTrue

    def contadorFragmentos(self, contador, data):
        self.resultadoTrue = data
        contador = data + self.resultadoTrue

        return contador

    def sumarFragmentos(self, data, sumaFragmentos):
        sumaFragmentos = data + self.resultadoTrue

        return sumaFragmentos
        
