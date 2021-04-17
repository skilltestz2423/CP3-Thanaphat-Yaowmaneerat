from tkinter import*

def leftClickButton(event):
    BMI = (float(textBoxWeight.get())/((float(textBoxHeight.get())/100)**2))
    if BMI>30:
        bmiResult ='อ้วนเกินไป'
    elif BMI>=25:
        bmiResult ='อ้วน'
    elif BMI>=23:
        bmiResult ='น้ำหนักเกิน'
    elif BMI>=18.6:
        bmiResult ='น้ำหนักปกติ'
    elif BMI<=18.5:
        bmiResult ='ผอมเกินไป'
    labelResult.configure(text=bmiResult)


main = Tk()
labelHeight = Label(main,text='ส่วนสูง (Cm.)')
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(main,text='น้ำหนัก (Kg.)')
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(main,text='คำนวณ')
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(main,text='ผลลัพธ์')
labelResult.grid(row=2,column=1)
main.mainloop()