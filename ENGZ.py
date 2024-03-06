from tkinter import *
from random import * 
from math import *

Food = {
    45:'ต้มยำกุ้ง',
    35:'ข้าวผัด',
    35:'ก๋วยเตี๋ยว',
    25:'ข้าวหมูทอด',
    20:'ข้าวเหนียวหมูปิ้ง',
    20:'ข้าวเหนียวลาบ',
    20:'ข้าวต้ม',
    20:'โจ๊ก',
    35:'ข้าวมันไก่',
    35:'ข้าวมันไก่ทอด',
    35:'ข้าวผัดกะเพรา',
    40:'ข้าวผัดกะเพราไข่ดาว',   
    35:'ราดหน้า',
    35:'ผัดซีอิ๊ว',
    30:'ข้าวไข่เจียวหมูสับ',
    15:'ข้าวไข่ต้ม2ลูก'
}

Food2 = {
    'ต้มยำกุ้ง':45,
    'ข้าวผัด':35,
    'ก๋วยเตี๋ยว':35,
    'ข้าวหมูทอด':25,
    'ข้าวเหนียวหมูปิ้ง':20,
    'ข้าวเหนียวลาบ':20,
    'ข้าวต้ม':20,
    'โจ๊ก':20,
    'ข้าวมันไก่':35,
    'ข้าวมันไก่ทอด':35,
    'ข้าวผัดกะเพรา':35,
    'ข้าวผัดกะเพราไข่ดาว':40,
    'ราดหน้า':35,
    'ผัดซีอิ๊ว':35,
    'ข้าวไข่เจียวหมูสับ':30,
    'ข้าวไข่ต้ม2ลูก':15
}

Water = {
    5:'น้ำเปล่า',
    20:'ชาเขียวเย็น',
    20:'ชามะนาว',
    10:'โค้ก',
    25:'ชานมไข่มุก',
    20:'ชาไทย',
    20:'เฉาก๊วยนมสด',
    15:'น้ำส้ม',
    20:'น้ำแตงโม'
}

Water2 = {
    'น้ำเปล่า':5,
    'ชาเขียวเย็น':20,
    'ชามะนาว':20,
    'โค้ก':10,
    'ชานมไข่มุก':25,
    'ชาไทย':20,
    'เฉาก๊วยนมสด':20,
    'น้ำส้ม':15,
    'น้ำแตงโม':20
}


class CzGz:
    def __init__(self, master):
        self.master = master
        master.title('โปรแกรมหาอาหารตามจำนวนเงิน')

        self.lable = Label(master, text='\n\n\n', font=('Helvetica', 16))
        self.lable.pack()
        
        self.Frame = Frame(master)
        self.Frame.pack()

        self.lable2 = Label(self.Frame, text='How much money do u have ? ', font=('Helvetica', 16))
        self.lable2.pack(side=LEFT)

        self.Entry = Entry(self.Frame, textvariable=IntVar(), font=('Helvetica', 16))
        self.Entry.pack(side=LEFT)

        self.ButtonEntry = Button(self.Frame, text='Entry', font=('Helvetica', 16), command=self.EntryFunc)
        self.ButtonEntry.pack(side=LEFT)

        self.ButtonReset = Button(self.Frame, text='Reset', font=('Helvetica', 16), command=self.Reset)
        self.ButtonReset.pack(side=LEFT)

        self.Frame2 = Frame(master)
        self.Frame2.pack()

        self.lable3 = Label(self.Frame2, text='Food :', font=('Helvetica', 16))
        self.lable3.pack(side=LEFT)

        self.lableMid = Label(self.Frame2, text='                             ', font=('Helvetica', 16))
        self.lableMid.pack(side=LEFT)

        self.lable4 = Label(self.Frame2, text='Water :', font=('Helvetica', 16))
        self.lable4.pack(side=LEFT)

        self.Frame3 = Frame(master)
        self.Frame3.pack()


        self.Listbox =Listbox(self.Frame3, font=('Helvetica', 16))
        self.Listbox.pack(side=LEFT)

        self.Listbox2 =Listbox(self.Frame3, font=('Helvetica', 16))
        self.Listbox2.pack(side=LEFT)


        self.Frame4 = Frame(master)
        self.Frame4.pack()

        self.lable5 = Label(self.Frame4, text='', font=('Helvetica', 16))
        self.lable5.pack(side=LEFT)

        self.lableMid2 = Label(self.Frame4, text=' ', font=('Helvetica', 16))
        self.lableMid2.pack(side=LEFT)

        self.lable6 = Label(self.Frame4, text='', font=('Helvetica', 16))
        self.lable6.pack(side=LEFT)

        self.Frame5 = Frame(master)
        self.Frame5.pack()

        self.Button = Button(self.Frame5, text='Seclect_Food', command=self.Select_Food, font=('Helvetica', 16))
        self.Button.pack(side=LEFT)

        self.Button2 = Button(self.Frame5, text='Seclect_Water', command=self.Seclect_Water, font=('Helvetica', 16))
        self.Button2.pack(side=LEFT)

    def Select_Food(self):
        self.lable5.config(text=f'Food : {Food2[f'{self.Listbox.get(ACTIVE)}']} Bath')

    def Seclect_Water(self):
        self.lable6.config(text=f'Water : {Water2[f'{self.Listbox2.get(ACTIVE)}']} Bath')

    def Reset(self):
        self.Listbox.delete(0, END)
        self.Listbox2.delete(0 , END)
        self.lable5.config(text=f'')
        self.lable6.config(text=f'')

    def EntryFunc(self):
        a=list(Food.keys())
        b=list(Water.keys())
        for i in a:
            if int(self.Entry.get()) >= i:
                self.Listbox.insert(END, Food[i])
        for p in b:
            if int(self.Entry.get()) >= p:
                self.Listbox2.insert(END, Water[p])

def main():
    root = Tk()
    CzGz(root)
    root.geometry('1920x1080')
    root.mainloop()

if __name__ == '__main__':
    main()

