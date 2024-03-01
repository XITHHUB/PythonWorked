#Config Your Program
configs = {
    1:'โปรแกรมหาค่าครึ่งชีวิต',
    2:'ค่าครึ่งชีวิต'
}

#
from tkinter import * 
from math import *

class App:
    def __init__(self, master):
        self.master = master
        master.title(configs[1])
        
        self.textbox = LabelFrame(master)
        self.textbox.pack()

        self.Label = Label(self.textbox, text=configs[2], font=('Helvetica', 16))
        self.Label.pack()

        self.Frame = Frame(master)
        self.Frame.pack()

        self.Label2 = Label(self.Frame, text='    N start    : ', font=('Helvetica', 16))
        self.Label2.pack(side=LEFT)

        self.Entry = Entry(self.Frame, textvariable=IntVar(), font=('Helvetica', 16))
        self.Entry.pack(side=LEFT)



        self.Frame2 = Frame(master)
        self.Frame2.pack()

        self.Label3 = Label(self.Frame2, text='    N Left     : ', font=('Helvetica', 16))
        self.Label3.pack(side=LEFT)

        self.Entry2 = Entry(self.Frame2, textvariable=IntVar(), font=('Helvetica', 16))
        self.Entry2.pack(side=LEFT)

        self.Frame4 = Frame(master)
        self.Frame4.pack()

        self.Label6 = Label(self.Frame4, text='Time(days) : ', font=('Helvetica', 16))
        self.Label6.pack(side=LEFT)

        self.Entry3 = Entry(self.Frame4, textvariable=IntVar(), font=('Helvetica', 16))
        self.Entry3.pack(side=LEFT)

        self.Frame3 = Frame(master)
        self.Frame3.pack()

        self.button = Button(self.Frame3, text='Convect', font=('Helvetica', 16), command=self.Convect)
        self.button.pack(side=LEFT)

        self.Label4 = Label(self.Frame3, text='ครั้งที่เกิดขึ้น : ', font=('Helvetica', 16))
        self.Label4.pack(side=LEFT)
        
        self.textbox2 = LabelFrame(self.Frame3)
        self.textbox2.pack(side=LEFT)

        self.Label5 = Label(self.textbox2, font=('Helvetica', 16))
        self.Label5.pack()

        self.Label8 = Label(self.Frame3, font=('Helvetica', 16), text=' เกิดครั้งละ : ')
        self.Label8.pack(side=LEFT)

        self.textbox3 = LabelFrame(self.Frame3)
        self.textbox3.pack(side=LEFT)
        
        self.Label7 = Label(self.textbox3, font=('Helvetica', 16))
        self.Label7.pack()
    
    def Convect(self):
        N1 = float(self.Entry.get())
        N2 = float(self.Entry2.get())
        T = float(self.Entry3.get()) 
        Ntotal = 0
        while True:
            if N1!=N2:
                if N1<N2:
                    Ntotal -=1
                    break
                else:
                    N1 = N1/2
                    Ntotal +=1
            else:
                break
        self.Label5.config(text=f'{Ntotal} ครั้ง')
        self.Label7.config(text=f'{(int(T/Ntotal))} วัน')



def main():
    root=Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()