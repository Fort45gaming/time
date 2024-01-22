from tkinter import *
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("600x450")



india_label=Label(root,text="India")
india_label.place(relx=0.2,rely=0.05,anchor=CENTER)

india_clock=Label(root)

india_clock.place(relx=0.2,rely=0.35,anchor=CENTER)

i_t=Label(root)
i_t.place(relx=0.2,rely=0.65,anchor=CENTER)


usa_label=Label(root,text="USA")
usa_label.place(relx=0.7,rely=0.05,anchor=CENTER)

usa_clock=Label(root)
usa_clock.place(relx=0.7,rely=0.35,anchor=CENTER)

u_t=Label(root)
u_t.place(relx=0.7,rely=0.65,anchor=CENTER)

a_label=Label(root,text="Australia")
a_label.place(relx=0.7,rely=0.05,anchor=CENTER)

a_clock=Label(root)
a_clock.place(relx=0.7,rely=0.35,anchor=CENTER)

at=Label(root)
at.place(relx=0.7,rely=0.65,anchor=CENTER)

j_label=Label(root,text="Japan")
j_label.place(relx=0.7,rely=0.05,anchor=CENTER)

j_clock=Label(root)
j_clock.place(relx=0.7,rely=0.35,anchor=CENTER)

j_t=Label(root)
j_t.place(relx=0.7,rely=0.65,anchor=CENTER)


class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        i_t["text"]="time:"+ current_time
        i_t.after(200,self.times)
        
        
        
class Usa():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        u_t["text"]="time:"+ current_time
        u_t.after(200,self.times)

class Australia():
    def times(self):
        home=pytz.timezone('Australia/ACT')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        a_t["text"]="time:"+ current_time
        a_t.after(200,self.times)

class Japan():
    def times(self):
        home=pytz.timezone('Japan')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        j_t["text"]="time:"+ current_time
        j_t.after(200,self.times)


obj_india=India()
obj_usa=Usa()
obj_australia=Australia()
obj_japan=Japan()
india_btn=Button(root,text="Show time",command=obj_india.times)  
india_btn.place(relx=0.2,rely=0.8,anchor=CENTER)

usa_b=Button(root,text="Show time",command=obj_usa.times)
usa_b.place(relx=0.7,rely=0.8,anchor=CENTER)

a_b=Button(root,text="Show time",command=obj_australia.times)
a_b.place(relx=0.25,rely=0.92,anchor=CENTER)

j_b=Button(root,text="Show time",command=obj_usa.times)
j_b.place(relx=0.30,rely=0.92,anchor=CENTER)


root.mainloop()

    