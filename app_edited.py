import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import smtplib
import random 
import math
import os
import time
from tkinter import ttk


usernames=[]
passwords=[]  

otp_list=[]

names=[]
phones=[]
emails=[]

root=Tk()
root.iconbitmap("d:/Python/Contact App/appicon.ico")


#----------------sign up windows variables------------------------------
name_signup=StringVar()
email_signup=StringVar()
password_signup=StringVar()
conpassword_signup=StringVar()
radio_btn1_signup=IntVar()
#----------------New Admin Email variables------------------------------
new_admin_email=StringVar()
new_admin_email_pass=StringVar()

#-----------------------------------------------------------------------

#----------------sending Email variables--------------------------------
admin_email=""
admin_email_pass=""

#-----------------------------------------------------------------------

#----------------log in windows variables-------------------------------
name_login=StringVar()
password_login=StringVar()
#-----------------------------------------------------------------------

#----------------verify Email windows variables-------------------------
otp_entry=StringVar()
#-----------------------------------------------------------------------

#----------------------New contact Window variables---------------------
name_create=StringVar()
phone_create=StringVar()
email_create=StringVar()

#-------------------------Settings/Developer/Administrator variables--------------
admin=StringVar()
adminpass=StringVar()
#---------------------------------------------------------------------------------

#-----------------------Settings/Appearance/Themes variables-----------------------
theme_set_rbtn=IntVar()

bgcolor="#1B2631"
btncolor="#363637"
fontcolor="#A1B9DA"

#----------------------------------------------------------------------------------

#----------------------------------------------------Current Time-------------------------------------------
localtime = time.asctime( time.localtime(time.time()) )
    
#-----------------------------------------------------------------------------------------------------------

#-------------------------------------Sign up--------------------------------------------------------

def sign_up():
    root3=Toplevel()
    root3.title("Sign up")
    root3.iconbitmap("d:/Python/Contact App/appicon.ico")

    
    c2=Canvas(root3, height=450, width=450 ,bg="#148F77" )
    c2.pack()

    f2=LabelFrame(root3, height=400, width=400, bd="4", bg="White" )
    f2.place(x=30, y=30)

    label_name_signup=Label(f2, text="User Name", font="16", bg="White")   #User name(sign up)
    label_email_signup=Label(f2, text="Email", font="16", bg="White")   #Email(sign up)
    label_password_signup=Label(f2, text="Password", font="16", bg="White")    #Password(sign up)
    label_password_signupcond=Label(f2, text="You may use letters,numbers", font="arial 8 italic", bg="White", fg="Grey") #you may use thing.....
    label_conpassword=Label(f2, text="Confirm Password", font="16", bg="White")     #confirm password
    label_radio_btn1=Label(f2, text="I agree to all the conditions and rules", font="arial 10", bg="White")     #Label for
                                                                                                #radio button
    entry_name_signup=Entry(f2, bd="2", textvar=name_signup)
    entry_email_signup=Entry(f2, bd="2", textvar=email_signup)
    entry_password_signup=Entry(f2, bd="2", show="*", textvar=password_signup)
    entry_conpassword_signup=Entry(f2, bd="2", show="*", textvar=conpassword_signup)

    #radio button
    radio_btn1=Radiobutton(f2, bg="White", variable=radio_btn1_signup, value=1, command=agreebtn_checked)
    radio_btn1.place(x=50, y=290)

    #sign up button
    btn_signup=Button(f2, text="Sign up", font="arial 13 bold", bg="#148F77", fg="White", height="1", width="9", command=sign_up_validation)
    btn_signup.place(x=150, y=340)                                                          
    
    label_name_signup.place(x=50, y=70)
    label_email_signup.place(x=50, y=130)
    label_password_signup.place(x=50, y=190)
    label_password_signupcond.place(x=170, y=210)
    label_conpassword.place(x=50, y=250)
    label_radio_btn1.place(x=80, y=290)

    entry_name_signup.place(x=190, y=70)
    entry_email_signup.place(x=190, y=130)
    entry_password_signup.place(x=190, y=190)
    entry_conpassword_signup.place(x=190, y=250)
    
    root3.mainloop()
