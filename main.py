'''
Created on Apr 16, 2019

@author: Sebyb
'''

from tkinter import *
from tkinter import ttk

def begin():
    # Checks login credentials
    if (enterName.get() == 'admin' and enterPassword.get() == 'password'):
        start()
    else: 
        error()

# Error handlind for invalid login
def error():
    def close():
        loginError.destroy()
    loginError = Tk()
    invalid = Label(loginError, text = "Invalid Login", fg='red', width = 10, height = 3)
    confirm = Button(loginError, text = "Ok", width = 3, height = 1, command = close)
    invalid.pack()
    confirm.pack()

# Starts program with proper login
def start():
    def calculate():
        total = Tk()
        total.title("Total")
        
        # Reads user input
        fiberHelm = int(enterHelmet.get())*int(fibercostHelmet.get())
        fiberChest = int(enterChest.get())*int(fibercostChest.get())
        fiberLegs = int(enterLeggings.get())*int(fibercostLeggings.get())
        fiberBoots = int(enterBoots.get())*int(fibercostBoots.get())
        fiberGloves = int(enterGloves.get())*int(fibercostGloves.get())
        
        hideHelm = int(enterHelmet.get())*int(hidecostHelmet.get())
        hideChest = int(enterChest.get())*int(hidecostChest.get())
        hideLegs = int(enterLeggings.get())*int(hidecostLeggings.get())
        hideBoots = int(enterBoots.get())*int(hidecostBoots.get())
        hideGloves = int(enterGloves.get())*int(hidecostGloves.get())

        metalHelm = int(enterHelmet.get())*int(metalcostHelmet.get())
        metalChest = int(enterChest.get())*int(metalcostChest.get())
        metalLegs = int(enterLeggings.get())*int(metalcostLeggings.get())
        metalBoots = int(enterBoots.get())*int(metalcostBoots.get())
        metalGloves = int(enterGloves.get())*int(metalcostGloves.get())
        
        # Calculates and displays total costs
        totalFiber = Label(total, text="Fiber: ")
        totalHide = Label(total, text="Hide: ")
        totalMetal = Label(total, text="Metal: ")
        
        amountFiber = Label(total, text=fiberHelm+fiberChest+fiberLegs+fiberBoots+fiberGloves)
        amountHide = Label(total, text=hideHelm+hideChest+hideLegs+hideBoots+hideGloves)
        amountMetal = Label(total, text=metalHelm+metalChest+metalLegs+metalBoots+metalGloves)
        
        totalFiber.grid(row=0, column=0)
        totalHide.grid(row=1, column=0)
        totalMetal.grid(row=2, column=0)
        
        amountFiber.grid(row=0, column=1)
        amountHide.grid(row=1, column=1)
        amountMetal.grid(row=2, column=1)
        
        total.mainloop()
    
    # Closes login window and initializes calculator window
    login.destroy()
    root = Tk()
    root.title("Blueprint Cost Calculator")
    root.geometry('300x225')
    
    nb = ttk.Notebook(root)
    nb.grid(row=1, column=0, columnspan=50, rowspan=50, sticky='NESW')
     
    page1 = ttk.Frame(nb)
    nb.add(page1, text='Calculate')

    setsHelmet = StringVar()
    setsHelmet.set('0')
    setsChest = StringVar()
    setsChest.set('0')
    setsLeggings = StringVar()
    setsLeggings.set('0')
    setsBoots = StringVar()
    setsBoots.set('0')
    setsGloves = StringVar()
    setsGloves.set('0')
    
    enterHelmet = Entry(page1, width = 5, textvariable=setsHelmet)
    enterChest = Entry(page1, width = 5, textvariable=setsChest )
    enterLeggings = Entry(page1, width = 5, textvariable=setsLeggings)
    enterBoots = Entry(page1, width = 5, textvariable=setsBoots)
    enterGloves = Entry(page1, width = 5, textvariable=setsGloves)
        
    flakHelmet = Label(page1, text="Flak Helmet", width = 13, height = 1)
    flakChest = Label(page1, text="Flak Chest", width = 13, height = 1)
    flakLeggings = Label(page1, text="Flak Leggings", width = 13, height = 1)
    flakBoots = Label(page1, text="Flak Boots", width = 13, height = 1)
    flakGloves = Label(page1, text="Flak Gloves", width = 13, height = 1)
    
    go = Button(page1, text= "Calculate", bg = "green", command = calculate, height = 1, width = 10)
    
    # Edit Cost Tab
    page2 = ttk.Frame(nb)
    nb.add(page2, text='Edit Cost')
    
    flakHelmet.grid(row=1, column=3)
    flakChest.grid(row=2, column=3)
    flakLeggings.grid(row=3, column=3)
    flakBoots.grid(row=4, column=3)
    flakGloves.grid(row=5, column=3)
    
    enterHelmet.grid(row=1, column=2)
    enterChest.grid(row=2, column=2)
    enterLeggings.grid(row=3, column=2)
    enterBoots.grid(row=4, column=2)
    enterGloves.grid(row=5, column=2)
    
    go.grid(row = 7, column=2, columnspan=2)
    
    fiberHelmet = StringVar()
    fiberHelmet.set('44')
    fiberChest = StringVar()
    fiberChest.set('46')
    fiberLeggings = StringVar()
    fiberLeggings.set('40')
    fiberBoots = StringVar()
    fiberBoots.set('48')
    fiberGloves = StringVar()
    fiberGloves.set('26')
    
    fibercostHelmet = Entry(page2, width = 5, textvariable=fiberHelmet)
    fibercostChest = Entry(page2, width = 5, textvariable=fiberChest )
    fibercostLeggings = Entry(page2, width = 5, textvariable=fiberLeggings)
    fibercostBoots = Entry(page2, width = 5, textvariable=fiberBoots)
    fibercostGloves = Entry(page2, width = 5, textvariable=fiberGloves)
    
    hideHelmet = StringVar()
    hideHelmet.set('103')
    hideChest = StringVar()
    hideChest.set('117')
    hideLeggings = StringVar()
    hideLeggings.set('97')
    hideBoots = StringVar()
    hideBoots.set('72')
    hideGloves = StringVar()
    hideGloves.set('66')
    
    hidecostHelmet = Entry(page2, width = 5, textvariable=hideHelmet)
    hidecostChest = Entry(page2, width = 5, textvariable=hideChest )
    hidecostLeggings = Entry(page2, width = 5, textvariable=hideLeggings)
    hidecostBoots = Entry(page2, width = 5, textvariable=hideBoots)
    hidecostGloves = Entry(page2, width = 5, textvariable=hideGloves)
    
    metalHelmet = StringVar()
    metalHelmet.set('147')
    metalChest = StringVar()
    metalChest.set('152')
    metalLeggings = StringVar()
    metalLeggings.set('130')
    metalBoots = StringVar()
    metalBoots.set('96')
    metalGloves = StringVar()
    metalGloves.set('79')
    
    metalcostHelmet = Entry(page2, width = 5, textvariable=metalHelmet)
    metalcostChest = Entry(page2, width = 5, textvariable=metalChest )
    metalcostLeggings = Entry(page2, width = 5, textvariable=metalLeggings)
    metalcostBoots = Entry(page2, width = 5, textvariable=metalBoots)
    metalcostGloves = Entry(page2, width = 5, textvariable=metalGloves)
    
    cost = Label(page2, text="Cost:", width = 5, height = 1)
    fiber = Label(page2, text="Fiber", width = 5, height = 1)
    hide = Label(page2, text="Hide", width = 5, height = 1)
    metal = Label(page2, text="Metal", width = 5, height = 1)
    
    flakHelmet = Label(page2, text="Flak Helmet", width = 10, height = 1)
    flakChest = Label(page2, text="Flak Chest", width = 10, height = 1)
    flakLeggings = Label(page2, text="Flak Leggings", width = 10, height = 1)
    flakBoots = Label(page2, text="Flak Boots", width = 10, height = 1)
    flakGloves = Label(page2, text="Flak Gloves", width = 10, height = 1)
    
    cost.grid(row = 0, column=0)
    fiber.grid(row = 0, column=1)
    hide.grid(row = 0, column=2)
    metal.grid(row = 0, column=3)
    
    flakHelmet.grid(row=1, column=0)
    flakChest.grid(row=2, column=0)
    flakLeggings.grid(row=3, column=0)
    flakBoots.grid(row=4, column=0)
    flakGloves.grid(row=5, column=0)
    
    fibercostHelmet.grid(row=1, column=1)
    fibercostChest.grid(row=2, column=1)
    fibercostLeggings.grid(row=3, column=1)
    fibercostBoots.grid(row=4, column=1)
    fibercostGloves.grid(row=5, column=1)
    
    hidecostHelmet.grid(row=1, column=2)
    hidecostChest.grid(row=2, column=2)
    hidecostLeggings.grid(row=3, column=2)
    hidecostBoots.grid(row=4, column=2)
    hidecostGloves.grid(row=5, column=2)
    
    metalcostHelmet.grid(row=1, column=3)
    metalcostChest.grid(row=2, column=3)
    metalcostLeggings.grid(row=3, column=3)
    metalcostBoots.grid(row=4, column=3)
    metalcostGloves.grid(row=5, column=3)
    
    root.mainloop() 
  
login = Tk()
login.title("Login")
login.geometry('225x100')

loginName = Label(login, text="Username: ", width = 10)
loginPassword = Label(login, text="Password: ", width = 10)

enterName = Entry(login)
enterPassword = Entry()

go = Button(login, text = "Login", command = begin,)

loginName.grid(row = 0, column = 0)
loginPassword.grid(row = 1, column= 0)

enterName.grid(row = 0, column = 1)
enterPassword.grid(row = 1, column = 1)

go.grid(row = 4, column = 1)

login.mainloop()
