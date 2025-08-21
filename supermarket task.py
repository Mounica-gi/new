#super market task
#customer name
customer_name=input("enter costomer name...")
#list of items
list='''
rice  Rs 20kg
sugar Rs 25kg
salt  Rs 30kg
chicken Rs 35kg
'''

price=0
totalprice=0
finalprice=0
pricelist=[]
plist=[]
qlist=[]
ilist=[]

items={
    'rice':20,
    'sugar':25,
    'salt':30,
    'chicken':35
}

while True:
  option=input("enter option 1 to buy 2 to exit")
  if option=='2':
   print("thank you for visting")
   break

  elif option=='1':
    print(list)
    while True:
             input1=input("enter input 1 to buy or 2 to exit")
             if input1=='2':
              print("thanks for shopping")
              break
             elif input1=='1':
                 item=input("enter item to buy").lower()

                 while True:
                    quantity_input=input("enter your quantity item ")
                    if quantity_input.isdigit():
                          quantity=int(quantity_input)
                          break
                    else:

                     print("sorry for incovincece")

                 if item in items:
                    price=quantity*items[item]
                    pricelist.append((item,quantity,price,items[item]))
                    totalprice+=price
                    qlist.append(quantity_input)
                    plist.append(price)
                    ilist.append(item)
                 else:
                    print("its over.....")

           #tax 10% for total price
    if totalprice>0:
        tax=(totalprice*10)/100
        finalprice=tax+totalprice
        print("super market")
        print("hyd")
        print(f"{customer_name}")
        print(items,quantity,price)

    for i in range(len(pricelist)):
        price(i+1,qlist[i],plist[i],ilist[i])
        print(f"Rs {totalprice}")
        print(f"{tax}")
        print(f"{finalprice}")
        print("visit again thank you.....")
             



 
  

