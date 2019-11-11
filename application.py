from tkinter import *  #library
import random #random number generator
import time; #time

app = Tk()  #name of app
app.geometry("1600x800")  #size of the app

app.title("Captain Cook Restaurant")

Tops= Frame(app, width=1600,relief=SUNKEN)#creating frame
Tops.pack(side=TOP)   #packing the frame

f1= Frame(app, width=800, height=700, relief=SUNKEN)  #creating frame
f1.pack(side=LEFT)   #packing the frame

f2= Frame(app, width=300, height='700',bg="powder blue", relief=SUNKEN)  #creating frame
f2.pack(side=RIGHT)   #packing the frame



localtime = time.asctime(time.localtime(time.time())) #getting time

#input variable for text displa
text_Input = StringVar()
operator=''
rand=''
FriesValue= IntVar()
BurgerValue=IntVar()
PizzaValue=IntVar()
ChickenValue=IntVar()
CheeseValue= IntVar()
Service_ChargeValue=IntVar()
TaxValue=IntVar()
SubTotalValue=IntVar()
TotalValue=IntVar()
CostValue=IntVar()
DrinksValue=IntVar()



Title= Label(Tops,font=('arial',20,'bold'),text='Captain cook Restaurant Management System', fg='Steel Blue', bd='10', anchor='w' )
Title.grid(row=0,column=0)

#writing the date and time
Date= Label(Tops,font=('arial',20,'bold'),text=localtime, fg='Steel Blue', bd=10, anchor='w' )
Date.grid(row=1, column=0)

#building the calculator
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def ButtonClearDisplay():
    global operator
    operator=''
    text_Input.set('')


def ButtonEquals():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    
def Ref():
    x= random.randint(12908,50876)
    randomRef=str(x)
    rand.set(randomRef)
    
    QtyFries=float(FriesValue.get())
    QtyBurger=float(BurgerValue.get())
    QtyPizza=float(PizzaValue.get())
    QtyChicken=float(ChickenValue.get())
    QtyCheese=float(CheeseValue.get())
    QtyDrinks=float(DrinksValue.get())
    
    FriesPrice= QtyFries*0.99
    BurgerPrice= QtyBurger* 1.00
    PizzaPrice=QtyPizza* 2.99
    ChickenPrice=QtyChicken*2.87
    CheesePrice=QtyCheese*2.89
    DrinksPrice=QtyDrinks*2.69
    
    Meal_Cost= "$"+str('%.2f' %(FriesPrice+BurgerPrice+PizzaPrice+ChickenPrice+CheesePrice+DrinksPrice))
    PayTax= ((FriesPrice+BurgerPrice+PizzaPrice+ChickenPrice+CheesePrice+DrinksPrice)*0.2)
    TotalCost=FriesPrice+BurgerPrice+PizzaPrice+ChickenPrice+CheesePrice+DrinksPrice
    Service_Charge=((FriesPrice+BurgerPrice+PizzaPrice+ChickenPrice+CheesePrice+DrinksPrice)/99)
    Service="$"+str('%.2f' % Service_Charge)
    OverallCost="$"+str('%.2f' % (PayTax+TotalCost+Service_Charge))
    PaidTax="$"+str('%.2f' % PayTax)
    
    
    Service_ChargeValue.set(Service)
    TaxValue.set(PaidTax)
    TotalValue.set(OverallCost)
    SubTotalValue.set(Meal_Cost)
    CostValue.set(Meal_Cost)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
def Exit():
    app.destroy()

def Reset():
    rand.set("")
    FriesValue.set("")
    BurgerValue.set("")
    PizzaValue.set("")
    ChickenValue.set("")
    CheeseValue.set("")
    Service_ChargeValue.set("")
    TaxValue.set("")
    SubTotalValue.set("")
    TotalValue.set("")
    CostValue.set("")
    DrinksValue.set("")








#text display
txtDisplay= Entry(f2, font=('arial',20,'bold'),
                   textvariable=text_Input, bd=30, 
                   insertwidth=4, bg='powder blue', justify='right')
                  
txtDisplay.grid(columnspan=4)

#row2
btn7= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='7', bg='powder blue', command=lambda :btnClick(7)).grid(row=2,column=0 )   

btn8= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='8', bg='powder blue', command=lambda :btnClick(8)).grid(row=2,column=1 )   
              
btn9= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='9', bg='powder blue', command=lambda :btnClick(9)).grid(row=2,column=2 )   
                  
Addition= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='+', bg='powder blue', command=lambda :btnClick('+')).grid(row=2,column=3 ) 

  

btn4= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='4', bg='powder blue', command=lambda :btnClick(4)).grid(row=3,column=0 )   

btn5= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='5', bg='powder blue', command=lambda :btnClick(5)).grid(row=3,column=1 )   
              
btn6= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='6', bg='powder blue', command=lambda :btnClick(6)).grid(row=3,column=2 )   
                  
Subtraction= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='-', bg='powder blue', command=lambda :btnClick('-')).grid(row=3,column=3 )   



btn1= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='1', bg='powder blue', command=lambda :btnClick(1)).grid(row=4,column=0 )   

btn2= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='2', bg='powder blue', command=lambda :btnClick(2)).grid(row=4,column=1 )   
              
btn3= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='3', bg='powder blue', command=lambda :btnClick(3)).grid(row=4,column=2 )   
                  
Multiply= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='*', bg='powder blue', command=lambda :btnClick('*')).grid(row=4,column=3 )   



btn0= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='0', bg='powder blue', command=lambda :btnClick(0)).grid(row=5,column=0 )   

