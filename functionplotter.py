###############begin with imports
from tkinter import *
import tkinter as tk  
from tkinter import ttk
import tkinter as tk  
from tkinter import ttk
import tkinter
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from sympy import Symbol
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
xx= np.linspace(-5,5,100)
win=tk.Tk()
name = tk.StringVar()
display=tk.StringVar()
######################################## make a class called fun to draw a frame of gui
class fun(Frame):
    def __init__(self):
        Frame.__init__(self, bg= 'red')
        self.option_add('*font', 'aril 16 ')                         # for enlarge the size
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Function_ploter')
        lbl = ttk.Label(self, text = "Enter the function:")
        lbl.pack(side=TOP, expand=YES, fill= BOTH)
        display = StringVar()
        obj=Entry(self, relief=RIDGE, textvariable= display, justify = 'left',
                  bd=20, bg='powder blue', width=20)       # htzhr fo2 al main frame
        obj.pack(side=TOP, expand=YES, fill= BOTH)

        ##########to make buttons
        clear_button=Button(self, text='Clear', bg='white', bd=2,
                            command=lambda stored= display: stored.set("") )    ###clear button
        clear_button.pack(side=TOP, expand=YES, fill=BOTH)
        fig = Figure(figsize=(5, 4), dpi=100)
        T = tk.Text(self, height=2, width=30)
        T.pack(side=TOP,expand=YES,fill=BOTH)
        check=Button(self,text='check for error',bg='white',bd=2,
                     command= lambda stored=display:T.insert(tk.END, check_err(stored)) )      #check for error button
        check.pack(side=TOP, expand=YES, fill=BOTH)
        equal=Button(self, text='Draw', bg='white', bd=2,
                     command= lambda stored=display: fig.add_subplot(111).plot(xx,click(stored)) )
        equal.pack(side=TOP, expand=YES, fill=BOTH)        #draw button
        
       ### to draw in gui 

        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


        def _quit():
            self.quit()     # stops mainloop
            self.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        button = tkinter.Button(master=self, text="exit", command=_quit)
        button.pack(side=tkinter.BOTTOM)     # exit button
############################## check for error function
def check_err(stored):
        name=stored.get()
        x1=0
        x2=0
        x3=0
        y = name
        for input_char in y :
               # CHECKING FOR ALPHABET 
            if ((ord(input_char) >= 65 and ord(input_char) <= 90) or (ord(input_char) >= 97 and ord(input_char) <= 122)) :
               if input_char=="x":
                   x1=0
  
               else:
                   x1=1
 
                   continue
            # CHECKING FOR DIGITS 
            elif (ord(input_char) >= 48 and ord(input_char) <= 57): 

                pass
  
            # OTHERWISE SPECIAL CHARACTER 
            else:
                if(input_char=="+" or input_char=="-" or input_char=="/" or input_char=="*" or input_char=="^"):
   
                    if input_char=="+" or input_char=="-" or input_char=="/" or input_char=="*" :
                        x2=0
                         
                        continue
                    else:
                        x2=1
                        x3=1
                         
                        break
                else:
                    x2=1
 
        import tkinter as tk

        if(x1==1 and x2==0):
            return(" Error use only letter x ")
        elif(x1==0 and x2==1 and x3==1):
            return(" Error use ** instead of ^ ")
        elif(x1==0 and x2==1 and x3==0):
            return(" Error don't use special characters ")
        elif(x1==1 and x2==1 and x3==0):
            return(" Error use x only and don't use special characters ")
        elif(x1==1 and x2==1 and x3==1):
            return(" Error use x only and ** instead of ^ ")
        elif(x1==0 and x2==0 and x3==0):
            return( " No Error ")

########################## Draw function
def click(stored):
        name=stored.get()

        x1=0
        x2=0
        x3=0
        y = name
        for input_char in y :

               # CHECKING FOR ALPHABET 
            if ((ord(input_char) >= 65 and ord(input_char) <= 90) or (ord(input_char) >= 97 and ord(input_char) <= 122)) :
               if input_char=="x":
                   x1=0

               else:
                   x1=1
                   continue
            # CHECKING FOR DIGITS 
            elif (ord(input_char) >= 48 and ord(input_char) <= 57): 
                pass
  
            # OTHERWISE SPECIAL CHARACTER 
            else:
                if(input_char=="+" or input_char=="-" or input_char=="/" or input_char=="*" or input_char=="^"):
                    if input_char=="+" or input_char=="-" or input_char=="/" or input_char=="*" :
                        x2=0
                        continue
                    else:
                        x2=1
                        x3=1
                        break
                else:
                    x2=1
        import tkinter as tk

        if(x1==0 and x2==0 and x3==0):
            # plot the function
    
            fx=list(y)  # make array of string

            y=0
            plus=0 
            mult=0
            div=0
    
            x=symbols('x')
            
            neg=0
            xtem=0
            for i in fx:
                if i=="x":

                    if y==0:
                        y=x
                    elif plus==1:
                       y=y+x
                       plus=0
                    elif neg==1:
                       y=y-x
                       neg=0
                    elif mult==1:
                        if(xtem=="x"):
                            xtem2=x*x
                            y=y-x+xtem2
                            mult=0
                        else:
                            xtem2=int(xtem)*x
                            y=y-int(xtem)+xtem2
                            mult=0
 
                    elif div==1:
                        if(xtem=="x"):
                            xtem2=x/x
                            y=y-x+xtem2
                            div=0

                        else:

                            xtem2=int(xtem)/x
                            y=y-int(xtem)+xtem2
                            div=0

                    elif mult==2:
                        if(xtem=="x"):
                            xtem2=x**x
                            y=y-x+xtem2
                            mult=0
                        else:

                            xtem2=int(xtem)**x
                            y=y-int(xtem)+xtem2
                            mult=0
                elif i=="+":
                    plus=1
                elif i=="-":
                    neg=1
                elif i=="*":
                    mult=mult+1
                
                elif i=="/":
                    div=1
                else:
                    if plus==1:
                        y=y+int(i)
                        plus=0
                    elif neg==1:
                        y=y-int(i)
                        neg=0
                    elif mult==1:
                        if(xtem=="x"):
                            xtem2=x*int(i)
                            y=y-x+xtem2
                            mult=0
                        
                        else:
                            
                            xtem2=int(xtem)*int(i)
                            y=y-int(xtem)+int(xtem2)
                            mult=0
                

                    elif div==1:
                        if(xtem=="x"):
                            xtem2=x/int(i)
                            y=y-x+int(xtem2)
                            div=0
                        else:

                            xtem2=int(xtem)/int(i)
                            y=y-int(xtem)+int(xtem2)
                            div=0

                    elif mult==2:
                        if(xtem=="x"):
                            xtem2=x**int(i)
                            y=y-x+xtem2
                            mult=0
                        else:
                            xtem2=int(xtem)**int(i)
                            y=y-int(xtem)+int(xtem2)
                            mult=0
                
                    else:
                        y=int(i)
                        #y=int(i)
                    

                if i!="*" and i!="/" and i!="+" and i!="-":
                    xtem=i
          
        

   
            xp=10
            y11 = []
            xx= np.linspace(-5,5,100)
            for i in xx:
               yy=y.subs(x,i)
               y11.append(float(yy))

        else:
            pass
        return y11



fun().mainloop()