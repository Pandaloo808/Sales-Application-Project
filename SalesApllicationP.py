from tkinter import *

root=Tk()
root.title("Sales Application")
root.geometry("600x500")
root.configure(bg="#708ae0")

months=Label(root,bg="#708ae0",fg="black",font=("comic sans ms",12,"italic"))
months.place(relx=0.5, rely=0.3,anchor=CENTER)
months["text"]="Months : " + str(month)

profits=Label(root,bg="#708ae0",fg="black",font=("bold"))
profits.place(relx=0.5,rely=0.4,anchor=CENTER)
profits["text"]="Profits : " + str(profit)

maxP=Label(root,bg="#708ae0",fg="black")
maxP.place(relx=0.5,rely=0.6,anchor=CENTER)

minP=Label(root,bg="#708ae0",fg="black")
minP.place(relx=0.5,rely=0.8,anchor=CENTER)

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novemeber", "December")

profit = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

def maxProf():
    max_profit= max(profits)
    max_profit_index=profits.index(max_profit)
    print(max_profit_index)

    max_profit_month=month[max_profit_index]
    maxP["text"]="The maximum profit of " + str(max_profit)+ " was recorded in the month of " +str(max_profit_month)

def minProf():
    min_profit= min(profits)
    min_profit_index=profits.index(min_profit)
    print(min_profit_index)

    min_profit_month=month[min_profit_index]
    minP["text"]="The minimum profit of " + str(min_profit)+ " was recorded in the month of " +str(min_profit_month)

btnMax=Button(root,text="Show Max Profitable Month",command=maxProf,bg="#fcba03",fg="black")
btnMax.place(relx=0.5,rely=0.5,anchor=CENTER)

btnMin=Button(root,text="Show Min Profitable Month",command=minProf,bg="#fcba03",fg="black")
btnMin.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()