#-------------------------------------Sign up/Validation Process--------------------------------------------------------
def agreebtn_checked():
    radio_btn1_signup.set(1)
#when clicked the radio button, set to 1

def sign_up_validation():
    
    a=name_signup.get()
    b=password_signup.get()
    c=conpassword_signup.get()
    d=radio_btn1_signup.get()
    
    
    if not c or not b or not a:
        tkinter.messagebox.showerror("Error","All fields should be filled")
    else:
        if b==c:
            if len(b)>=5:
                if d==1:
                    verify_otp()
                else:
                    tkinter.messagebox.showerror("Error","You have to agree to all the conditions and rules")    
            else:
                tkinter.messagebox.showerror("Error","Your Password is too short")    
                      
        else:
        #messagebox giving an error with confirm password 
            tkinter.messagebox.showerror("Error","Confirm Password doesn't match")

#-------------------------------------sending emails----------------------------------------------------------------------
def send_otp():
    h=email_signup.get()

    otp=str(random.randint(1000,10000))
    otp_list.append(otp)         #------------------------Generating OTP 
    print(otp)

    #----------------------Saving sent OTP s with recieved email in OTP.txt file---------------------------------
    f=open("OTP.txt","a")
    f.write(f'\n\n{otp}   to {h}  - {localtime }')
    f.close()
    #------------------------------------------------------------------------------------------------------------
    
    with open("d:/Python/Contact App/Files/admin_email.txt","r") as file:
        line=file.readlines()
        line[-1]=admin_email

    with open("d:/Python/Contact App/Files/admin_email_pass.txt","r") as file:
        linee=file.readlines()
        linee[-1]=admin_email_pass


    subject="Symetry-Verify Account" 
    msg=f'Subject: {subject}\n\nYour OTP is {otp}'
    
    server =smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(admin_email,admin_email_pass)
    print("login ok")
    server.sendmail(admin_email,h ,msg)
    print("sent!!!")

#------------------------------------------------------------------------------------------------------------------------

#--------------------------------------Adding user names and passwords into the relevant files---------------------------
def append_to_files():
    p=name_signup.get()
    q=password_signup.get()

    with open("d:/Python/Contact App/Files/user_names.txt", "a") as file: 
        file.writelines(f'{p}\n')
     
    with open("d:/Python/Contact App/Files/passwords.txt", "a") as file: 
        file.writelines(f'{q}\n')
    
 
#--------------------------------------Adding user names and passwords into the relevant lists---------------------------
    
def append_to_lists():
    with open("d:/Python/Contact App/Files/user_names.txt", "r") as file: 
        data = file.readlines() 
        for line in data: 
            usernames.append(line)

    with open("d:/Python/Contact App/Files/passwords.txt", "r") as file: 
        data = file.readlines() 
        for line in data: 
            passwords.append(line)

    log_in()


#....................................verify button command.......................................#
def verify_sent_otp():
    g=otp_entry.get()

    
    #for i in otp_list:

    print(otp_list[-1])
    print(g)
    if g==otp_list[-1]:
        tkinter.messagebox.showinfo("System","You have successfully created\nan user account")       
        append_to_files()
        append_to_lists()
        log_in()
    else:
        tkinter.messagebox.showerror("Error","Entered OTP is invalid") 

#-------------------------------------Sign up/Verify Email Window--------------------------------------------------------
def verify_otp():
    
    send_otp()
    root6=Toplevel()
    root6.title("Verify Email")
    root6.iconbitmap("d:/Python/Contact App/appicon.ico")

    c4=Canvas(root6, width=370, height=370, bg="#D35400")
    c4.pack()

    f4=LabelFrame(root6, width=280, height=280, bg="White")
    f4.place(x=40, y=40)

    label_otp=Label(f4, text="OTP", bg="White", font="15")
    label_otp.place(x=130,y=70)

    entry_otp=Entry(f4, bg="White", bd="1", textvar=otp_entry)
    entry_otp.place(x=90,y=110)
    
    btn_resend=Button(f4, text="Resend OTP", font=" arial 10 italic", bg="White", height="1", width="12", bd="0", fg="#D35400", command=send_otp)
    btn_resend.place(x=75,y=130)

    btn_verify=Button(f4, text="Verify", font="16", bg="#D35400", fg="White", height="1", width="9", command=verify_sent_otp)
    btn_verify.place(x=100,y=220)

    root6.mainloop()
