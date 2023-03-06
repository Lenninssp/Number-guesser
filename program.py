from random import randint

class juego:
    def __init__ (self):
        pass 


    def what_number (self):
        self.numero = randint (0, 100)
        print("la maquina ya pensó en un numero entre uno a 100")

    def mayorMenor (self):
        while (True):
            adiv = int(input())

            if adiv > self.numero:
                print("Tu numero es mayor al de la maquina")

            elif adiv < self.numero:
                print("Tu numero es menor")

            else:
                print ("adivinaste")
                break



