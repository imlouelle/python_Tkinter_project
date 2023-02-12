import tkinter as tk
from tkinter import messagebox
import os
import openpyxl

window = tk.Tk()
window.title("Inventory by Louelle")
frame = tk.Frame(window)
frame.config(bg='#00425A')
frame.pack()



def enter_data():
    
    if enter_data:
        
        if date_input.get() and name_input and device_input and typeR_input and warranty_input and price_input and partsP_input:
            price = int(price_input.get())
            parts = int(partsP_input.get())
            total = price - parts
            print(total)
            messagebox.showinfo(title ="Notice", message="Data Saved")
        else:
            messagebox.showwarning(message="Please fill in The blanks")
            
        filepath = "C:/Users/PC/Documents/data.xlsx"
 
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            headings = ["Date" , "Name" , "Device" , "Type of Repair" ,"Warranty" ,"Price" ,"PartsPrice" , "Revenue"]
            sheet.append(headings)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([date_input.get(), name_input.get(), device_input.get(), typeR_input.get() ,warranty_input.get(),price_input.get(),partsP_input.get(),total])
        workbook.save(filepath)
         
        

headings = tk.Label(frame,text= "INVENTORY SYSTEM",fg="white",bg='#00425A',font=("arial",15,"bold"))
headings.grid(row= 0 ,column= 0 ,padx= 5 , pady=0)

client_data = tk.LabelFrame(frame , text="Client information", fg= "white")
client_data.grid(row =1 , column= 0 ,padx= 10 , pady=5 )
client_data.config(bg='#00425A')

date_label = tk.Label(client_data, text= "Date:" ,fg="white",bg='#00425A')
date_label.grid(row =0 , column = 0)

date_input = tk.Entry(client_data)
date_input.grid(row =0 , column= 1,padx= 10 , pady=10 )

name_label = tk.Label(client_data, text= "Client Name:",fg="white",bg='#00425A')
name_label.grid(row =1 , column = 0)

name_input = tk.Entry(client_data)
name_input.grid(row =1 , column= 1,padx= 10 , pady=10 )

device_label = tk.Label(client_data, text= "Device:",fg="white",bg='#00425A')
device_label.grid(row =2 , column = 0)

device_input = tk.Entry(client_data )
device_input.grid(row =2 , column= 1,padx= 10 , pady=10 )

typeR_label = tk.Label(client_data , text="Type of Repair:",fg="white",bg='#00425A')
typeR_label.grid(row =3 , column= 0 )

typeR_input = tk.Entry(client_data )
typeR_input.grid(row =3 , column= 1 ,padx= 10 , pady=10 )

warranty_label = tk.Label(client_data , text="Warranty:",fg="white",bg='#00425A')
warranty_label.grid(row =4 , column= 0)

warranty_input = tk.Spinbox(client_data ,from_=0 , to="infinity")
warranty_input.grid(row =4 , column= 1 ,padx= 10 , pady=10 )

price_label = tk.Label(client_data , text="Price of Repair:",fg="white",bg='#00425A')
price_label.grid(row =5 , column= 0)

price_input = tk.Spinbox(client_data ,from_=0 , to="infinity")
price_input.grid(row =5 , column= 1,padx= 10 , pady=10 )

partsP_label = tk.Label(client_data , text="Parts Price:",fg="white",bg='#00425A')
partsP_label.grid(row =6 , column= 0)

partsP_input = tk.Spinbox(client_data ,from_=0 , to=10000)
partsP_input.grid(row =6 , column= 1,padx= 10 , pady=10 )

confirm_button = tk.Button(client_data, text= "Save Data" , command= enter_data,fg="white",bg='#1F8A70')
confirm_button.grid(row =7 , column= 1 , sticky= "news" ,padx= 10 , pady=10 )




window.mainloop()