#--------------------------------------------------------------------------------------------------------

#-------------------------------------Log in--------------------------------------------------------

def log_in():
    root2=Toplevel()
    root2.title("Log in ")
    root2.geometry("450x450")
    root2.iconbitmap("d:/Python/Contact App/appicon.ico")

    c1=Canvas(root2, height=450, width=450 ,bg="#148F77")
    c1.pack()

    f1=LabelFrame(root2, height=400, width=400, bd="4", bg="White" )
    f1.place(x=30, y=30)
    
    #resizing image
    image1=Image.open("d:/Python/Contact App/user.png")
    resized1=image1.resize((120,120), Image.ANTIALIAS)
    newimage1=ImageTk.PhotoImage(resized1)

    #Image
    image1=ImageTk.PhotoImage(file="d:/Python/Contact App/user.png")
    label_image1=Label(root2, image=newimage1, bg="White")
    label_image1.place(x=180, y=90)

    label_name=Label(f1, text="User Name", font="16", bg="White")   #User name(log in)
    label_password=Label(f1, text="Password", font="16", bg="White")    #Password(log in)

    #Add button
    btn_login=Button(f1, text="Log in", font="16", pady=7 ,padx=7, width=7, bg="#148F77", fg="White", command=log_in_validation)
    btn_login.place(x=150, y=340)

    entry_name=Entry(f1, bd="2", textvar=name_login)
    entry_password=Entry(f1, bd="2", show="*", textvar=password_login)

    label_name.place(x=50, y=230)
    label_password.place(x=50, y=280)

    entry_name.place(x=170, y=230)
    entry_password.place(x=170, y=280)

    root2.mainloop()

def log_in_validation():
    e=name_login.get()
    en=f'{e}\n'
    t=password_login.get()
    tn=f'{t}\n'

    for item in usernames:
        if item==en:
            getindex=usernames.index(item)
            if passwords[getindex]==tn:
                append_creates_to_lists()
                
                main_window()
            #else:
            #    tkinter.messagebox.showerror("Error","Invalid Password")
            #    break
                             
        #else:
        #    tkinter.messagebox.showerror("Error","Invalid User Name")            

