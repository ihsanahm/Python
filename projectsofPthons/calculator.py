from tkinter import Tk, Entry, Button, StringVar


class Calculator:

    def __init__(self,master):

        master.title(" Calculator ")
        master.geometry('350x410+0+0')
        master.config(bg = '#c5d2e6' )
        master.resizable(False , False)

        self.equation=StringVar()
        self.entery_value=' '

        Entry(width=17,bg='white',font=('Arial Bold', 28),textvariable=self.equation).place(x=0,y=0)

        Button(width=11, height=4, text='(', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', compound='center', relief='flat', bg='#7588ff', command=lambda:self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', compound='center', relief='flat', bg='#faaf23', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='/', compound='center', relief='flat', bg='#faaf23', command=lambda: self.show('/')).place(x=270, y=50)

        Button(width=11, height=4, text='7', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(7)).place(x=0, y=125)
        Button(width=11, height=4, text='8', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(8)).place(x=90, y=125)
        Button(width=11, height=4, text='9', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(9)).place(x=180, y=125)
        Button(width=11, height=4, text='*', compound='center', relief='flat', bg='#faaf23', command=lambda: self.show('*')).place(x=270, y=125)

        Button(width=11, height=4, text='4', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='-', compound='center', relief='flat', bg='#faaf23', command=lambda: self.show('-')).place(x=270, y=200)

        Button(width=11, height=4, text='1', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(1)).place(x=0, y=275)
        Button(width=11, height=4, text='2', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(2)).place(x=90, y=275)
        Button(width=11, height=4, text='3', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(3)).place(x=180, y=275)
        Button(width=11, height=4, text='+', compound='center', relief='flat', bg='#faaf23', command=lambda: self.show('+')).place(x=270, y=275)

        Button(width=11, height=4, text='C', compound='center', relief='flat', bg='#f23847', command=self.clear).place(x=0, y=350)
        Button(width=11, height=4, text='0', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', compound='center', relief='flat', bg='#7588ff', command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='=', compound='center', relief='flat', bg='#13e841', command=self.solve).place(x=270, y=350)
        
        

    def show(self,value):

        self.entery_value+=str(value)
        self.equation.set(self.entery_value)

    def clear(self):

        self.entery_value=' '
        self.equation.set(self.entery_value)

    def solve(self):

        result=eval(self.entery_value)
        self.equation.set(result)


root=Tk()

Calculator=Calculator(root)

root.mainloop()

