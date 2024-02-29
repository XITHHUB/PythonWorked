from tkinter import *
from tkinter import messagebox
from math import *
from decimal import *

class App:
    def __init__(self, master):
        self.master = master
        master.title("Packing Efficiency Program")

        self.Labelbox = LabelFrame(master)
        self.Labelbox.pack()

        self.Label = Label(self.Labelbox, text='Packing Efficiency', font=('Helvetica', 16))
        self.Label.pack()
        
        self.Frame = Frame(master)
        self.Frame.pack()

        self.Label2 = Label(self.Frame, text='d : ', font=('Helvetica', 16))
        self.Label2.pack(side=LEFT)

        self.Entry = Entry(self.Frame, textvariable=IntVar())
        self.Entry.pack(side=LEFT)

        self.Frame2 = Frame(master)
        self.Frame2.pack()

        self.Label3 = Label(self.Frame2, text='Mw : ', font=('Helvetica', 16))
        self.Label3.pack(side=LEFT)

        self.Entry2 = Entry(self.Frame2, textvariable=IntVar())
        self.Entry2.pack(side=LEFT)

        self.Frame3 = Frame(master)
        self.Frame3.pack()

        self.Button = Button(self.Frame3, text='SCC', font=('Helvetica', 16), bg='White', command=self.on_event)
        self.Button.pack(side=LEFT)

        self.Button2 = Button(self.Frame3, text='BCC', font=('Helvetica', 16), bg='White', command=self.on_event2)
        self.Button2.pack(side=LEFT)

        self.Button3 = Button(self.Frame3, text='FCC', font=('Helvetica', 16), bg='White', command=self.on_event3)
        self.Button3.pack(side=LEFT)

        self.Frame4 = Frame(master)
        self.Frame4.pack()

        self.Label4 = Label(self.Frame4, text='g : ', font=('Helvetica', 16))
        self.Label4.pack(side=LEFT)

        self.Labelbox2 = LabelFrame(self.Frame4)
        self.Labelbox2.pack(side=LEFT)

        self.Label5 = Label(self.Labelbox2, font=('Helvetica', 16), text='0')
        self.Label5.pack()

        self.Frame5 = Frame(master)
        self.Frame5.pack()
        
        self.Label6 = Label(self.Frame5, text='v : ', font=('Helvetica', 16))
        self.Label6.pack(side=LEFT)

        self.Labelbox3 = LabelFrame(self.Frame5)
        self.Labelbox3.pack(side=LEFT)

        self.Label7 = Label(self.Labelbox3, text='0', font=('Helvetica', 16))
        self.Label7.pack()

        self.Frame6 = Frame(master)
        self.Frame6.pack()
        
        self.Label8 = Label(self.Frame6, text='a : ', font=('Helvetica', 16))
        self.Label8.pack(side=LEFT)

        self.Labelbox4 = LabelFrame(self.Frame6)
        self.Labelbox4.pack(side=LEFT)

        self.Label9 = Label(self.Labelbox4, text='0', font=('Helvetica', 16))
        self.Label9.pack()

        self.Frame7 = Frame(master)
        self.Frame7.pack()
        
        self.Label10 = Label(self.Frame7, text='r : ', font=('Helvetica', 16))
        self.Label10.pack(side=LEFT)

        self.Labelbox5 = LabelFrame(self.Frame7)
        self.Labelbox5.pack(side=LEFT)

        self.Label11 = Label(self.Labelbox5, text='0', font=('Helvetica', 16))
        self.Label11.pack()

        self.Frame8 = Frame(master)
        self.Frame8.pack()

        self.Button4 = Button(self.Frame8, text='Convect to %PE', font=('Helvetica', 16), command=self.convect_pe)
        self.Button4.pack()

        self.Frame9 = Frame(master)
        self.Frame9.pack()

        self.Label12 = Label(self.Frame9, text='%PE : ', font=('Helvetica', 16))
        self.Label12.pack(side=LEFT)

        self.Labelbox6 = LabelFrame(self.Frame9)
        self.Labelbox6.pack(side=LEFT)

        self.Label13 = Label(self.Labelbox6, text='', font=('Helvetica', 16))
        self.Label13.pack()

        self.preesb1 = False
        self.preesb2 = False
        self.preesb3 = False

    def on_event(self):
        global g,v,a,r
        g=(float(self.Entry2.get()))/(6.022*10**23)
        v=g/float(self.Entry.get())
        a=v**3
        r=a/2
        if self.Button2.cget('bg') != 'White' or self.Button3.cget('bg') != 'White':
            self.Button2.config(bg='White')
            self.Button3.config(bg='White')
            self.Label5.config(text='0')
            self.Label7.config(text='0')
            self.Label9.config(text='0')
            self.Label11.config(text='0')
            self.preesb2 = False
            self.preesb3 = False
        elif self.Button.cget('bg') == 'White': 
            self.Button.config(bg='Green')
            self.Label5.config(text=f'{g}')
            self.Label7.config(text=f'{v}')
            self.Label9.config(text=f'{a}')
            self.Label11.config(text=f'{r}')
            self.preesb1 = True
        else:
            self.Button.config(bg='White')
            self.Label5.config(text='0')
            self.Label7.config(text='0')
            self.Label9.config(text='0')
            self.Label11.config(text='0')
            self.preesb1 = False

    def on_event2(self):
        global g,v,a,r
        g=(float(self.Entry2.get())*2)/(6.022*10**23)
        v=g/float(self.Entry.get())
        a=v**3
        r=(a*sqrt(3))/4
        if self.Button.cget('bg') != 'White' or self.Button3.cget('bg') != 'White':
            self.Button.config(bg='White')
            self.Button3.config(bg='White')
            self.Label5.config(text='0')
            self.Label7.config(text='0')
            self.Label9.config(text='0')
            self.Label11.config(text='0')
            self.preesb1 = False
            self.preesb3 = False
        elif self.Button2.cget('bg') == 'White': 
            self.Button2.config(bg='Green')
            self.Label5.config(text=f'{g}')
            self.Label7.config(text=f'{v}')
            self.Label9.config(text=f'{a}')
            self.Label11.config(text=f'{r}')
            self.preesb2 = True
        else:
            self.Button2.config(bg='White')
            self.Label5.config(text='0')
            self.Label7.config(text='0')
            self.Label9.config(text='0')
            self.Label11.config(text='0')
            self.preesb2 = False
    
    def on_event3(self):
        global g,v,a,r
        g=(float(self.Entry2.get())*4)/(6.022*10**23)
        v=g/float(self.Entry.get())
        a=v**3
        r=a/sqrt(8)
        if self.Button.cget('bg') != 'White' or self.Button2.cget('bg') != 'White':
            self.Button.config(bg='White')
            self.Button2.config(bg='White')
            self.Label5.config(text='0')
            self.Label7.config(text='0')
            self.Label9.config(text='0')
            self.Label11.config(text='0')
            self.preesb1 = False
            self.preesb2 = False
        elif self.Button3.cget('bg') == 'White': 
            self.Button3.config(bg='Green')
            self.Label5.config(text=f'{g}')
            self.Label7.config(text=f'{v}')
            self.Label9.config(text=f'{a}')
            self.Label11.config(text=f'{r}')
            self.preesb3 = True
        else:
            self.Button3.config(bg='White')
            self.Label5.config(text='0')
            self.Label7.config(text='0')
            self.Label9.config(text='0')
            self.Label11.config(text='0')
            self.preesb3 = False
    def convect_pe(self):
        if self.preesb1 == True:
            voc=float(self.Label9.cget('text'))**3
            vos=(4*pi*float(self.Label11.cget('text'))**3)/3
            self.Label13.config(text=f'{round((vos/voc)*100, 2)}%')
        elif self.preesb2 == True:
            voc=float(self.Label9.cget('text'))**3
            vos=(2*4*pi*float(self.Label11.cget('text'))**3)/3
            self.Label13.config(text=f'{round((vos/voc)*100, 2)}%')
        elif self.preesb3 == True:
            voc=float(self.Label9.cget('text'))**3
            vos=(4*4*pi*float(self.Label11.cget('text'))**3)/3
            self.Label13.config(text=f'{round((vos/voc)*100, 2)}%')
        else:
            self.Label13.config(text=f'')
            messagebox.showerror("Announcement!", "Please Select PE!")   
def main():
    root=Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()