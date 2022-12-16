from tkinter import *
import requests,json

win=Tk()

var=StringVar()
var.set("Currency")

var2=StringVar()
var2.set("Currency")

options = ["EUR", "USD", "JPY", "TRY"]
options2 = ["EUR", "USD", "JPY", "TRY"]

def clear_all():
    entry1.delete(0,END)
    var.set('Currency')
    var2.set('Currency')

def exchange():
    base_url=r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    lbl3=var.get()
    lbl4=var2.get()
    api_key="K3MQO5ISZGAYC6NI"

    main_url=base_url+"&from_currency="+lbl3+"&to_currency="+lbl4+"&apikey="+api_key
    print(main_url)

    req_ob=requests.get(main_url)
    result=req_ob.json()
    rate=float(result["RealTime Currency Exchange Rate"]["5. Exchange Rate"])
    print(rate)
    amount=entry1.get()
    final=round(float(rate)*float(amount),2)
    entry2.insert(0, final)


option=OptionMenu(win,var,*options)
option.grid(row=2,column=1)

option2=OptionMenu(win,var2,*options2)
option2.grid(row=3,column=1)

lbl1=Label(win,text="           Welcome to Real Time Currency Conventor")
lbl1.grid(row=0,column=0)

lbl2=Label(win,text="Amount:")
lbl2.grid(row=1,column=0)

entry1=Entry(win)
entry1.grid(row=1,column=1)

lbl3=Label(win,text="From Currency: ")
lbl3.grid(row=2,column=0)

lbl4=Label(win,text="To Currency: ")
lbl4.grid(row=3,column=0)

conv2=Button(win,text="Convert",command=exchange)
conv2.grid(row=4,column=1)

lbl5=Label(win,text="Result: ")
lbl5.grid(row=5,column=0)

entry2=Entry(win)
entry2.grid(row=5,column=1)


win.mainloop()