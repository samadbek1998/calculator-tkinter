# kalkulator yaratish
# kalkulator yasash 1-qism

import tkinter as tk
from tkinter import messagebox

def raqam_joylashtirish(raqam):
    #value = kirish.get()+ str(raqam) # value degan o'zgaruvchiga malumotlarni olib yangi malumotlarni uni ortidan qo'shish uchun ishlatdik
    value = kirish.get()
    if value[0]=='0' and len(value)==1:
        value = value[1:]
    kirish.delete(0,tk.END)
    kirish.insert(0, value+str(raqam))

def add_operation(operation):
    value = kirish.get()
    if value[-1] in "+-*/":
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        make_hisoblash()
        value = kirish.get() 
    kirish.delete(0, tk.END)
    kirish.insert(0, value+operation)

def button_hosilqilish(raqam):
    return tk.Button(text=raqam, bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(raqam)) 

def operation_button_hosil_qilish(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', 
                    command=lambda:add_operation(operation)
                    )

def make_hisoblash():
    value = kirish.get()
    if value[-1] in '+/*-':
        operation = value[-1]
        value = value[:1]+operation+value[:-1]
    kirish.delete(0,tk.END)
    try:  # agarda hamma narsa to'gri ishlasa try ni ichida yozilgan narsalar ishlaydi     
        kirish.insert(0, eval(value))# eval bu matemetik hisoblashlarni stiringda bo'lsa ham amalga oshiradi
    except: #agar qanqadur xatoliklar bo'lsa bizga xatolik haqida xabar beradida keyin dasturimiz yana ishlayveradi
        messagebox.showinfo('Diqqat',"Iltimos faqat raqam kiriting, siz boshqa narsa kiritdingiz")
        kirish.insert(0,0)
def hisoblash(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', 
                    command=make_hisoblash) # make hisoblash fumksiyasiga yuboramiz

def ac():
    kirish.delete(0,tk.END)
    kirish.insert(0,0) 

def ac_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial',10), fg='red',
                    command=ac    
                        )
def pres_key(event):# klavyaturadan bosilgan elementlarni olib olamiz
    #print(event.char)# bosilgan elementlarni faqat harf qismini olish uchun ishlatamiz 
    if event.char.isdigit(): #Agar bosilgan kinopka raqammi yoqmi shuni bilib oldik
        raqam_joylashtirish(event.char) #agar raqam bo'lsa oynamizga qo'shdik bo'lmasa yoq
    elif event.char in "+-*/": # agar bosilgan knopkalarni ichida +-*/ shu amallar bo'lsa tekshiruvini o'tqazdik
        add_operation(event.char)  # aperatsiyalar qo'shish buyurug'ini qo'shib oldik  
    elif event.char == '\r':# agar kiritilgn raqam enter ga teng bo'lsa 
        make_hisoblash() #meke hisoblash funksiyasini chaqirdik

win = tk.Tk()
win.geometry("240x280")
win.config(bg="#33ffe6")
win.title("Kalkulator")
win.bind('<Key>', pres_key) # klavyatura orqli malumot kiritishimiz uchun bundan foydalanamiz

kirish = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15) #  justify=tk.RIGHT Malumotlarni yozganda o'ng tomondan chiqarish uchun ishlatiladi 
kirish.insert(0,'0')
kirish.grid(row=0, column=0, columnspan=3, stick='we', padx=5, pady=5)

button_hosilqilish("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)# lambda funksiyasida har bitta knopka bosilganida yozish funksiyasi berilgan
tk.Button(win, text="2", bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(2)).grid(row=2, column=0, stick="wens", padx=5, pady=5)# bd bu knopka qilish uchun ishlatiladi  
tk.Button(win, text="3", bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(3)).grid(row=3, column=0, stick="wens", padx=5, pady=5)
tk.Button(win, text="4", bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(4)).grid(row=1, column=1 ,stick="wens", padx=5, pady=5)
tk.Button(win, text="5", bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(5)).grid(row=2, column=1, stick="wens", padx=5, pady=5)
tk.Button(win, text="6", bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(6)).grid(row=3, column=1, stick="wens", padx=5, pady=5)
tk.Button(win, text="7", bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(7)).grid(row=1, column=2, stick="wens", padx=5, pady=5)
tk.Button(win, text="8", bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(8)).grid(row=2, column=2, stick="wens", padx=5, pady=5)
tk.Button(win, text="9", bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(9)).grid(row=3, column=2, stick="wens", padx=5, pady=5)
tk.Button(win, text="0", bd=5, font=('Arial', 13), command=lambda:raqam_joylashtirish(0)).grid(row=4, column=0, stick="wens", padx=5, pady=5)
button_hosilqilish('.').grid(row=4, column=1, stick="wens", padx=5, pady=5)


operation_button_hosil_qilish('+').grid(row=1, column=3, stick="wens", padx=5, pady=5)
operation_button_hosil_qilish('-').grid(row=2, column=3, stick="wens", padx=5, pady=5)
operation_button_hosil_qilish('*').grid(row=3, column=3, stick="wens", padx=5, pady=5)
operation_button_hosil_qilish('/').grid(row=4, column=3, stick="wens", padx=5, pady=5)

hisoblash('=').grid(row=4, column=2, stick="wens", padx=5, pady=5)
ac_button("C").grid(row=0, column=3, stick='wens', padx=3, pady=3)

win.columnconfigure(0, minsize=60)
win.columnconfigure(1, minsize=60)
win.columnconfigure(2, minsize=60)
win.columnconfigure(3, minsize=60)


win.rowconfigure(1, minsize=60)
win.rowconfigure(2, minsize=60)
win.rowconfigure(3, minsize=60)
win.rowconfigure(4, minsize=60)

win.mainloop()
