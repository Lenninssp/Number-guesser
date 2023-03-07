import program
import UI

if __name__ == "__main__":
    print("Funcionando")

    var = input("1 para UI, 2 para terminal, 0 para salir\n")

    if var == "1":
        app = UI.App()
        app.mainloop()

    elif var == "2":
        p = program.juego()
        p.what_number()
        p.mayorMenor()

    else:
        pass