def append_creates_to_lists():
    with open("d:/Python/Contact App/Files/names.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            if line not in names: 
                names.append(line)
            else:
                pass
        
    with open("d:/Python/Contact App/Files/phones.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            if line not in phones: 
                phones.append(line)
            else:
                pass 
            

    with open("d:/Python/Contact App/Files/emails.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            if line not in emails: 
                emails.append(line)
            else:
                pass 
            
    print(names)
    print(phones)
    print(emails)

    main_window()

#-------------------------------------Main Window--------------------------------------------------------
def main_window():
    root4=Toplevel()
    root4.title("Main Window")
    root4.iconbitmap("d:/Python/Contact App/appicon.ico")

    c7=Canvas(root4, width=870, height=500, bg="#1F618D")
    c7.pack()

    c8=Canvas(root4, width=820, height=460, bg="White")
    c8.place(x=25,y=20)

    c9=Canvas(root4, width=184, height=460, bg="#212F3D")
    c9.place(x=25,y=20)

    btn_home=Button(root4, text="Home", font="arial 16", width=14, bd="0", height=2, bg="#212F3D", fg="#BFC9CA", command=opening_window)
    btn_home.place(x=27,y=22)

    c9.create_line(25,70,160,70, width=7, fill="#424949")

    btn_new=Button(root4, text="New", font="arial 16", width=14, bd="0", height=2, bg="#212F3D", fg="#BFC9CA", command=new_contact)
    btn_new.place(x=27,y=90)

    c9.create_line(25,135,160,135, width=3, fill="#424949")

    btn_delete=Button(root4, text="Delete", font="arial 16", width=14, bd="0", height=2, bg="#212F3D", fg="#BFC9CA")
    btn_delete.place(x=27,y=158)

    c9.create_line(25,200,160,200, width=6, fill="#424949")

    btn_settings=Button(root4, text="Settings", font="arial 16", width=14, bd="0", height=2, bg="#212F3D", fg="#BFC9CA", command=settings_before)
    btn_settings.place(x=27,y=226)

    c9.create_line(25,270,160,270, width=3, fill="#424949")

    btn_quit=Button(root4, text="Quit", font="arial 16", width=14, bd="0", height=2, bg="#212F3D", fg="#BFC9CA", command=root4.destroy)
    btn_quit.place(x=27,y=294)

    c9.create_line(25,337,160,337, width=4, fill="#424949")

    entry_search=Entry(root4, width=80, bd="2")
    entry_search.place(x=280,y=120)

    #---------------------------------Search Button-------------------------------------------------
    v=Image.open("d:/Python/Contact App/search.png")
    resizedv=v.resize((20,20), Image.ANTIALIAS)
    newv=ImageTk.PhotoImage(resizedv)

    btn_search=PhotoImage(file="d:/Python/Contact App/search.png")
    btn_search=Button(root4, image=newv, bg="White", bd=0)
    btn_search.place(x=768 , y=118)
    #-----------------------------------------------------------------------------------------------
    
    v1=Image.open("d:/Python/Contact App/user2.png")
    resizedv1=v1.resize((50,50), Image.ANTIALIAS)
    newv1=ImageTk.PhotoImage(resizedv1)

    label_user=Label(root4, image=newv1, bg="White")
    label_user.place(x=280, y=50)

    e=name_login.get()
    label_status=Label(root4, text=f'Hi {e}', font="arial 14", bg="White", fg="Black")
    label_status.place(x=340,y=60)

    #named_tuple = time.localtime() # get struct_time
    #time_string = time.strftime("%H:%M:%S", named_tuple)

    #label_time=Label(root4, text=localtime, font="arial 14", bg="White")
    #label_time.place(x=600,y=30)

#----------------------------------------------------------------------------------------------------------------------
        
    #-----------------------------Table------------------------------------------------
    tree=ttk.Treeview(root4)
    tree['columns']=("Name","Phone","Email")

    tree.column("#0",stretch=NO,width=0)
    tree.column("Name",width="180", anchor=CENTER)
    tree.column("Phone",width="100", anchor=CENTER)
    tree.column("Email",width="204", anchor=CENTER)

    tree.heading("#0", text="")
    tree.heading("Name", text="Name")
    tree.heading("Phone", text="Phone")
    tree.heading("Email", text="Email")

    #combining elements in names,phones,emails lists into one list with tuples!!!
    zipped=list(zip(names,phones,emails))
    
    for record in zipped:
        tree.insert(parent="", index="end", text="",values=(record[0],record[1],record[2]))
        

    tree.place(x=280,y=200)
    #-----------------------------------------------------------------------------------

    root4.mainloop()


def change_admin_email():
    a=new_admin_email.get()
    b=new_admin_email_pass.get()
    with open("d:/Python/Contact App/Files/admin_email.txt", "a") as file:
        file.writelines(f'{a}\n')

    with open("d:/Python/Contact App/Files/admin_email_pass.txt", "a") as file:
        file.writelines(f'{b}\n')



#-------------------------------------------------------------------------------------------------------- 

def settings_before():
    settings(bgcolor,btncolor,fontcolor)

#-----------------------------------------Settings Window--------------------------------------------------------------
def rbtn_checked():
    k=theme_set_rbtn.get()
    
    if k==1:
        bgcolor="#03A325"
        btncolor="#A0F53A"
        fontcolor="#4D5445"
        settings(bgcolor,btncolor,fontcolor)
    elif k==2:
        bgcolor="#004033"
        btncolor="#097E67"
        fontcolor="#19302B"
        settings(bgcolor,btncolor,fontcolor)

def settings(bgcolor,btncolor,fontcolor):

    def appearance():
        c3=Canvas(root8, width=478  ,height=380, bg="White")
        c3.place(x=220,y=0)

        label_1=Label(c3, text="Cutomize the way you see", font="arial 22", bg="White", width=80, anchor=W)   #Topic - Appearance
        label_1.place(x=20,y=5)

        label_2=Label(c3, text="Themes", font="arial 14", bg="White")       #Sub topic - Themes 
        label_2.place(x=20,y=70)

        radio_btn1=Radiobutton(c3, bg="White", variable=theme_set_rbtn, value=1, command=rbtn_checked)          #Radio btn for Themes set 1
        radio_btn1.place(x=50, y=120)

        label_3=Label(c3, text="Theme set 1", font="arial 12", bg="White")       #label for Theme set 1 
        label_3.place(x=80,y=120)
        #------------------------------------------------------
        radio_btn2=Radiobutton(c3, bg="White", variable=theme_set_rbtn, value=2, command=rbtn_checked)          #Radio btn for Themes set 2
        radio_btn2.place(x=50, y=150)

        label_4=Label(c3, text="Theme set 2", font="arial 12", bg="White")       #label for Theme set 2 
        label_4.place(x=80,y=150)


    def dev():
        c4=Canvas(root8, width=478  ,height=380, bg="White")
        c4.place(x=220,y=0)

        label_1=Label(c4, text="Developer Options",  font="arial 22", bg="White")
        label_1.place(x=20,y=5)

        label_2=Label(c4, text="You have to log in as administrator for further more access\n Only the developer can access this option.\nFurther more info- tharindahp@gmail.com", 
                             font="arial 11", bg="White", fg="Red")
        label_2.place(x=20,y=70)

        label_3=Label(c4, text="Administrator",  font="arial 11", bg="White")   #Administrator
        label_3.place(x=20,y=160)

        label_4=Label(c4, text="Password",  font="arial 11", bg="White")        #Password
        label_4.place(x=20,y=200)

        entry_1=Entry(c4, bg="White", bd=1, width=29, textvar=admin)
        entry_1.place(x=150,y=165) 

        entry_2=Entry(c4, bg="White", bd=1, width=29, show="*", textvar=adminpass)
        entry_2.place(x=150,y=205) 

        btn=Button(c4, text="log in", bd=1, bg="white", width=10, command=admin_check)
        btn.place(x=150, y=240)

    #----------------------------checking validation of entered info--------------------------------------------------------
    def admin_check():
        m=admin.get()
        n=adminpass.get()

        if not m or not n:
            tkinter.messagebox.showerror("Error","No empty fields can be exist")
        else:
            if m=="Tharinda":
                if n=="symetry":
                    tkinter.messagebox.showinfo("System","Successfully Entered")
                    admin_log_in()
                else:
                    tkinter.messagebox.showerror("Error","Invalid Password")
            else:
                tkinter.messagebox.showerror("Error","Invalid Admin")

    
    #--------------Change Admin Email(with password) to a new one-----------------------------------------------------------
    def admin_log_in():
        c5=Canvas(root8, width=478  ,height=380, bg="White")
        c5.place(x=220,y=0)

        label_0=Label(c5, text="This will also change the sender's Email address \nof generated OTP s and the reciever will see your new email address."
                        ,font="arial 11", fg="Red", bg="White")
        label_0.place(x=20,y=70)

        label_1=Label(c5, text="Change Administrator Email", font="arial 14", bg="White")
        label_1.place(x=20,y=20)

        label_2=Label(c5, text="New Admin Email",  font="arial 11", bg="White")   #New Admin Email
        label_2.place(x=20,y=160)

        label_3=Label(c5, text="Email Password",  font="arial 11", bg="White")    #Email Password
        label_3.place(x=20,y=200)

        label_3_con=Label(c5, text="Enter the original Email password",  font="arial 8 italic", bg="White", fg="Gray") 
        label_3_con.place(x=150,y=225)

        entry_4=Entry(c5, bg="White", bd=1, width=29, textvar=new_admin_email)
        entry_4.place(x=150,y=165) 

        entry_5=Entry(c5, bg="White", bd=1, width=29, show="*", textvar=new_admin_email_pass)
        entry_5.place(x=150,y=205) 

        btn=Button(c5, text="Apply", bd=1, bg="white", width=10, command=change_admin_email)
        btn.place(x=150, y=250)


    def about():
        c3=Canvas(root8, width=478  ,height=380, bg="White")
        c3.place(x=220,y=0)

        label_1=Label(c3, text="Info",  font="arial 18 bold", bg="White", fg="Black") 
        label_1.place(x=20,y=20)

        label_2=Label(c3, text="Release Date: 2020.12.04\nVersion: 1.0.0\nLicense: Freeware\nCompany: Symetry\nPublisher: Symetry",  font="arial 11", bg="White", fg="Black") 
        label_2.place(x=20,y=70)

        label_3=Label(c3, text="Credits",  font="arial 18 bold", bg="White", fg="Black") 
        label_3.place(x=20,y=180)

        label_4=Label(c3, text="Platinum Thanks: Gihan Ayya\n(Thanks million times for giving me the tip for consider about\nfile handling  for create a database.Huge success!)",  font="arial 11", bg="White", fg="Black") 
        label_4.place(x=20,y=220)

        label_5=Label(c3, text="Golden Thanks: #codemy , #thenewboston, #Mosh, #Telusco\n(Youtube Channels)",  font="arial 11", bg="White", fg="Black") 
        label_5.place(x=20,y=290)

        label_6=Label(c3, text="Extra Platinum Thanks: Hp notebook 430(My Laptop)",  font="arial 11", bg="White", fg="Black") 
        label_6.place(x=20,y=340)



    root8=Toplevel()
    root8.title("Settings")
    root8.iconbitmap("d:/Python/Contact App/appicon.ico")

    c1=Canvas(root8, width=700  ,height=380, bg=bgcolor)     #By default "#1B2631" color
    c1.pack()

    c2=Canvas(root8, width=214  ,height=380, bg=bgcolor)   #By default "#1B2631" color
    c2.place(x=0,y=0)

    btn_appearance=Button(root8, text="Appearance",font="arial 17", width=16, height=2, bd=0
                                                  , command=appearance,fg=fontcolor, bg=btncolor)
    btn_appearance.place(x=2,y=0)

    btn_dev=Button(root8, text="Developer",font="arial 17", width=16, height=2, bd=0
                                                  , command=dev, fg=fontcolor, bg=btncolor)
    btn_dev.place(x=2,y=70)

    btn_about=Button(root8, text="About",font="arial 17", width=16, height=2, bd=0
                                                  , command=about, fg=fontcolor, bg=btncolor)
    btn_about.place(x=2,y=140)

    
    
    
    root8.mainloop()
    
  
#----------------------------------------------------------------------------------------------------------------------



#-------------------------------------Create New Contact Window--------------------------------------------------------
    
def new_contact():
    root7=Toplevel()
    root7.title("New Contact")
    root7.iconbitmap("d:/Python/Contact App/appicon.ico")


    c5=Canvas(root7, width=480, height=390, bg="#D35400")
    c5.pack(fill=BOTH)

    c6=Canvas(root7, width=400, height=320, bg="White")
    c6.place(x=40, y=40)

    label_name_create=Label(root7, text="Name", bg="White", font="arial 12") #Contact Name
    label_phone_create=Label(root7, text="Phone", bg="White", font="arial 12") #Phone Number
    label_email_create=Label(root7, text="Email", bg="White", font="arial 12") #Email

    entry_name_create=Entry(root7, bg="White", width="40", bd="0", textvar=name_create) 
    entry_phone_create=Entry(root7, bg="White", width="40", bd="0", textvar=phone_create) 
    entry_email_create=Entry(root7, bg="White", width="40", bd="0", textvar=email_create) 

    c6.create_line(60,80,300,80)
    c6.create_line(60,160,300,160)
    c6.create_line(60,230,300,230)

    btn_create_create=Button(root7, text="Create", font="arial 15 bold", bg="#D35400", fg="White", bd="0", command=append_creates_to_files)
    btn_reset_create=Button(root7, text="Reset", font="arial 15 bold", bg="#D35400", fg="White", width="6", bd="0", command=reset)


    label_name_create.place(x=98,y=70)
    label_phone_create.place(x=98,y=150)
    label_email_create.place(x=98,y=220)

    entry_name_create.place(x=98,y=100)
    entry_phone_create.place(x=98,y=180)
    entry_email_create.place(x=98,y=250)

    btn_create_create.place(x=120,y=310)
    btn_reset_create.place(x=270,y=310)

    root7.mainloop()

def reset():
    name_create.set("")
    phone_create.set("")
    email_create.set("")


def append_creates_to_files():
    u=name_create.get()
    v=phone_create.get()
    w=email_create.get()

    with open("d:/Python/Contact App/Files/names.txt", "a") as file: 
        file.writelines(f'{u}\n')

    with open("d:/Python/Contact App/Files/phones.txt", "a") as file: 
        file.writelines(f'{v}\n')

    with open("d:/Python/Contact App/Files/emails.txt", "a") as file: 
        file.writelines(f'{w}\n')

    append_creates_to_lists()

#-------------------------------------Opening Window--------------------------------------------------------
def opening_window():
    root5=Toplevel()
    root5.title("Opening Window")
    root5.iconbitmap("d:/Python/Contact App/appicon.ico")

    c3=Canvas(root5, width=800, height=300, bg="#424949")
    c3.pack()

    f3=LabelFrame(root5, width=650, height=200, bg="#CACFD2", bd=0, highlightbackground="Black")
    f3.place(x=80, y=45)

    image2=Image.open("d:/Python/Contact App/login.png")
    resized2=image2.resize((90,90), Image.ANTIALIAS)
    newimage2=ImageTk.PhotoImage(resized2)
    #Changing original image size

    button_image2=PhotoImage(file="d:/Python/Contact App/login.png")   #log in button
    button_login=Button(f3, image=newimage2, command=append_to_lists, bg="#CACFD2", bd=0)
    button_login.place(x=60 , y=47)

    lbl_1=Label(f3, text="Log in", font="arial 14", bg="#CACFD2")
    lbl_1.place(x=85, y=134)    
    
    image3=Image.open("d:/Python/Contact App/signup.png")
    resized3=image3.resize((90,90), Image.ANTIALIAS)
    newimage3=ImageTk.PhotoImage(resized3)
    #Changing original image size

    button_image3=PhotoImage(file="d:/Python/Contact App/signup.png")   #sign up button
    button_signup=Button(f3, image=newimage3, command=sign_up, bg="#CACFD2", bd=0)
    button_signup.place(x=274 , y=47)

    lbl_2=Label(f3, text="Sign up", font="arial 14", bg="#CACFD2")
    lbl_2.place(x=274, y=137)  
       
    image4=Image.open("d:/Python/Contact App/exit.png")
    resized4=image4.resize((90,90), Image.ANTIALIAS)
    newimage4=ImageTk.PhotoImage(resized4)
    #Changing original image size

    button_image4=PhotoImage(file="d:/Python/Contact App/exit.png")   #Exit button
    button_exit=Button(f3, image=newimage4, command=root5.destroy, bg="#CACFD2", bd=0)
    button_exit.place(x=483 , y=47)
    
    lbl_3=Label(f3, text="Exit", font="arial 14", bg="#CACFD2")
    lbl_3.place(x=508, y=140)  

    root5.mainloop()
#---------------------------------------------------------------------------------------------------
#main_window()
opening_window()

root.mainloop()