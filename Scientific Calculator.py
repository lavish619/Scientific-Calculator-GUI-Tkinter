import tkinter.font
from tkinter import *
import math

def clearall():
    global expression
    global equation
    global value
    global ans
    expression=''
    value=''
    ans=''
    equation.set(expression)

def sgn(a):
    return 1 if a>0 else -1 if a<0 else 0

def clearback():
    result1=""
    result2=""
    global equation
    global expression
    global value
    global ans

    expression = area.get()
    temp1= list(expression)    
    temp2= list(value)
        
    if value=='':
        temp1=[]
        temp2=[]
    elif expression[-5:]=="asin(":
        for _ in range(5):temp1.pop()
        for _ in range(10):temp2.pop()
    
    elif expression[-5:]=="acos(":
        for _ in range(5):temp1.pop()
        for _ in range(11):temp2.pop()
    
    elif expression[-5:]=="atan(":
        for _ in range(5):temp1.pop()
        for _ in range(11):temp2.pop()
        
    elif expression[-4:]=="log(":
        for _ in range(4):temp1.pop()
        for _ in range(11):temp2.pop()
        
    elif expression[-4:]=='sin(':
        for _ in range(4): temp1.pop()
        for _ in range(9): temp2.pop()
    
    elif expression[-4:]=='cos(' :
        for _ in range(4): temp1.pop()
        for _ in range(9): temp2.pop()
        
    elif expression[-4:]=='tan(':
        for _ in range(4): temp1.pop()
        for _ in range(9): temp2.pop()
        
    elif expression[-4:]=='sgn(':
        for _ in range(4): temp1.pop()
        for _ in range(4): temp2.pop()
        
    elif expression[-3:]=='ln(':
        for _ in range(3):temp1.pop()
        for _ in range(9): temp2.pop()
        
    elif expression[-2:]=='e^':
        for _ in range(2):temp1.pop()
        for _ in range(8): temp2.pop()
        
    elif expression[-1]=='^':
        for _ in range(1):temp1.pop()
        for _ in range(2): temp2.pop()

    elif expression[-1]=="√":
        for _ in range(1):temp1.pop()
        for _ in range(10):temp2.pop()
        
    elif expression[-1]=='π':
        for _ in range(1):temp1.pop()
        for _ in range(7): temp2.pop()
        
    elif expression[-1]=='e':
        for _ in range(1):temp1.pop()
        for _ in range(6): temp2.pop() 

    elif expression[-1]=='%':
        for _ in range(1):temp1.pop()
        for _ in range(4): temp2.pop()      
        
    else: 
        temp1.pop()
        temp2.pop()
        
    for element in range(len(temp1)):
        result1+=temp1[element]
    expression = result1
    equation.set(expression)
        
    for element in range(len(temp2)):
        result2+=temp2[element]
        
    value=result2
    try:ans = str(eval(value))
    except:pass

def pressbtn(num):
    global expression 
    global value
    global ans
    expression = expression + str(num)
    equation.set(expression)
    if num=='1':
        value += '1'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='2':
        value += '2'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='3':
        value += '3'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='4':
        value += '4'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='5':
        value += '5'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='6':
        value += '6'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='7':
        value += '7'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='8':
        value += '8'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='9':
        value += '9'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='0':
        value += '0'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='00':
        value += '00'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='+':value += '+'
    elif num=='-':value += '-'
    elif num=='*':value += '*'
    elif num=='/':value += '/'
    elif num=='.':value += '.'    
    elif num=='asin(':value += 'math.asin('
    elif num=='acos(':value += 'math.acos('
    elif num=='atan(':value += 'math.atan('
    elif num=='^':value += '**'
    elif num=='%':
        value += '/100'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='^2':
        value += '**2'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='^3':
        value += '**3'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='1/':value += '1/'
    elif num=='√(':value += 'math.sqrt('
    elif num=='sin(':value += 'math.sin('
    elif num=='cos(':value += 'math.cos('
    elif num=='tan(':value += 'math.tan('
    elif num=='e':
        value += 'math.e'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='π':
        value += 'math.pi'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='log(':value += 'math.log10('
    elif num=='ln(':value += 'math.log('
    elif num=='e^':value += 'math.e**'
    elif num== 'sgn(':value += 'sgn('
    elif num=='(':
        value += '('
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num==')':
        value += ')'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"

def equal():
    global ans
    global value
    global expression

    equation.set(ans)
    ans=''
    value=''
    expression=''

root=Tk()
root.title("Scientific Calculator")

