#TO--DO--LIST

from tkinter import*
import tkinter .messagebox

def input():
    input1=entry1.get()
    if input1=="":
        tkinter.messagebox.showwarning("invalid entry!!")
    else:
        list_box.insert(END,input1)
        entry1.delete(END,0)
        
    
def delete():
    value=list_box.curselection()
    if value:
        list_box.delete(value)
    else:
        tkinter.messagebox.showwarning(title="Please select a task!!")
    
    

    
win=Tk()
win.configure(bg="beige")
win.title("TO-DO-LIST")
win.geometry("250x300")




entry1=Entry(win,text=" ",font=('aeril','20','bold'),bg='grey',relief='ridge',bd='20')

entry1.grid(row=0,column=2,pady=10)

submit=Button(win,text="ADD Task",font=("aeril","20","bold"),fg="white",bg="brown",padx='15',pady='15',command=input)
submit.grid(row=1,column=2,padx=2,pady=8,ipadx=5,ipady=5)

list_box=Listbox(win,bg='grey',relief='ridge',bd='20',font="aeril")
list_box.grid(row=2,column=2,ipadx='10',ipady='50')

delete1=Button(win,text="Marked done",font=("aeril","20","bold"),fg="white", bg="brown",padx="10",pady="10",command=delete)
delete1.grid(row=3,column=2,padx=5,pady=5,ipadx=10,ipady=10)


exit=Button(win,text="exit",font=("aeril","20","bold"),fg="white",bg="brown",command=exit)
exit.grid(row=4,column=2,ipadx=20,ipady=20)


win.mainloop()
    

