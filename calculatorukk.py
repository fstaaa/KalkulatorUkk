from tkinter import *
   

def btnclick(number):
    global val
    val = val + str(number)
    data.set(val)

def btnclear():
    global val
    val = ""
    data.set("")

def btnsamdeng():
    try:
       global val
       result = str(eval(val))
       data.set(result)


    except (ZeroDivisionError):
        val = ""
        data.set("Tidak Dapat Dibagi 0")

    except (SyntaxError, NameError):
        val = ""
        data.set("syntax error")

main = Tk()
main.resizable(0, 0)
main.title("Kalkulator UKK")
main.geometry("280x358")
val = " "
data = StringVar()  

display = Entry(main, bd = 9, textvariable = data, justify = "right", bg = "white", font = ("Palatino Linotype", 19))
display.grid(row = 0, columnspan = 25)

btn1 = Button(main, text = "1", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(1))
btn2 = Button(main, text = "2", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(2))
btn3 = Button(main, text = "3", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(3))
btn4 = Button(main, text = "4", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(4))
btn5 = Button(main, text = "5", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(5))
btn6 = Button(main, text = "6", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(6))
btn7 = Button(main, text = "7", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(7))
btn8 = Button(main, text = "8", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(8))
btn9 = Button(main, text = "9", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(9))
btn0 = Button(main, text = "0", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick(0))

btnplus = Button(main, text = "+", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
                 command = lambda: btnclick('+'))
btnmin = Button(main, text = "-", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
                command = lambda: btnclick('-'))
btnkali = Button(main, text = "*", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
                 command = lambda: btnclick('*'))
btnbagi = Button(main, text = "/", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
                 command = lambda: btnclick('/'))
btnsamdeng = Button(main, text = "=", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 27,
                    command = btnsamdeng)
btnclear = Button(main, text = "C", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
                  command = btnclear)
koma = Button(main, text = ".", font = ("Palatino Linotype", 12, "bold"), height = 2, width = 6,
              command = lambda: btnclick('.'))

btn1.grid(row = 3, column = 0)
btn2.grid(row = 3, column = 1)
btn3.grid(row = 3, column = 2)
btn4.grid(row = 2, column = 0)
btn5.grid(row = 2, column = 1)
btn6.grid(row = 2, column = 2)
btn7.grid(row = 1, column = 0)
btn8.grid(row = 1, column = 1)
btn9.grid(row = 1, column = 2)
btn0.grid(row = 4, column = 1)

btnplus.grid(row = 1, column = 3)
btnmin.grid(row = 2, column = 3)
btnkali.grid(row = 3, column = 3)
btnbagi.grid(row = 4, column = 3)
koma.grid(row = 4, column = 2)
btnclear.grid(row = 4, column = 0)
btnsamdeng.place(x = 0, y = 297)

main.mainloop()