from tkinter import *


jedn = 12

def logowanie():
    root = Tk()
    root.title('Logowanie')

    loginplan = 'planista'
    hasloplan = '123'

    loginkier = 'kierownik'
    haslokier = '123'

    theLabel1 = Label(root, text='Wpisz login i hasło:')
    theLabel1.pack()

    theLabel2 = Label(root, text='login: planista')
    theLabel2.pack()

    login = Entry(root, width=50)
    login.pack()
    login.insert(0, 'Login')

    theLabel3 = Label(root, text='hasło:123')
    theLabel3.pack()

    haslo = Entry(root, width=50)
    haslo.pack()
    haslo.insert(0, 'Haslo')

    def myClick():
        login2 = login.get()
        haslo2 = haslo.get()
        if login2 == loginplan and haslo2 == hasloplan:
            myLabel = Label(root, text='Zalogowano pomyślnie jako planista')
            myLabel.pack()
            root.destroy()
        elif login2 == loginkier and haslo2 == haslokier:
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