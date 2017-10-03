#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import time
import Models

class Main():
    def __init__(self):
        today = time.strftime("%d.%m.%Y")
        self.conn, self.cursor = Models.createOrOpenTable()
        self.today = today.split(".")
        Models.pushNewDate(today.replace(".", ""))
        self.first=True
        self.main()


    def main(self):
        self.gui = Tk()
        self.gui.resizable(width=False, height = False)
        self.gui.minsize(width=1000, height = 800)

        titleLabel = Label(self.gui, bg="black", fg="white" ,text="Gelir Gider Takip", width=80, height= 2, font = "Times 20 bold").place(heigh= 50, width = 1000)

        printImage=PhotoImage(file="print.gif")
        printButton= Button(self.gui)
        printButton.config(image=printImage, compound=RIGHT, command=self.saveAs)
        printButton.place(x=850, y=100, width=100, height=100)

        saveImage=PhotoImage(file="save.gif")
        saveButton = Button(self.gui)
        saveButton.config(image = saveImage, compound=RIGHT, command=self.pushData)
        saveButton.place(y=100, x=700, width=100, height=100)

        dateLabel= Label(self.gui, text="Tarih:", font="Times 14", width=6).place(y=55, x=0, width=50, height=30)
        self.day = StringVar(self.gui)
        self.day.set(self.today[0])
        days =  ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        daySelection = OptionMenu(self.gui, self.day, *days).place(y=55, x=165, width=50, height=30)

        self.month = StringVar(self.gui)
        self.month.set(self.today[1])
        months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        monthSelection = OptionMenu(self.gui, self.month, *months).place(y=55, x=110, width=50, height=30)

        self.year = StringVar(self.gui)
        self.year.set(self.today[2])
        yearSelection = Entry(self.gui, textvariable=self.year, width=6).place(y=55, x=55, width=50, height=30)

        setDateButton = Button(self.gui, text="Tarih\'e Git.", font="Times 12 bold" , command=self.getData).place(y = 55, x = 250, width= 100, height = 30)

        totalIncomeLabel= Label(self.gui, text="Toplam Gelir:", font="Times 12 bold", width=14, bg="red", fg="white").place(y=90, x = 0, height=30)
        totalOutcomeLabel = Label(self.gui, text="Toplam Gider:", font="Times 12 bold", width=14, bg="red", fg="white").place(y=125, x=0, height=30)
        totalRevenueLabel = Label(self.gui, text="Toplam Kar:", font="Times 12 bold", width=14, bg="red", fg="white").place(y=160, x=0, height=30)

        self.totalIncome = DoubleVar()
        totalIncomeText = Entry(self.gui, textvariable=self.totalIncome, width = 10, state=DISABLED, bg = "red").place(y=90, x=120, height=30)

        self.totalOutcome = DoubleVar()
        totalOutcomeText = Entry(self.gui, textvariable=self.totalOutcome, width=10, state=DISABLED, bg="red").place(y=125,x=120,height=30)

        self.totalRevenue = DoubleVar()
        totalRevenueText = Entry(self.gui, textvariable=self.totalRevenue, width=10, state=DISABLED, bg="red").place(y=160,x=120,height=30)

        pastIncomeLabel=Label(self.gui, text="Önceki Toplam Gelir:", font="Times 12 bold", width=17, bg="red", fg="white").place(y=90, x=480, height=30)
        self.pastIncome = DoubleVar()
        pastIncomeText= Entry(self.gui, textvariable=self.pastIncome, width=10, state=DISABLED).place(y=90, x=635, height=30)

        pastOutcomeLabel = Label(self.gui, text="Önceki Toplam Gider:", font="Times 12 bold", width=17, bg="red",
                                fg="white").place(y=125, x=480, height=30)
        self.pastOutcome = DoubleVar()
        pastOutcomeText = Entry(self.gui, textvariable=self.pastIncome, width=10, state=DISABLED).place(y=125, x=635,
                                                                                                       height=30)
        self.dailyNetIncome = DoubleVar()
        dailyNetIncomeLabel = Label(self.gui, text="Günlük Net Gelir", font="Times 12 bold", width=17, bg="red", fg="white").place(y=195, x=480, height=30)
        dailyNetIncomeText = Entry(self.gui, textvariable=self.dailyNetIncome, width=10, state=DISABLED).place(y = 195, x=635, height=30)

        self.dailyNetOutcome = DoubleVar()
        dailyNetOutcomeLabel = Label(self.gui, text="Günlük Net Gider", font="Times 12 bold", width=17, bg="red",
                                    fg="white").place(y=230, x=480, height=30)
        dailyNetOutcomeText = Entry(self.gui, textvariable=self.dailyNetOutcome, width=10, state=DISABLED).place(y=230, x=635, height=30)

        self.pastVault = DoubleVar()
        pastVaultLabel = Label(self.gui, text="Devreden Kasa:", font="Times 12 bold", width=20, anchor=E).place(y=90, x= 200, height=30)
        pastVaultText = Entry(self.gui, textvariable=self.pastVault, width=10, state=DISABLED).place(y=90,x=400,height=30)

        self.todayVault = DoubleVar()
        todayVaultLabel = Label(self.gui, text="Günlük Mevcut Kasa:", font="Times 12 bold", width=20, anchor=E).place(y=125, x=200, height=30)
        todayVaultText = Entry(self.gui, textvariable=self.todayVault, width=10).place(y=125, x=400, height=30)

        self.totalVault = DoubleVar()
        self.totalVault.set(self.todayVault.get()+self.pastVault.get())
        totalVaultLabel = Label(self.gui, text="Toplam Günlük Kasa:", font="Times 12 bold", width=20, anchor=E).place(y=160, x=200, height=30)
        totalVaultText = Entry(self.gui, textvariable=self.totalVault, width=10, state=DISABLED).place(y=160, x=400, height=30)

        self.mainVaultProductsTotal = DoubleVar()

        self.totalPastVault = DoubleVar()

        totalPastVaultLabel = Label(self.gui, text="Devreden Toplam Kasa:", font="Times 12 bold", width=20, anchor=E).place(y=195,x=200,height=30)
        totalPastVaultText = Entry(self.gui, textvariable=self.totalPastVault, width=10, state=DISABLED).place(y=195, x=400,height=30)

        dailyOutProductsLabel= Label(self.gui, text="Çıkan Ürün \t\t Açıklama \t\t Tutar", font="Times 12 bold", bg = "white").place(y=265, x=0, height=30, width=500)
        self.dailyOutProductsNames = Listbox(self.gui, font="Times 12")
        self.dailyOutProductsNames.place(y=295, x=0, height=300, width=150)
        self.dailyOutProductsDescs = Listbox(self.gui, font="Times 12")
        self.dailyOutProductsDescs.place(y=295, x=150, height=300, width=250)
        self.dailyOutProductsAmounts = Listbox(self.gui, font="Times 12")
        self.dailyOutProductsAmounts.place(y=295, x=400, height=300, width=130)
        addDailyOutProductButton = Button(self.gui, font = "Times 20 bold", text ="+", fg = "green", bg="white", command=self.addDailyProduct).place(y=265,x=470, height=30, width=30)
        subDailyOutProductButton = Button(self.gui, font="Times 20 bold", text="-", fg="red", bg="white",
                                          command=self.subDailyProduct).place(y=265, x=500, height=30, width=30)

        totalDailyOutcomeLabel=Label(self.gui, text="Günlük Toplam Gider:", font="Times 12 bold", bg="red").place(y=600, x=245, height=30)
        self.totalDailyOutcome=DoubleVar()
        totalDailyOutcomeEntry=Entry(self.gui, textvariable=self.totalDailyOutcome, state=DISABLED).place(y=600, x=405, height=30)

        mainVaultOutProductsLabel=Label(self.gui, text="Ana Kasa Çıkan Ürün \t\t Tutar", font="Times 12 bold", bg="white").place(y=265, x=535, height=30, width=455)
        self.mainVaultProductsNames = Listbox(self.gui,font="Times 12")
        self.mainVaultProductsNames.place(y=295, x=535, height=300, width=340)
        self.mainVaultProductsAmounts = Listbox(self.gui, font="Times 12")
        self.mainVaultProductsAmounts.place(y=295, x=535+340, height=300, width=455-345)

        mainVaultProductsTotalLabel = Label(self.gui, text="Anakasa Çıkan Ürün Toplam:", font="Times 12 bold", bg="red").place(y=600,x=665,height=30)

        mainVaultProductsTotalEntry = Entry(self.gui, textvariable=self.mainVaultProductsTotal, state=DISABLED).place(
            y=600, x=535+340, height=30)

        addDailyOutProductButton = Button(self.gui, font="Times 20 bold", text="+", fg="green", bg="white",
                                          command=self.addMainVaultProduct).place(y=265, x=925, height=30, width=30)
        subDailyOutProductButton = Button(self.gui, font="Times 20 bold", text="-", fg="red", bg="white",
                                          command=self.subMainVaultProduct).place(y=265, x=955, height=30, width=30)

        self.pastVisa = DoubleVar()
        pastVisaLabel = Label(self.gui, text="Önceki Visa: ", width=10, bg="red", fg="white",
                              font="Times 12 bold").place(y=670, x=100, height=30)
        pastVisaText = Entry(self.gui, textvariable=self.pastVisa, state=DISABLED).place(y=670, x=200,
                                                                                                   height=30)

        self.dailyVisa = DoubleVar()
        dailyVisaLabel=Label(self.gui, text="Günlük Visa:", font = "Times 12 bold").place(y=705, x=100, height=30)
        dailyVisaText=Entry(self.gui, textvariable=self.dailyVisa).place(y=705, x=200, height=30)

        self.totalVisa = DoubleVar()

        totalVisaLabel= Label(self.gui, text="Toplam Visa:", font = "Times 12 bold").place(y=740, x=100, height=30)
        totalVisaText=Entry(self.gui, textvariable=self.totalVisa, state=DISABLED).place(y=740, x=200, height=30)




        if self.first:
            self.getData()
            self.first = False
        self.gui.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.gui.bind("<Return>", self.pushData)
        self.gui.mainloop()

    def getData(self):
        try:
            self.selectedDate = "%s%s%s" % (self.day.get(), self.month.get(), self.year.get())
        except AttributeError:
            self.selectedDate = "%s%s%s" % (self.today[0], self.today[1], self.today[2])
        data = Models.loadData(self.selectedDate)
        print data
        if data is not None:
            self.totalIncome.set(data[1])
            self.totalOutcome.set(data[2])
            self.totalRevenue.set(data[3])
            self.pastVault.set(data[4])
            self.todayVault.set(data[5])
            self.totalVault.set(data[6])
            self.totalPastVault.set(data[8])
            self.totalDailyOutcome.set(data[10])
            self.mainVaultProductsTotal.set(data[12])

            if data[9]:
                self.parseData(data[9], True)
            if data[11]:
                self.parseData(data[11], False)
        else:
            tkMessageBox.showerror("Tarih Kaydı Bulunamadı.", "Tarih kaydı bulunamadı. Bugüne geri yönlendiriliyorsunuz.")
            Models.loadData("%s%s%s" % (self.today[0], self.today[1], self.today[2]))

    def parseData(self, data, daily):
        data = data.split(".")
        if daily:
            for i in data:
                j = i.split(",")
                self.dailyOutProductsNames.insert(END, j[0])
                self.dailyOutProductsDescs.insert(END, j[1])
                self.dailyOutProductsAmounts.insert(END, j[2])
        else:
            for i in data:
                j = i.split(",")
                self.mainVaultProductsNames.insert(END, j[0])
                self.mainVaultProductsAmounts.insert(END, j[1])
        pass

    def pushData(self, event=None):

        self.totalVisa.set(self.dailyVisa.get() + self.pastVisa.get())

        self.totalVault.set(self.pastVault.get() + self.todayVault.get())

        self.totalPastVault.set(self.totalVault.get() - self.mainVaultProductsTotal.get())

        self.dailyNetOutcome.set(self.totalDailyOutcome.get() + self.mainVaultProductsTotal.get())

        self.totalOutcome.set(self.dailyNetOutcome.get() + self.pastOutcome.get())

        self.dailyNetIncome.set(self.totalVisa.get() + self.todayVault.get())

        self.totalIncome.set(self.dailyNetIncome.get() + self.pastIncome.get())

        self.totalRevenue.set(self.totalIncome.get() - self.totalOutcome.get())

        mainVault=""
        for i in range(self.mainVaultProductsNames.size()):
            if i == 0:
                try:
                    mainVault += "%s,%d" %(self.mainVaultProductsNames.get(i), self.mainVaultProductsAmounts.get(i))
                except TypeError:
                    mainVault += "%s,%s" % (self.mainVaultProductsNames.get(i), self.mainVaultProductsAmounts.get(i))
            else:
                try:
                    mainVault += ".%s,%d" % (self.mainVaultProductsNames.get(i), self.mainVaultProductsAmounts.get(i))
                except TypeError:
                    mainVault += ".%s,%s" % (self.mainVaultProductsNames.get(i), self.mainVaultProductsAmounts.get(i))

        dailyOut=""
        for i in range(self.dailyOutProductsNames.size()):
            if i==0:
                try:
                    dailyOut += "%s,%s,%d" %(self.dailyOutProductsNames.get(i), self.dailyOutProductsDescs.get(i),
                                             self.dailyOutProductsAmounts.get(i))
                except TypeError:
                    dailyOut += "%s,%s,%s" % (self.dailyOutProductsNames.get(i), self.dailyOutProductsDescs.get(i),
                                              self.dailyOutProductsAmounts.get(i))
            else:
                try:
                    dailyOut += ".%s,%s,%d" % (self.dailyOutProductsNames.get(i), self.dailyOutProductsDescs.get(i),
                                          self.dailyOutProductsAmounts.get(i))
                except TypeError:
                    dailyOut += ".%s,%s,%s" % (self.dailyOutProductsNames.get(i), self.dailyOutProductsDescs.get(i),
                                              self.dailyOutProductsAmounts.get(i))


        date=str(self.day.get())+str(self.month.get()) + str(self.year.get())
        Models.updateData(date, totalIncome=self.totalIncome.get(), totalOutcome=self.totalOutcome.get(),
                          pastVault=self.pastVault.get(), todayVault=self.todayVault.get(),
                          dailyOutProducts=dailyOut,
                          dailyOutProductsTotal=self.totalDailyOutcome.get(), mainVaultProducts=mainVault,
                          mainVaultProductsTotal=self.mainVaultProductsTotal.get())

    def addDailyProduct(self):
        self.topDailyOutProduct = Toplevel(self.gui)
        self.topDailyOutProduct.wm_minsize(300, 50)
        self.topDailyOutProduct.wm_resizable(False, False)
        self.addDailyOutProduct_name=StringVar()
        self.addDailyOutProduct_desc=StringVar()
        self.addDailyOutProduct_amount=DoubleVar()
        Label(self.topDailyOutProduct, text="Urun Adi", font="Times 11 bold").place(x=0, y=0, width=70, height=30)
        Entry(self.topDailyOutProduct, textvariable=self.addDailyOutProduct_name, font="Times 12").place(x=70, y=0, width=225, height=30)
        Label(self.topDailyOutProduct, text="Aciklama", font="Times 11 bold").place(x=0, y=35, width=70, height=30)
        Entry(self.topDailyOutProduct, textvariable=self.addDailyOutProduct_desc, font="Times 12").place(x=70, y=35, width=225, height=30)
        Label(self.topDailyOutProduct, text="Tutar", font="Times 11 bold").place(x=0, y=70, width=70, height=30)
        Entry(self.topDailyOutProduct, textvariable=self.addDailyOutProduct_amount, font="Times 12").place(x=70, y=70, width=225, height=30)

        Button(self.topDailyOutProduct, text="Ekle", font="Times 11 bold", command=self.totalDailyProductAmount).place(width=70, x=115, y=120)

    def totalDailyProductAmount(self):
        name = self.addDailyOutProduct_name.get()
        desc = self.addDailyOutProduct_desc.get()
        amount = self.addDailyOutProduct_amount.get()
        if name == "":
            tkMessageBox.showerror("İsim Eksik", "Ürün eklemek için isim belirtmek zorundasınız")
        else:
            self.dailyOutProductsNames.insert(END, name)
            self.dailyOutProductsDescs.insert(END, desc)
            self.dailyOutProductsAmounts.insert(END, amount)
            self.totalDailyOutcome.set(self.totalDailyOutcome.get() + self.addDailyOutProduct_amount.get())
            self.topDailyOutProduct.destroy()
            self.pushData()

    def subDailyProduct(self):
        name = self.dailyOutProductsNames.curselection()
        desc = self.dailyOutProductsDescs.curselection()
        amount= self.dailyOutProductsAmounts.curselection()

        toDelete = None
        if name != ():
            toDelete=name[0]
        elif desc!=():
            toDelete=desc[0]
        elif amount!=():
            toDelete=amount[0]
        else:
            return

        self.totalDailyOutcome.set(self.totalDailyOutcome.get() - float(self.dailyOutProductsAmounts.get(toDelete)))
        self.dailyOutProductsNames.delete(toDelete)
        self.dailyOutProductsDescs.delete(toDelete)
        self.dailyOutProductsAmounts.delete(toDelete)
        self.pushData()
        pass

    def on_closing(self):
        if tkMessageBox.askokcancel("Çıkış", "Çıkış yapmak istediğinizden emin misiniz? \nKaydedilmemiş veriler kaydedilecek."):
            self.pushData()
            self.gui.destroy()

    def addMainVaultProduct(self):
        self.topMainVaultProduct = Toplevel(self.gui)
        self.topMainVaultProduct.wm_minsize(300, 50)
        self.topMainVaultProduct.wm_resizable(False, False)
        self.addMainVaultProduct_name = StringVar()
        self.addMainVaultProduct_amount = DoubleVar()
        Label(self.topMainVaultProduct, text="Urun Adi", font="Times 11 bold").place(x=0, y=0, width=70, height=30)
        Entry(self.topMainVaultProduct, textvariable=self.addMainVaultProduct_name, font="Times 12").place(x=70, y=0, width=225,
                                                                                                           height=30)
        Label(self.topMainVaultProduct, text="Tutar", font="Times 11 bold").place(x=0, y=35, width=70, height=30)
        Entry(self.topMainVaultProduct, textvariable=self.addMainVaultProduct_amount, font="Times 12").place(x=70, y=35,
                                                                                                             width=225,
                                                                                                             height=30)

        Button(self.topMainVaultProduct, text="Ekle", font="Times 11 bold", command=self.totalMainVaultProductAmount).place(width=70, x=115,
                                                                                                           y=80)

    def totalMainVaultProductAmount(self):
        name = self.addMainVaultProduct_name.get()
        if name=="":
            tkMessageBox.showerror("İsim Eksik", "Ürün eklemek için isim belirtmek zorundasınız")
        else:
            self.mainVaultProductsNames.insert(END, name)
            self.mainVaultProductsAmounts.insert(END, self.addMainVaultProduct_amount.get())
            self.mainVaultProductsTotal.set(self.mainVaultProductsTotal.get() + self.addMainVaultProduct_amount.get())
            self.topMainVaultProduct.destroy()
            self.pushData()

    def subMainVaultProduct(self):
        name = self.mainVaultProductsNames.curselection()
        amount= self.mainVaultProductsAmounts.curselection()

        toDelete = None
        if name != ():
            toDelete=name[0]
        elif amount!=():
            toDelete=amount[0]
        else:
            return

        self.mainVaultProductsTotal.set(self.mainVaultProductsTotal.get()-float(self.mainVaultProductsAmounts.get(toDelete)))
        self.mainVaultProductsNames.delete(toDelete)
        self.mainVaultProductsAmounts.delete(toDelete)
        self.pushData()

    def saveAs(self):
        pass


start = Main()
