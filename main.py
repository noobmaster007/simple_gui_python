#python tkinter tutorial
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title('New Window')

#creating font
new_fnt = font.Font(family='consolas', size='11')

#create label
name_label = ttk.Label(root, text='Enter your name: ', font = new_fnt)
name_label.grid(row=0, column=0, sticky=tk.W)

age_label = ttk.Label(root, text = 'Enter your age: ', font = new_fnt)
age_label.grid(row=1, column=0,sticky=tk.W)

email_label = ttk.Label(root, text='Enter your email: ', font=new_fnt)
email_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(root, text='Gender is: ', font = new_fnt)
gender_label.grid(row=3, column=0)
# create entryBox or textBox

name_var = tk.StringVar()
name_entrybox = ttk.Entry(root, width=16, textvar = name_var, font = new_fnt)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

age_var = tk.StringVar()
age_entry = ttk.Entry(root, width = 16, textvar = age_var, font = new_fnt)
age_entry.grid(row=1, column=1)

email_var = tk.StringVar()
email_entry = ttk.Entry(root, width = 16, textvar = email_var, font = new_fnt)
email_entry.grid(row=2, column=1)
#combo Box

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root,width=14, textvar=gender_var, state='readonly', font=new_fnt)
gender_combobox.grid(row=3,column=1)
gender_combobox['value']=('Male','Female','Others')
gender_combobox.current(0)

#radio button
usertype = tk.StringVar()
radiobtn1=ttk.Radiobutton(root, text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=4, column=0)

radiobtn2=ttk.Radiobutton(root, text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column=1)

#check button
checkbtn_var = tk.BooleanVar()
checkbtn = ttk.Checkbutton(root, text='Click if you like my project!', variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=2)

#create button
def keyPress():
    username = name_var.get()
    email = email_var.get()
    age = age_var.get()
    user_gen = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == False:
        subs = 'No'
    else:
        subs = 'Yes'
    
           
    # print ("Username is ",username)
    # print ("Email is ", email)
    # print ("Your age is ", age)
    # print ("Gender is ",user_gen)
    # print ("User type is ", user_type)
    # print ("Subscribed: ",subs)
    
    with open('file.txt','a') as f:
        f.write(f"Username is {username}\nEmail is {email}\nYour age is {age}\nGender is {user_gen}\nUser type is {user_type}\nSubscribed {subs}\n\n")
    f.close()
    
    
    #after submit textbox clear
    name_entrybox.delete(0,tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0,tk.END)
    #small msgbox
    messagebox.showinfo('info','Successfully Submitted!')
    

submit_button = ttk.Button(root, text = 'submit', command = keyPress)
submit_button.grid(row=6, column=0)







root.mainloop()


