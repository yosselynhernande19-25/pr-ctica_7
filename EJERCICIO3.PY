#EJERCICIO #3
class ValidadorContraseña:
    def __init__(self, longitud_minima):
        self.longitud_minima = longitud_minima

    def validar(self, contraseña):
        try:
            if len(contraseña) < self.longitud_minima:
                raise ValueError("La contraseña es demasiado corta. Debe tener al menos {} caracteres.".format(self.longitud_minima))
            else:
                print("La contraseña es válida.")
        except ValueError as error:
            print(error)


longitud_minima = 8
validador = ValidadorContraseña(longitud_minima)

contraseña = "Yosselyn.H"
validador.validar(contraseña)  

contraseña = "HernándezOrellana"
validador.validar(contraseña)  
