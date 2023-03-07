
import customtkinter
from random import randint
import score

file =score.f_managing()

class App(customtkinter.CTk):
    def __init__(self):

        super().__init__()

        self.puntaje=1
        self.numero = randint (0, 100)
        print("la maquina ya pensó en un numero entre uno a 100")
        
        self.geometry("300x200")
        self.title("Number guesser")
        self.minsize(300,300)
        self.maxsize(300,300)

        self.grid_rowconfigure(4,weight=1)
        self.grid_columnconfigure((0,3), weight=1)

        self.text= customtkinter.CTkTextbox(master=self,font=("American Typewriter",25),width=80, height=20)
        self.text.grid(row=2, column=2, columnspan=1, padx=10, pady=10, sticky="ew")

        self.button = customtkinter.CTkButton(master=self, text="Text", command=self.test)
        self.button.grid(row=3, column=2, padx=20, sticky="ew")
        
    def test(self):

        self.intento=int(self.text.get("0.0","end"))

        if self.intento != '':

                if self.intento > self.numero:
                    self.frame("Tu numero es mayor al de la maquina")
                    self.puntaje += 1

                elif self.intento < self.numero:
                    self.frame("Tu numero es menor al de la maquina")
                    self.puntaje += 1

                else:
                    textov = "adivinaste \n Tu puntaje", self.puntaje, "\n", "Puntaje mas alto: ", file.leer()
                    
                    self.frame (textov)
                    file.nuevo(self.puntaje)
                    
    
    def frame (self, texto):
         self.label = customtkinter.CTkLabel(master=self, text=texto)
         self.label.grid(row=4, column=2, padx=10, sticky="ew")
                    

        