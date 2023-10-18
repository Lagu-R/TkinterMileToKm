MILE TO KM Tkinter project
 from tkinter import *
 
 window = Tk()
 window.title("My First GUI Program")
 window.minsize(width=500, height=300)
 window.config(padx=100, pady=100)
 
 
 
 # # entry
 
 input = Entry(width=20)
 input.grid(row=0, column=1)
 
 # miles label
 
 miles = Label(text="Miles", font=("Arial", 24, "bold"))
 miles.grid(row=0, column=2)
 
 
 #label
 
 my_label = Label(text="is equal to", font=("Arial", 24, "bold"))
 my_label.grid(row=3, column=0)
 
 # output text 
 output = Label(text="0", font=("Arial", 24, "bold"))
 output.grid(row=3, column=1)
 
 # Kilometers
 km = Label(text="Km", font=("Arial", 24, "bold"))
 km.grid(row=3, column=2)
 
 
 
 def calc():
     mile = float(input.get())
     miles_to_km = mile * 1.609
     output.config(text=miles_to_km)
 
 button = Button(text="Calculate", width=20, command=calc)
 button.grid(row=4, column=1)
 
 # #button 2 
 
 # button2 = Button(text="Click Me N2", command=button_clicked)
 # button2.grid(row=0, column=2)
 
 
 
 
 
 
 window.mainloop()
