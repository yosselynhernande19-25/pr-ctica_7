class ValidadorDeEdad:
    def validar(self, edad):
        try:
            edad_entero = int(edad)
            if edad_entero >= 0:
                return f"Edad valida: {edad_entero}"
            else:
                return "Error: La edad no puede ser un numero negativo."
        except ValueError:
            return "Error: La edad ingresada no es un numero entero valido."


validador = ValidadorDeEdad()

entrada = input("Ingresa una edad: ")
resultado = validador.validar(entrada)
print(resultado)
