




            #tkinter.messagebox.showinfo("Error","Invalid User Name")
            

    
  #Unwant part  
    
    #for i in usernames:
    #    if i==e:
    #        getuserindex=usernames.index(i)
    #        if passwords[getuserindex]==f:
    #            main_window()  #function name to enter the main window
    #        else:
    #            tkinter.messagebox.showinfo("Error","Invalid Password")
                
    #    else:
    #        tkinter.messagebox.showinfo("Error","Invalid User name")







    

    



    
    



        

    

   
#log_in()
#sign_up()
#opening_window()
#verify_otp()
#new_contact()
#main_window()
#settings(bgcolor,btncolor,fontcolor)


#........................Have to solve the otp problem
#                         !!!!!!!!!!!SOLVED!!!!!!!!!!..............................
from tkinter import *
from tkinter import ttk


root4=Tk()

names=["Tharinda","Prabhath"]
phones=["071","077"]
emails=["hello@","Hi@"]

tree=ttk.Treeview(root4)
tree['columns']=("Name","Phone","Email")

tree.column("#0",stretch=NO,width=0)
tree.column("Name",width="180", anchor=CENTER)
tree.column("Phone",width="100")
tree.column("Email",width="204", anchor=CENTER)

tree.heading("#0", text="")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")


zipped=list(zip(names,phones,emails))
print(zipped)

for i in zipped:
    if i=='Prabhath':
        print("Yes")

for record in zipped:
    tree.insert(parent="", index="end", text="Name",values=(record[0],record[1],record[2]))

tree.pack()

root4.mainloop()