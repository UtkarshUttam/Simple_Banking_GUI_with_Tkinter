import random
import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime

def move():   
    if message.winfo_x() + message.move >= message.x_limit or message.winfo_x() + message.move < 0:
        message.move = -message.move
    message.place(x=message.winfo_x() + message.move)
    message.after(message.delay, move)
def move1():   
    if message1.winfo_x() + message1.move1 >= message1.x_limit or message1.winfo_x() + message1.move1 < 0:
        message1.move1 = -message1.move1
    message1.place(x=message1.winfo_x() + message1.move1)
    message1.after(message1.delay, move1)
def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

'''(BACKEND) Most important and hardest part of the program.
This is basically combination of debit process and credit process but with different accounts which makes it the hardest part of the program.'''
def transfer(master,amt,accnt1,accnt2,name1,name2):
    fdet1=open(accnt1+".txt",'r')
    pin1=fdet1.readline()
    camt=int(fdet1.readline())
    fdet1.close()
    if(int(amt)>camt):
        messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
    else:
        amti1=int(amt)
        cb=camt-amti1
        fdet1=open(accnt1+".txt",'w')
        fdet1.write(pin1)
        fdet1.write(str(cb)+"\n")
        fdet1.write(accnt1+"\n")
        fdet1.write(name1+"\n")
        fdet1.close()
        frec1=open(str(accnt1)+"-rec.txt",'a+')
        frec1.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti1)+"              "+str(cb)+"\n")
        frec1.close()

        fdet2=open(accnt2+".txt",'r')
        pin2=fdet2.readline()
        damt=int(fdet2.readline())
        fdet2.close()
        amti2=int(amt)
        cab=amti2+damt
        fdet2=open(accnt2+".txt",'w')
        fdet2.write(pin2)
        fdet2.write(str(cab)+"\n")
        fdet2.write(accnt2+"\n")
        fdet2.write(name2+"\n")
        fdet2.close()
        frec2=open(str(accnt2)+"-rec.txt",'a+')
        frec2.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti2)+"              "+str(cab)+"\n")
        frec2.close()
        messagebox.showinfo("Operation Successfull!!","Amount Transfered Successfully!!")
        master.destroy()
        return

#(BACKEND) (Exception Handling) Checks for the account number entered is correct or not.
def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return

#This provides the option to return to the homepage
def home_return(master):
	master.destroy()
	MainMenu()

