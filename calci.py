from tkinter import *

def btnClick(nos):
    global operator
    operator = operator + str(nos)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

calci = Tk()
calci.title("Calculator")
calci.configure(background = 'black')

operator = ""
text_input = StringVar()

textdisp = Entry(calci, font = ('times', 20, 'bold'), textvariable = text_input, bd = 30, insertwidth = 4, bg = 'silver', justify = 'right').grid(columnspan = 4)

btn7 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '7', command = lambda:btnClick(7)).grid(row = 1, column = 0)
btn8 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '8', command = lambda:btnClick(8)).grid(row = 1, column = 1)
btn9 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '9', command = lambda:btnClick(9)).grid(row = 1, column = 2)
btnadd = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '+', command = lambda:btnClick('+')).grid(row = 1, column = 3)

btn4 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '4', command = lambda:btnClick(4)).grid(row = 2, column = 0)
btn5 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '5', command = lambda:btnClick(5)).grid(row = 2, column = 1)
btn6 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '6', command = lambda:btnClick(6)).grid(row = 2, column = 2)
btnsub = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '-', command = lambda:btnClick('-')).grid(row = 2, column = 3)

btn1 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '1', command = lambda:btnClick(1)).grid(row = 3, column = 0)
btn2 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '2', command = lambda:btnClick(2)).grid(row = 3, column = 1)
btn3 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '3', command = lambda:btnClick(3)).grid(row = 3, column = 2)
btnmul = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '*', command = lambda:btnClick('*')).grid(row = 3, column = 3)

btn0 = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '0', command = lambda:btnClick(0)).grid(row = 4, column = 0)
btnclear = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = 'C', command = btnClearDisplay).grid(row = 4, column = 1)
btnequal = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '=', command = btnEquals).grid(row = 4, column = 2)
btndiv = Button(calci, padx = 16, pady = 16, bd = 8, fg = 'black', bg = 'silver', font = ('times', 20, 'bold'), text = '/', command = lambda:btnClick('/')).grid(row = 4, column = 3)

calci.mainloop()
