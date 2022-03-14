import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")  

tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='what does this calculator do?')      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Set Generation 0 Values')      # Make second tab visible
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Display Generation 0 Values') 
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='Run the Model')
tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text='junk')


tabControl.pack(expand=1, fill="both")  # Pack to make visible

########################################################################
#LabelFrame using tab1 as the parent
mighty1 = ttk.LabelFrame(tab1) # text='Main Page'
mighty1.grid(column=0, row=0, padx=8, pady=4)

#juvenile label
ttk.Label(mighty1, text=" WELCOME!\
        \n This calcualtor generates results based on its input of bird popualtion numbers to pedict\
        \n the numbers of every new generation the user requests. This software can display the values\
        \n the user has entered as well as save them on a file. To use just click on the relevent buttons\
        \n starting with 'set generation 0 values' and follow thorugh with the rest of the instructions.\
        \n Enjoy!\
        \n+\
        \n+\
        \n How To Use:\
        \n+\
        \n+\
        \n+\
        \n+\
        \n+\
        \n+\
        \n+\
        \n Made by Kenza Borja.").grid(column=0, row=0)









##################################################################################
#########################################################################
#SET GEN values
mighty2 = ttk.LabelFrame(tab2) # text='Main Page'
mighty2.grid(column=0, row=0, padx=8, pady=4)

# Modified Button Click Function
def done_page1(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get())



############################################################################
#juvenile label
ttk.Label(mighty2, text="Enter the number of jeveniles:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty2, width=12, textvariable=name)
name_entered.grid(column=1, row=0, sticky='W')   

# servial rate 
ttk.Label(mighty2, text="Servival Rate:").grid(column=2, row=0)

# servial rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty2, width=12, textvariable=name)
name_entered.grid(column=3, row=0, sticky='W')   

############################################################################
#number of adults
ttk.Label(mighty2, text="Enter the Number of Adults:").grid(column=0, row=1)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty2, width=12, textvariable=name)
name_entered.grid(column=1, row=1, sticky='W')   

# servial rate 
ttk.Label(mighty2, text="Servival Rate:").grid(column=2, row=1)

# servial rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty2, width=12, textvariable=name)
name_entered.grid(column=3, row=1, sticky='W')

##############################################################################
#number of adults
ttk.Label(mighty2, text="Enter the Number of Seniles:").grid(column=0, row=2)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty2, width=12, textvariable=name)
name_entered.grid(column=1, row=2, sticky='W')   

# servial rate 
ttk.Label(mighty2, text="Servival Rate:").grid(column=2, row=2)

# servial rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty2, width=12, textvariable=name)
name_entered.grid(column=3, row=2, sticky='W')

# seniles birth rate
ttk.Label(mighty2, text="Birth Rate:").grid(column=4, row=2)

# seniles bith rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty2, width=12, textvariable=name)
name_entered.grid(column=5, row=2, sticky='W')


###############################################################################
# number of gens 
ttk.Label(mighty2, text="Enter the Number of New Generations:").grid(column=0, row=3)

# servial rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty2, width=12, textvariable=name)
name_entered.grid(column=1, row=3, sticky='W')

##################################################################################
# done button
# Adding a Button
action = ttk.Button(mighty2, text="Done", command=done_page1)   
action.grid(column=5, row=4)   








################################################################
###############################################################
#display gen values
mighty3 = ttk.LabelFrame(tab3, text='')
mighty3.grid(column=0, row=0, padx=8, pady=4)

#juvenile label
ttk.Label(mighty3, text="Number of Jeveniles:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty3, width=12, textvariable=name)
name_entered.grid(column=1, row=0, sticky='W')   

# servial rate 
ttk.Label(mighty3, text="Servival Rate:").grid(column=2, row=0)

# servial rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty3, width=12, textvariable=name)
name_entered.grid(column=3, row=0, sticky='W')   

############################################################################
#number of adults
ttk.Label(mighty3, text="Number of Adults:").grid(column=0, row=1)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty3, width=12, textvariable=name)
name_entered.grid(column=1, row=1, sticky='W')   

# servial rate 
ttk.Label(mighty3, text="Servival Rate:").grid(column=2, row=1)

# servial rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty3, width=12, textvariable=name)
name_entered.grid(column=3, row=1, sticky='W')

##############################################################################
#number of adults
ttk.Label(mighty3, text="Number of Seniles:").grid(column=0, row=2)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty3, width=12, textvariable=name)
name_entered.grid(column=1, row=2, sticky='W')   

# servial rate 
ttk.Label(mighty3, text="Servival Rate:").grid(column=2, row=2)

# servial rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty3, width=12, textvariable=name)
name_entered.grid(column=3, row=2, sticky='W')

# seniles birth rate
ttk.Label(mighty3, text="Birth Rate:").grid(column=4, row=2)

# seniles bith rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty3, width=12, textvariable=name)
name_entered.grid(column=5, row=2, sticky='W')


###############################################################################
# number of gens 
ttk.Label(mighty3, text="Number of New Generations:").grid(column=0, row=3)

# servial rate box
name = tk.StringVar()
name_entered = ttk.Entry(mighty3, width=12, textvariable=name)
name_entered.grid(column=1, row=3, sticky='W')








###############################################################################
###############################################################################
#run the model



























































#####################################################################################
#####################################################################
# Tab Control junk refactoring  ---------------------------------------------------------

# We are creating a container frame to hold all other widgets -- Tab2

mighty5 = ttk.LabelFrame(tab5, text=' The Snake ')
mighty5.grid(column=0, row=0, padx=8, pady=4)

# Creating three checkbuttons

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty5, text="Disabled", variable=chVarDis, state='disabled')

check1.select()
check1.grid(column=0, row=4, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty5, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty5, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)                     

# GUI Callback function 
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   


# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]   

# We have also changed the callback function to be zero-based, using the list 
# instead of module-level global variables 
# Radiobutton Callback

def radCall():
    radSel=radVar.get()
    if   radSel == 0: mighty5.configure(text='Blue')
    elif radSel == 1: mighty5.configure(text='Gold')
    elif radSel == 2: mighty5.configure(text='Red')

# create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
radVar.set(99)                                 
 
# Now we are creating all three Radiobutton widgets within one loop - Tab2
for col in range(3):                             
    curRad = tk.Radiobutton(mighty5, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=6, sticky=tk.W)             # row=6

# Now we are creating all three Radiobutton widgets within one loop - Tab1
#for col in range(3):                             
    #curRad = tk.Radiobutton(mighty, text=colors[col], variable=radVar, 
                            #value=col, command=radCall)          
    #curRad.grid(column=col, row=2, sticky=tk.W)             # row=2, Bug!

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty5, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=7)        
 
# Place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit() 
    
# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)


name_entered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()