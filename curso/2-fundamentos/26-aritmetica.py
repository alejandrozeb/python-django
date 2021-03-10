""" Objetos con metodos """
class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        """ se realiza la opracion con los atributos de la clase, forma parte de la documetnacion de la clase """
        return self.operando1 + self.operando2
    
    def resta(self):
        return self.operando1 - self.operando2
    
#creamos un nuevo objeto
aritmetica = Aritmetica(2,4)

print("Resultado suma: ", aritmetica.sumar())
print("Resultado resta ", aritmetica.resta())