btnClear= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='C', bg='powder blue',command=ButtonClearDisplay).grid(row=5,column=1 )   
              
btnEquals= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='=', bg='powder blue', command=ButtonEquals).grid(row=5,column=2 )   
                  
Division= Button(f2, padx=16, pady=16,bd=8,fg='black', font=('arial',20,'bold')
             ,text='/', bg='powder blue', command=lambda :btnClick('/')).grid(row=5,column=3 )   


Reference= Label(f1,font=('arial',16,'bold'),text='Order Reference',  bd='16', anchor='w' )
Reference.grid(row=0, column=0)
ReferenceText= Entry(f1,font=('arial',16,'bold'),textvariable=rand,  bd='10', insertwidth=4, bg='powder blue',justify='right' )
ReferenceText.grid(row=0, column=1)

Fries= Label(f1,font=('arial',16,'bold'),text='Large Fries',  bd='16', anchor='w' )
Fries.grid(row=1, column=0)
FriesText= Entry(f1,font=('arial',16,'bold'),textvariable=FriesValue,  bd='10', insertwidth=4, bg='powder blue',justify='right' )
FriesText.grid(row=1, column=1)


Burger= Label(f1,font=('arial',16,'bold'),text='Hamburger',  bd='16', anchor='w' )
Burger.grid(row=2, column=0)
BurgerText= Entry(f1,font=('arial',16,'bold'),textvariable=BurgerValue,  bd='10', insertwidth=4, bg='powder blue',justify='right' )
BurgerText.grid(row=2, column=1)

Pizza= Label(f1,font=('arial',16,'bold'),text='Pizza ',  bd='16', anchor='w' )
Pizza.grid(row=3, column=0)
PizzaText= Entry(f1,font=('arial',16,'bold'),textvariable=PizzaValue,  bd='10', insertwidth=4, bg='powder blue',justify='right' )
PizzaText.grid(row=3, column=1)

Chicken= Label(f1,font=('arial',16,'bold'),text='Kenturckey Fried Chicken',  bd='16', anchor='w' )
Chicken.grid(row=4, column=0)
ChickenText= Entry(f1,font=('arial',16,'bold'),textvariable=ChickenValue,  bd='10', insertwidth=4, bg='powder blue',justify='right' )
ChickenText.grid(row=4, column=1)

Cheese= Label(f1,font=('arial',16,'bold'),text='MacDonalds Cheese',  bd='16', anchor='w' )
Cheese.grid(row=5, column=0)
CheeseText= Entry(f1,font=('arial',16,'bold'),textvariable=CheeseValue,  bd='10', insertwidth=4, bg='powder blue',justify='right' )
CheeseText.grid(row=5, column=1)


#restuarant info 2
Drinks= Label(f1,font=('arial',16,'bold'),text='Drinks',  bd='16', anchor='w' )
Drinks.grid(row=0, column=2)
DrinksText= Entry(f1,font=('arial',16,'bold'),textvariable=DrinksValue,  bd='10', insertwidth=4, bg='#ffffff',justify='right' )
DrinksText.grid(row=0, column=3)


Cost= Label(f1,font=('arial',16,'bold'),text='Cost of meal',  bd='16', anchor='w' )
Cost.grid(row=1, column=2)
CostText= Entry(f1,font=('arial',16,'bold'),textvariable=CostValue,  bd='10', insertwidth=4, bg='#ffffff',justify='right' )
CostText.grid(row=1, column=3)


Service= Label(f1,font=('arial',16,'bold'),text='Service Charge',  bd='16', anchor='w' )
Service.grid(row=2, column=2)
ServiceText= Entry(f1,font=('arial',16,'bold'),textvariable=Service_ChargeValue,  bd='10', insertwidth=4, bg='#ffffff',justify='right' )
ServiceText.grid(row=2, column=3)

Tax= Label(f1,font=('arial',16,'bold'),text='State Tax ',  bd='16', anchor='w' )
Tax.grid(row=3, column=2)
TaxText= Entry(f1,font=('arial',16,'bold'),textvariable=TaxValue,  bd='10', insertwidth=4, bg='#ffffff',justify='right' )
TaxText.grid(row=3, column=3)

SubTotal= Label(f1,font=('arial',16,'bold'),text='SubTotal',  bd='16', anchor='w' )
SubTotal.grid(row=4, column=2)
SubTotalText= Entry(f1,font=('arial',16,'bold'),textvariable=SubTotalValue,  bd='10', insertwidth=4, bg='#ffffff',justify='right' )
SubTotalText.grid(row=4, column=3)

Total= Label(f1,font=('arial',16,'bold'),text=' Total',  bd='16', anchor='w' )
Total.grid(row=5, column=2)
TotalText= Entry(f1,font=('arial',16,'bold'),textvariable=TotalValue,  bd='10', insertwidth=4, bg='#ffffff',justify='right' )
TotalText.grid(row=5, column=3)

ButonTotal= Button(f1, padx=16, pady=8,bd=16,fg='black', font=('arial',20,'bold')
             ,text='Total', bg='powder blue', command=Ref).grid(row=7,column=1 )



BuutonReset= Button(f1, padx=16, pady=8,bd=16,fg='black', font=('arial',20,'bold')
             ,text='Reset', bg='powder blue', command=Reset).grid(row=7,column=2 )   


 
ButonExit= Button(f1, padx=16, pady=8,bd=16,fg='black', font=('arial',20,'bold')
             ,text='Exit', bg='powder blue', command=Exit).grid(row=7,column=3 )   





app.mainloop()
