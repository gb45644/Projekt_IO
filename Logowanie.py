from tkinter import *


def logowanie():
    root = Tk()
    root.title('Logowanie')

    theLabel1 = Label(root, text='Wpisz login i hasło:')
    theLabel1.pack()

    theLabel2 = Label(root, text='login: planista')
    theLabel2.pack()

    polelogin = Entry(root, width=50)
    polelogin.pack()
    polelogin.insert(0, 'Login')

    theLabel3 = Label(root, text='hasło:123')
    theLabel3.pack()

    polehaslo = Entry(root, width=50)
    polehaslo.pack()
    polehaslo.insert(0, 'Haslo')

    def myClick():
        login2 = polelogin.get()
        haslo2 = polehaslo.get()
        if login2 == 'planista' and haslo2 == '123':
            myLabel = Label(root, text='Zalogowano pomyślnie jako planista')
            myLabel.pack()
            root.destroy()
        elif login2 == 'kierownik' and haslo2 == '321':
            myLabel = Label(root, text='Zalogowano pomyślnie jako kierownik')
            myLabel.pack()
            root.destroy()
            kierownikm1()
        else:
            myLabel = Label(root, text='Zly login lub haslo')
            myLabel.pack()

    myButton = Button(root, text='Zaloguj się', command=myClick)
    myButton.pack()

    root.mainloop()


def kierownikm1():
    root = Tk()
    root.title('Menu 1 - Kierownik')


logowanie()