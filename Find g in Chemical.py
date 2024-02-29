configs={
    'Title':'NameProgram',#ชื่อโปรแกรม
    'MainTitle':'MainTab',#หัวเรื่องโปรแกรม
    'TkinterBg':'#EFABF7',
    'MianColor':'#FF7E7E',
    'Button':'#779AFF',
    'OutputColor':'#91FF79'
}

#g/mw = CV/1000
from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        master.title(configs['Title'])
        master.configure(bg=configs['TkinterBg'])

        self.Labelbox = LabelFrame(master, bg=configs['MianColor'])
        self.Labelbox.pack()

        self.Label = Label(self.Labelbox, text=configs['MainTitle'], font=('Helvetica', 16), bg=configs['MianColor'])
        self.Label.pack()

        self.Frame = Frame(master, bg=configs['TkinterBg'])
        self.Frame.pack()

        self.Label2 = Label(self.Frame, text='Mw : ', font=('Helvetica', 16), bg=configs['Button'])
        self.Label2.pack(side=LEFT)

        self.Entry = Entry(self.Frame, textvariable=IntVar(), font=('Helvetica', 16))
        self.Entry.pack(side=LEFT)

        self.Frame2 = Frame(master, bg=configs['TkinterBg'])
        self.Frame2.pack()

        self.Label3 = Label(self.Frame2, text='C    : ', font=('Helvetica', 16), bg=configs['Button'])
        self.Label3.pack(side=LEFT)

        self.Entry2 = Entry(self.Frame2, textvariable=IntVar(), font=('Helvetica', 16))
        self.Entry2.pack(side=LEFT)

        self.Frame3 = Frame(master, bg=configs['TkinterBg'])
        self.Frame3.pack()

        self.Label4 = Label(self.Frame3, text='V    : ', font=('Helvetica', 16), bg=configs['Button'])
        self.Label4.pack(side=LEFT)

        self.Entry3 = Entry(self.Frame3, textvariable=IntVar(), font=('Helvetica', 16))
        self.Entry3.pack(side=LEFT)

        self.Frame4 = Frame(master, bg=configs['TkinterBg'])
        self.Frame4.pack()

        self.Button = Button(self.Frame4, text='Convect', font=('Helvetica', 16), command=self.Convect, bg=configs['Button'])
        self.Button.pack(side=LEFT)

        self.Labelbox2 = LabelFrame(self.Frame4, bg=configs['TkinterBg'])
        self.Labelbox2.pack(side=LEFT)
        
        self.Label5 = Label(self.Labelbox2, text='', font=('Helvetica', 16), bg=configs['OutputColor'])
        self.Label5.pack()

    def Convect(self):
        a=(float(self.Entry2.get())*float(self.Entry3.get())/1000)*float(self.Entry.get())
        self.Label5.config(text=f'g = {a}g')
            


def main():
    root=Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()