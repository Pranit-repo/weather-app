from tkinter import*
from tkinter import ttk
import requests

def get_data():

 city=city_name.get()
 data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e355fb0cec6fe8bd7293f9b1a0bebe9b").json()

 w_label1.config(text=data["weather"][0]["main"]) 
 wb_label1.config(text=data["weather"][0]["description"]) 
 t_label1.config(text=str(int(data["main"]["temp"]-273.15))) 
 per_label1.config(text=data["main"]["pressure"]) 
 


win=Tk()
win.title("PK TECH")
win.config(bg = "violet")
win.geometry("500x570")
name_label=Label(win,text="PK WEATHER APP",
                 font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
lists=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
"Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
"Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
"Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli",
"Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com=ttk.Combobox(win,text="PK WEATHER APP",values=lists,
                 font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)    #combobox


#1box
w_label=Label(win,text="WEATHER CLIMATE",font=("Time New Roman",14))
w_label.place(x=25,y=260,height=50,width=220)


w_label1=Label(win,text="",font=("Time New Roman",14))
w_label1.place(x=260,y=260,height=50,width=220)

#2nd box
wb_label=Label(win,text="WEATHER\n DESCRIPTION",font=("Time New Roman",14))
wb_label.place(x=25,y=330,height=50,width=220)

wb_label1=Label(win,text="",font=("Time New Roman",14))
wb_label1.place(x=260,y=330,height=50,width=220)

#3rd box
t_label=Label(win,text="Temperature",font=("Time New Roman",17))
t_label.place(x=25,y=400,height=50,width=220)


t_label1=Label(win,text="",font=("Time New Roman",17))
t_label1.place(x=260,y=400,height=50,width=220)

#4th box
per_label=Label(win,text="Pressure", font=("Time New Roman",17))
per_label.place(x=25,y=470,height=50,width=220)

per_label1=Label(win,text="", font=("Time New Roman",17))
per_label1.place(x=260,y=470,height=50,width=220)

btn=Button(win,text="Done",
                 font=("Time New Roman",20,"bold"),command=get_data)
btn.place(y=190,height=50,width=100,x=200)

win.mainloop()