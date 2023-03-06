class f_managing:

    def __init__ (self):
        try:
            self.f = open ("NumberGuesser_p1/puntaje.txt", "x")
        except:
            self.f = open ('NumberGuesser_p1/puntaje.txt', 'r')


    def nuevo (self, puntaje):
        try:
            pun = int(self.f.read())
        except:
            pun = 100
        
        if puntaje < pun:
            f = open('NumberGuesser_p1/puntaje.txt', 'w')
            f.write(str(puntaje))

    def leer (self):
        f = open('NumberGuesser_p1/puntaje.txt', 'r')
        return f.read()