root.resizable(False,False)
cal= Frame(root)
cal.grid()
cal.configure(bg="brown1")
equation=StringVar()

area = Entry(cal, textvariable = equation,width= 60, font= ("Comic Sans MS", 15),bd=10 ,justify=LEFT,state=DISABLED,
             disabledbackground="white",disabledforeground="black") 
area.insert(0,"0")
area.grid(row=0,columnspan=8)

def standard():
    root.geometry('361x350')
    area['width']=28
    area.grid(row=0,columnspan=4,sticky= EW)
    root.title("Standard Calculator")
    
def scientific():
    root.geometry('742x350')
    area['width']=60
    area.grid(row=0,columnspan=8)
    root.title("Scientific Calculator")

menubar = Menu(cal)
filemenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label= "Standard", command= standard)

filemenu.add_separator()
filemenu.add_command(label="Scientific", command= scientific)
root.config(menu=menubar)

value=""   
ans=""
expression=""

font= tkinter.font.Font(size=12,weight= "bold", family='Helvetica',)
h=2
w=7
actvbgnd='white'
bg1='gray0'
bg2="chocolate1"
bg3="salmon1"
bg4= "RosyBrown1"
fg1= "white"
fg2="black"

numberpad = [7,8,9,4,5,6,1,2,3]
i=0
for j in range(3):
    for k in range(3):
        Button(cal,command  = lambda x =str(numberpad[i]) : pressbtn(x), text = str(numberpad[i]), bg= bg1, fg=fg1,activebackground=actvbgnd,
               height=h, width=w,font= font).grid(row=j+2,column=k)
        i+=1

r=5
c=7
Button(cal,command  = lambda: pressbtn('0'),  text = "0", bg= bg1, fg=fg1,activebackground=actvbgnd,
                    height=h, width=w,font= font).grid(row=r,column= c-7)
Button(cal,command  = lambda: pressbtn('00'),text = "00", bg= bg1, fg=fg1,activebackground=actvbgnd,
                    height=h, width=w,font= font).grid(row=r,column= c-6)
Button(cal,command  = clearback,            text = "C", bg= bg2, fg=fg2,activebackground=actvbgnd,
                    height=h, width=w,font= font).grid(row=r-4,column= c-7)
Button(cal,command  = clearall,              text = "AC",bg= bg2, fg=fg2,activebackground=actvbgnd,
                   height=h, width=w,font= font).grid(row=r-4,column= c-6)
Button(cal,command  = lambda: pressbtn('.'), text = "•", bg= bg3, fg=fg2,activebackground=actvbgnd,
                   height=h, width=w,font= font).grid(row=r,column=c-5)
Button(cal,command  = lambda: pressbtn('+'), text = "+", bg= bg3, fg=fg2,activebackground=actvbgnd,
                   height=h, width=w,font= font).grid(row=r-2,column=c-4)
Button(cal,command  = lambda: pressbtn('-'),  text = "–", bg= bg3, fg=fg2,activebackground=actvbgnd,
                  height=h, width=w,font= font).grid(row=r-3,column=c-4)
Button(cal,command  = lambda: pressbtn('/'),   text = "/", bg= bg3, fg=fg2,activebackground=actvbgnd,
                 height=h, width=w,font= font).grid(row=r-4,column=c-5)
Button(cal,command  = lambda: pressbtn('*'),  text = "✶", bg= bg3, fg=fg2,activebackground=actvbgnd,
                  height=h, width=w,font= font).grid(row=r-4,column=c-4)
Button(cal,command  = equal,                text = "=", bg= bg2, fg=fg2,activebackground=actvbgnd,
                    height=2*h,width=w,font= font,pady=10).grid(row=r-1,column=c-4,rowspan=2,)

list1=['(',')','%','asin','sin','log','x^2','acos','cos','ln','x^3','atan','tan','e^x','1/x','x^y','e',"π",'√x','sgn']
list2=['(',')','%','asin(','sin(','log(','^2','acos(','cos(','ln(','^3','atan(','tan(','e^','1/','^','e',"π",'√(','sgn(']
i=0
btn=[]
for j in range(5):
    for k in range(4):
        Button(cal,command  = lambda x= list2[i]: pressbtn(x),  text = list1[i], bg=bg4,  fg= fg2,activebackground=actvbgnd,
               height=h,width=w,font= font).grid(row=j+1,column=k+4)
        i+=1

msize=60
cal.rowconfigure(0,minsize=50)
for i in range(1,6):
    cal.rowconfigure(i,minsize=60)

msize = 90
for i in range(8): 
    cal.columnconfigure(i,minsize= msize)

cal.mainloop()
