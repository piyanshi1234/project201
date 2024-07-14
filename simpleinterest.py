from tkinter import *
window=Tk()

window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i == float(p*r*t)/100
    interest= round(i,2)

    showlabel.destroy()
  
app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

principal_label=Label(window, text="Enter PRINCIPLE", fg = "black", bg = "lightcyan", font=("Calibri", 12))
principal_label.place(x=20, y=140)

principal_entry=Entry(window, text="", bd=2, width=15)
principal_entry.place(x=150, y=142)

rate_label=Label(window, text="Enter rate of interest ", fg = "black", bg = "lightcyan", font=("Calibri", 12))
rate_label.place(x=20, y=185)

rate_entry=Entry(window, text="", bd=2, width=15)
rate_entry.place(x=150, y=187)

time_label=Label(window, text="Enter time ", fg = "black", bg = "lightcyan", font=("Calibri", 12))
time_label.place(x=20, y=185)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=187)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command= calculate_interest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()






































