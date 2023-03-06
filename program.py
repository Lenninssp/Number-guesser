from random import randint
import score

file =score.f_managing()

class juego:
    def __init__ (self):
        self.puntaje = 1
        pass 


    def what_number (self):
        self.numero = randint (0, 100)
        print("la maquina ya pensó en un numero entre uno a 100")

    def mayorMenor (self):
        while (True):
            adiv = int(input())

            if adiv != '':

                if adiv > self.numero:
                    print("Tu numero es mayor al de la maquina")
                    self.puntaje += 1

                elif adiv < self.numero:
                    print("Tu numero es menor al de la maquina")
                    self.puntaje += 1

                else:
                    print ("adivinaste")
                    file.nuevo(self.puntaje)
                    print ("Tu puntaje", self.puntaje, "\n", "Puntaje mas alto: ", file.leer())
                    break

            else:
                print("Ingresa un numero valido")



