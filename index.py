from tkinter import *
import tkinter.messagebox as msg 

root=Tk()
root.geometry("1366x768+0+0")
root.config(bg="#0969da")
root.state("zoomed")


check1=IntVar()
check2=IntVar()
check3=IntVar()
lbName=StringVar()


def check():
    ans=entry.get()
    msg.showinfo("hello",ans)

    if check1.get()==1:
        msg.showinfo("Hello","you pressed c++")
    elif check2.get()==1:
        msg.showinfo("Hello","you pressed java")
    elif check3.get()==1:
        msg.showinfo("Hello","you pressed python")
    elif  check1.get()==0 or check2.get()==0 or check3.get()==0:
        msg.showerror("Error in Input","Please Check Button") 
    else:
       pass 

lbName=Label(root,text="Enter Name",bg="#0969da",font=("calibri",16))
entry=Entry(root,font=("calibri",16))
checkbtn1=Checkbutton(root,text="c++",variable=check1,onvalue=1,offvalue=0,height=5,width=10,bg="#0969da",font=("calibri",16))
checkbtn2=Checkbutton(root,text="java",variable=check2,onvalue=1,offvalue=0,height=5,width=10,bg="#0969da",font=("calibri",16))
checkbtn3=Checkbutton(root,text="python",variable=check3,onvalue=1,offvalue=0,height=5,width=10,bg="#0969da",font=("calibri",16))
btn=Button(root,text="Click",command=check,width=20,font=("calibri",14))

lbName.pack(side=LEFT,fill=X)
entry.pack(side=LEFT,fill=X)

checkbtn1.pack(side=LEFT,fill=X)
checkbtn2.pack(side=LEFT,fill=X)
checkbtn3.pack(side=LEFT,fill=X)

btn.pack(side=LEFT,fill=X)

root.mainloop() 
