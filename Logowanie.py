from tkinter import *
from LoadData import *

#test gita, bo nie wiem czy git, L.

def logowanie():
    root = Tk()
    root.title('Logowanie')
    root.geometry("800x600")
    root.configure(background='white')

    theLabel1 = Label(root, text='Ultimate planning tool', font=('Arial',24))
    theLabel1.configure(background='white')
    theLabel1.pack()


    theLabel2 = Label(root, text='Login:', font=('Arial',18))
    theLabel2.configure(background='white')
    theLabel2.pack()


    polelogin = Entry(root, width=50)
    polelogin.pack()

    theLabel3 = Label(root, text='Hasło:', font=('Arial',18))
    theLabel3.configure(background='white')
    theLabel3.pack()

    polehaslo = Entry(root, width=50, show='*')
    polehaslo.pack()

    def myClick():
        login2 = polelogin.get()
        haslo2 = polehaslo.get()
        result = sql(login2, haslo2)
        if result == 2:
            myLabel = Label(root, text='Zalogowano pomyślnie jako planista')
            myLabel.pack()
            root.destroy()
            planistam1()
        if result == 4:
            myLabel = Label(root, text='Zalogowano pomyślnie jako kierownik')
            myLabel.pack()
            root.destroy()
            kierownikm1()
        else:
            myLabel = Label(root, text='Zly login lub haslo')
            myLabel.pack()

    def myClick2():
        root.destroy()


    myButton = Button(root, text='Zaloguj się', command=myClick)
    myButton.pack()

    myButton2 = Button(root, text='Wyjdź', command=myClick2)
    myButton2.pack()

    root.mainloop()


def kierownikm1():
    root = Tk()

    root.title('Menu 1 - Kierownik')


def planistam1():
    root = Tk()
    root.title('Menu 1 - Planista')

    def myClick3():
        root.destroy()
        planistam2()

    myButton3 = Button(root, text='Planowanie srednio terminowe', command=myClick3)
    myButton3.pack()


def planistam2():
    root = Tk()
    root.title('Menu planowania srednio terminowego - Planista')

    def myClick4():
        root.destroy()
        planistam3()


    myButton4 = Button(root, text='Capacity loading', command=myClick4)
    myButton4.pack()

def planistam3():
    root = Tk()
    root.title('Capacity loading')



logowanie()