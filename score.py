class f_managing:

    def __init__ (self):
        try:
            self.f = open ("puntaje.txt", "x")
        except:
            self.f = open ('puntaje.txt', 'r')


    def nuevo (self, puntaje):
        try:
            pun = int(self.f.read())
        except:
            pun = 100
        
        if puntaje < pun:
            self.f.close()
            f = open('puntaje.txt', 'w')
            f.write(str(puntaje))

    def leer (self):
        self.f.close()
        f = open('puntaje.txt', 'r')
        return f.read()

