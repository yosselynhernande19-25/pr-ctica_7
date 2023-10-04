class Divisor:
    def dividir(self, numerador, denominador):
        try:
            resultado = numerador / denominador
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero."

divisor = Divisor()

numerador = 20
denominador = 0

resultado = divisor.dividir(numerador, denominador)
print(resultado)
