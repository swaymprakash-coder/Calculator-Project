from tkinter import*
import random
import time;
import datetime
root=Tk()
root.geometry("450x650+0+0")
root.title("Swaym's Calculator")
#==============================Frame and label===========================

Tops = Frame(root,width=450,height=100,bd=8, relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=500,height=560,bd=8,relief="raise")
f1.pack(side=LEFT)
#===============================functions, variable and operators======================
text_Input=StringVar()
operator=""

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)    





#===============================Label and Display Area=======================

lblinfo=Label(Tops,font=('arial',24,'bold'), text="Swaym's Calculator", fg="orange",bg="black", bd=10,anchor='w')
lblinfo.grid(row=0, column=0)

textDisplay=Entry(f1,font=('arial',20,'bold'), textvariable=text_Input,bd=40, insertwidth=5, justify='right')
textDisplay.grid(columnspan=4)
#=================================button (9,8,7, +)=============================

btn7=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="7", command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="8", command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="9", command=lambda:btnClick(9)).grid(row=1,column=2)
btnplus=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="+", command=lambda:btnClick('+')).grid(row=1,column=3)

#=================================button (4,5,6, -)=============================

btn6=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="6", command=lambda:btnClick(6)).grid(row=2,column=0)
btn5=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="5", command=lambda:btnClick(5)).grid(row=2,column=1)
btn4=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="4", command=lambda:btnClick(4)).grid(row=2,column=2)
btnminus=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="-", command=lambda:btnClick('-')).grid(row=2,column=3)

#=================================button (1,2,3, *)=============================

btn3=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="3", command=lambda:btnClick(3)).grid(row=3,column=0)
btn2=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="2", command=lambda:btnClick(2)).grid(row=3,column=1)
btn1=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="1", command=lambda:btnClick(1)).grid(row=3,column=2)
btnMul=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="*", command=lambda:btnClick('*')).grid(row=3,column=3)

#=================================button (0,=,clear, /)=============================

btn0=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="0", command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear=Button(f1,padx=16,pady=16,bd=8,fg="black",bg='red', font=('arial',20,'bold'), text="C", command=btnClearDisplay).grid(row=4,column=1)
btnEquals=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="=", command=btnEqualsInput).grid(row=4,column=2)
btnDiv=Button(f1,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'), text="/", command=lambda:btnClick('/')).grid(row=4,column=3)