#(BACKEND) This is a file handling process, used to store the data
def write(master,name,oc,pin):
    if( (is_number(name)) or (is_number(oc)== 0) or (is_number(pin)==0)or name==""):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return
    x = random.randint(1,11) 
    f1=open("Accnt_Record.txt",'r')
    accnt_no=int(f1.readline())
    accnt_no+=x
    f1.close()

    f1=open("Accnt_Record.txt",'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet=open(str(accnt_no)+".txt","w")
    fdet.write(pin+"\n")
    fdet.write(oc+"\n")
    fdet.write(str(accnt_no)+"\n")
    fdet.write(name+"\n")
    fdet.close()
    frec=open(str(accnt_no)+"-rec.txt",'w')
    frec.write("Date                             Credit      Debit     Balance\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
    frec.close()	
    messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
    master.destroy()
    return

#(BACKEND) Credit Processing Function: this function credits the amount from balance and stores the final balance
def crdt_write(master,amt,accnt,name):
    if(is_number(amt)==0):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return
    if(amt=='0' or amt <='0'):
        messagebox.showinfo('!!!Alert!!!','Please enter correct value!!!!!')
        master.destroy()
        return
    else:
        fdet=open(accnt+".txt",'r')
        pin=fdet.readline()
        camt=int(fdet.readline())
        fdet.close()
        amti=int(amt)
        cb=amti+camt
        fdet=open(accnt+".txt",'w')
        fdet.write(pin)
        fdet.write(str(cb)+"\n")
        fdet.write(accnt+"\n")
        fdet.write(name+"\n")
        fdet.close()
        frec=open(str(accnt)+"-rec.txt",'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
        frec.close()
        messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
        master.destroy()
        return

#(BACKEND) Debit Processing Function: this function debits the amount from balance and stores the final balance
def debit_write(master,amt,accnt,name):
    if(is_number(amt)==0):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return
    if(amt == '0' or amt <='0'):
        messagebox.showinfo('Invalid input!!','Please enter correct value!!!!!')
        master.destroy()
        return
    else:
        fdet=open(accnt+".txt",'r')
        pin=fdet.readline()
        camt=int(fdet.readline())
        fdet.close()
        if(int(amt)>camt):
            messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
        else:
            amti=int(amt)
            cb=camt-amti
            fdet=open(accnt+".txt",'w')
            fdet.write(pin)
            fdet.write(str(cb)+"\n")
            fdet.write(accnt+"\n")
            fdet.write(name+"\n")
            fdet.close()
            frec=open(str(accnt)+"-rec.txt",'a+')
            frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
            frec.close()
            messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
            master.destroy()
            return

#This function input values for crediting process and call the credit processing function.
def Cr_Amt(accnt,name):
	creditwn=tk.Tk()
	creditwn.geometry("1920x1080")
	creditwn.title("Credit Amount")
	creditwn.configure(bg="light blue")
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(creditwn,text="_______ BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(creditwn,relief="raised",text="Enter Amount to be credited: ")
	e1=tk.Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(creditwn,text="Credit",relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
	b.pack(side="top")
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))

#This function input values for transferring process and calls transfer processing function	
def Transfer_Amt(accnt,name):
    trnsfrwn=tk.Tk()
    trnsfrwn.geometry("1920x1080")
    trnsfrwn.title('Transfer Amount')
    trnsfrwn.configure(bg="green")
    fr1=tk.Frame(trnsfrwn,bg="blue")
    l_title=tk.Message(trnsfrwn,text="______ BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(trnsfrwn,relief="raised",text="Enter Amount to be transfered: ")
    e1=tk.Entry(trnsfrwn,relief="raised")
    l2=tk.Label(trnsfrwn,relief='raised',text='Enter Account Number of the recipient: ')
    e2=tk.Entry(trnsfrwn,relief='raised')
    l3=tk.Label(trnsfrwn,relief='raised',text='Enter the name of the recipient: ')
    e3=tk.Entry(trnsfrwn,relief='raised')
    l1.pack(side="top")
    e1.pack(side="top")
    l2.pack(side="top")
    e2.pack(side="top")
    l3.pack(side="top")
    e3.pack(side="top")
    b=tk.Button(trnsfrwn,text="Transfer",relief="raised",command=lambda:transfer(trnsfrwn,e1.get(),accnt,e2.get(),name,e3.get()))
    b.pack(side="top")
    trnsfrwn.bind("<Return>",lambda x:transfer(trnsfrwn,e1.get(),accnt,e2.get(),name,e3.get()))

#This function inputs values for the debiting process and call the debit processing function    
def De_Amt(accnt,name):
	debitwn=tk.Tk()
	debitwn.geometry("1920x1080")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg="crimson")
	fr1=tk.Frame(debitwn,bg="blue")
	l_title=tk.Message(debitwn,text="______ BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(debitwn,relief="raised",text="Enter Amount to be debited: ")
	e1=tk.Entry(debitwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(debitwn,text="Debit",relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
	b.pack(side="top")
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))

#this defines to display the balance of  the logge in account
def disp_bal(accnt):
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",(bal))

#this defines the transaction history profile of the user logged in 	
def disp_tr_hist(accnt):
	disp_wn=tk.Tk()
	disp_wn.geometry("1920x1080")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="orange")
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="_____ BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=2000,bg="black",fg="white",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
		l.pack(side="top")
	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

#this function defines the menu for logged in users.	
def logged_in_menu(accnt,name):
    def move():#this function defines the marquee movement which will be called in the function later.
        if message.winfo_x() + message.move >= message.x_limit or message.winfo_x() + message.move < 0:
            message.move = -message.move
        message.place(x=message.winfo_x() + message.move)
        message.after(message.delay, move)
    rootwn=tk.Tk()
    rootwn.geometry("1920x1080")
    rootwn.title("______ BANK-"+name)
    rootwn.configure(background='peru')
    fr1=tk.Frame(rootwn)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file ="26.png")
    x = tk.Label (image = bg_image)
    x.place(y=0,x=0)
    l_title=tk.Message(rootwn,text=" MENU ",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    label=tk.Label(text="Logged in as: "+name,relief="raised",bg="black",fg="white",anchor="center",justify="center")
    label.pack(side="top")
    img2=tk.PhotoImage(file="credit.png")
    myimg2=img2.subsample(1,1)
    img3=tk.PhotoImage(file="debit.png")
    myimg3=img3.subsample(1,1)
    img4=tk.PhotoImage(file="balance.png")
    myimg4=img4.subsample(1,1)
    img5=tk.PhotoImage(file="history.png")
    myimg5=img5.subsample(1,1)
    img6=tk.PhotoImage(file='transfer.png')
    myimg6=img6.subsample(1,1)
    b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
    b2.image=myimg2
    b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
    b3.image=myimg3
    b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
    b4.image=myimg4
    b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
    b5.image=myimg5
    b6=tk.Button(image=myimg6,command=lambda: Transfer_Amt(accnt,name))
    b6.image=myimg6    
    img7=tk.PhotoImage(file="logout.png")
    myimg7=img7.subsample(1,1)
    b7=tk.Button(image=myimg7,relief="raised",command=lambda: logout(rootwn))
    b7.image=myimg7	
    b2.place(x=100,y=220)
    b3.place(x=100,y=370)
    b4.place(x=100,y=550)
    b5.place(x=980,y=220)
    b6.place(x=980,y=370)
    b7.place(x=980,y=550)    
    message=tk.Label(rootwn,text="Welcome back Mr./Mrs."+name)
    message.config(fg='white',bg='black', font=('times','20'))
    message.x_limit = 2000
    message.move = 1
    message.delay = 10
    message.place(x=0)
    message.after(10,move)
    rootwn.mainloop()

#to display a message after logging out
def logout(master):	
	messagebox.showinfo("Logged Out","Have A Nice Day :) !")
	master.destroy()
	MainMenu()
	return
    
#this checks login credentials
def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		MainMenu()
		return
	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		MainMenu()
	else:
		master.destroy()
		logged_in_menu(acc_num,name)
		
#This function defines the login page		
def log_in(master):
	master.destroy()
	loginwn=tk.Tk()
	loginwn.geometry("1920x1080")
	loginwn.title("Log in")
	loginwn.configure(background='white')
	fr1=tk.Frame(loginwn)
	fr1.pack(side="top")
	bg_image = tk.PhotoImage(file = "19.png")
	x = tk.Label(loginwn,image = bg_image)
	x.place(y=-200,x=0)
	l_title=tk.Message(loginwn,text="______ BANK",relief="raised",width=2000,padx=600,pady=50,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(loginwn,text="Enter Name:",fg= "black",relief="raised")
	l1.pack(side="top",ipady=5)
	e1=tk.Entry(loginwn)
	e1.place(width=150,height=50)
	e1.pack(side="top")
	l2=tk.Label(loginwn,text="Enter account number:",relief="raised")
	l2.pack(side="top",ipady=5)
	e2=tk.Entry(loginwn,show="#")
	e2.pack(side="top")
	l3=tk.Label(loginwn,text="Enter your PIN:",relief="raised")
	l3.pack(side="top",ipady=5)
	e3=tk.Entry(loginwn,show="*")
	e3.pack(side="top")
	b=tk.Button(loginwn,text="Submit",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	b1=tk.Button(text="HOME",relief="raised",bg="black",fg="white",command=lambda: home_return(loginwn))
	b1.pack(side="top")
	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	loginwn.mainloop()
#This function defines the program to create a new account as well as providing a account number 	
def Create():
    crwn=tk.Tk()
    crwn.geometry("1920x1080")
    crwn.title("Create Account")
    crwn.configure(bg="#FFE873")
    fr1=tk.Frame(crwn,bg="blue")
    l_title=tk.Message(crwn,text="_____ BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(crwn,text="Enter Name:",relief="raised")
    l1.pack(side="top")
    e1=tk.Entry(crwn)
    e1.pack(side="top")
    l2=tk.Label(crwn,text="Enter opening credit:",relief="raised")
    l2.pack(side="top")
    e2=tk.Entry(crwn)
    e2.pack(side="top")
    l3=tk.Label(crwn,text="Enter desired PIN:",relief="raised")
    l3.pack(side="top")
    e3=tk.Entry(crwn,show="*")
    e3.pack(side="top")
    b=tk.Button(crwn,text="Submit",command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b.pack(side="top")
    crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    crwn.mainloop()
    return

#This is the menu which will display after logging in 
def MainMenu():
    def move():
        if message.winfo_x() + message.move >= message.x_limit or message.winfo_x() + message.move < 0:
            message.move = -message.move
        message.place(x=message.winfo_x() + message.move)
        message.after(message.delay, move)
    try:
        root.destroy()
    except:
        return
    rootwn=tk.Tk()
    rootwn.geometry("1920x1080")
    rootwn.title("_____ BANK")
    rootwn.configure(background='black')
    fr1=tk.Frame(rootwn)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file ="21.png")
    x = tk.Label (image = bg_image)
    x.place(x=-50,y=-340)
    l_title=tk.Message(text="WELCOME TO THE  BANK _____",relief="raised",width=2000,padx=600,pady=50,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")    
    imglo=tk.PhotoImage(file="login.png")    
    imglog=imglo.subsample(1,1)   
    b1=tk.Button(image=imglog,command=lambda: log_in(rootwn))
    b1.image=imglog
    img6=tk.PhotoImage(file="quit.png")
    myimg6=img6.subsample(1,1)
    b2=tk.Button(image=myimg6,command=rootwn.destroy)
    b2.image=myimg6    
    b1.place(x=200,y=345)	
    b2.place(x=1000,y=345)
    message=tk.Button(text="New Here??  Don't worry, Just click here",command=Create)
    message.config(fg='blue',bg='white', font=('times','20'))
    message.x_limit = 950
    message.move = 1
    message.delay = 10
    message.place(x=0,y=125)
    message.after(10,move)
    rootwn.mainloop()
#From here the introductory page begins    
root=tk.Tk()
root.title("Intro")
root.geometry("1920x1080")
root.configure(bg='white')
fr1=tk.Frame(root,bg='white')
fr1.pack(side="left",expand=1)
a=tk.PhotoImage(file="23.png")
tk.Label(fr1,image=a).pack()
fr2=tk.Frame(root,bg='white')
fr2.pack(side="left",expand=1)
tk.Label(fr2,text='created and presented to you by:',font=("Bauhaus 93",14),compound="center",fg="red",bg="white").pack()
tk.Label(fr2,text="Your Name",font=("algerian",34),fg="Black",compound="center",bg="white").pack()
message = tk.Label(root, text = 'WELCOME TO THE BANK _____ !')#write your bank's name at _____
message.config(fg = 'black',bg="white", font=('times','45'))
message.x_limit = 1000
message.move = 1
message.delay = 10
message.place(x=0,y=0)
message.after(10, move)
message1=tk.Label(root,text= 'For your feedbacks, complains, and suggestions please email us at your_email@email.com.')#your email for better feedback
message1.config(fg = 'navy',bg="white", font=('times','15'))
message1.x_limit = 1000
message1.move1 = 1
message1.delay = 10
message1.place(x=0,y=750)
message1.after(10, move1)
tk.Button(fr2,text="Proceed",compound="center",bg="Yellow",font=("algerian"),fg="blue",command=MainMenu).pack()
root.mainloop()

