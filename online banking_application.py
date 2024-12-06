#phone pay application
#someone try to open phone by 3 times send msg
#after transaction send msg

import pywhatkit 
from time import *
from random import *
from datetime import *
hr=localtime().tm_hour
min=localtime().tm_min+2
today=date.today()
# da=localtime().
pa=1234
otp=randint(1,9)

class Phone():
    
    p="-----NII PAY-----"
    def __init__(self,name,pnum,Bname,upi_id,x,B_balance=500000):
                
        self.name=name
        self.pnum=pnum
        self.Bname=Bname
        self.upi_id=upi_id
        self.B_balance=B_balance
        self.x=x



class  mobile(Phone):
    def read(self):
        print("account holder:",self.name)
        print("your phone no:",self.pnum)
        print("your bank name:",self.Bname)
        print("your upi_id:",self.upi_id)
    def ban(self):
        j=int(input("enter a possword:"))
        if j==pa:

            print("Total Bank balance",self.B_balance)
        else:
            print("wrong pin")



    def rec(self):
        print("1) 293 unlimited 5g and voice calls and 1.5gb p/d 1 month ")
        print("2) 769 unlimited 5g and voice calls and 1.5gb p/d 3 months")
        print("3) 3555 unlimited 5g and voice calls and 2.5gb p/d 365 days")
        t=int(input("choose the plane:" ))
        j=int(input("enter a possword:"))
        if j==pa:
            if self.B_balance>t:
                if t==1:
                    self.B_balance=self.B_balance-293
                    print("succesfully reacharged")
                elif t==2:
                    self.B_balance=self.B_balance-769
                    print("succesfully reacharged")
                elif t==3:
                    self.B_balance=self.B_balance-3555
                    print("succesfully reacharged")
                    w.rewar()
            else:
                print("insufficient money in your bank")
        else:
            print("wrong pin")



    def dth(self):
        print("1) 293/1 month ")
        print("2) 769/3 months")
        print("3) 3555/12 months")
        x=int(input("choose the plane:" ))
        j=int(input("enter a possword:"))
        if j==pa:
            if self.B_balance>x:
                if x==1:
                    self.B_balance=self.B_balance-293
                    print("succesfully reacharged")
                elif x==2:
                    self.B_balance=self.B_balance-769
                    print("succesfully reacharged")
                elif x==3:
                    self.B_balance=self.B_balance-3555  
                    print("succesfully reacharged")
                    w.rewar()
            else:                  
                print("insufficient money in your bank")
        else:
            print("wrong pin")



    def mtn(self):
        h=int(input("enter number:"))
        k=int(input("enter amount:"))
        j=int(input("enter a possword:"))
        if j==pa:
            if self.B_balance>k:
                if len(str(h))==10 and k<self.B_balance:
                    self.B_balance=self.B_balance-k
                    hr=localtime().tm_hour
                    min=localtime().tm_min+2
                    z=f"An amount of INR {k} has been CREDITED to your account xxxx0564 on {today}. Total Available bal {self.B_balance}.CANARA BANK"
                    y=f"An amount of INR {k} has been DEBITED to your account xxxx0@@@ on {today}. Total Available bal {self.B_balance}.CANARA BANK"
                    print(f"{k} succesfully trasfered")
                    if k>1000:
                        w.rewar()
                    v=f"91+{h}"
                    pnum=f"91+{self.pnum}"
                    pywhatkit.sendwhatmsg(v,z,hr,min)
                    sleep(90)
                    mmin=localtime().tm_min+1
                    pywhatkit.sendwhatmsg(pnum,y,hr,mmin)
                else:
                    print("invalide input")
            else:
                print("insufficient money in your bank")
        else:
            print("wrong pin")




    def mtc(self):
        e=input("enter the bank:")
        i=input("enter the name of account holder:")
        f=(input("enter IFC Code:"))
        g=int(input("enter number:"))
        h=int(input("enter amount:"))
        j=int(input("enter a possword:"))
        v=f"91+{h}"
        pnum=f"91+{self.pnum}"
        if j==pa:

            if h<self.B_balance:
                
                self.B_balance=self.B_balance-h
                z=f"An amount of INR {h} has been CREDITED to your account {i} on {today}. Total Available bal {self.B_balance}.{e}"
                y=f"An amount of INR {h} has been DEBITED to your account {i} on {today}. Total Available bal {self.B_balance}.CANARA BANK"
                
                print("Succesfully Transfered")
                if h>1000:
                    w.rewar()
                pywhatkit.sendwhatmsg(v,z,hr,min)
                sleep(100)
                pywhatkit.sendwhatmsg(pnum,y,hr,min)
            else:
                print("Insufficient Balance")
        else:
             print("Wrong pin")




    def ins(self,amt):
        j=int(input("enter a possword:"))
        if self.B_balance>amt:
            if j==pa:
                self.B_balance=self.B_balance-amt
            else:
                print("wrong pin")
        else:
            print("insufficient amount in your bank")



    def flig(self):
        
        print("your amount is:")
        k = 0
        for i in range(4):
            k = k * 10 + randint(1,9)
        amount=k*d
        print(amount)
        c=(input("enter upi id:"))
        j=int(input("enter password:"))
        if j==pa:
            if self.B_balance>amount:
                if c==self.upi_id:
                    self.B_balance=self.B_balance-k
                    print("succesfully booked your booking status will send you later")
                    if k>3000:
                        w.rewar()
                    v=f"Qatar Airways m-Ticket from: {a} to: {b}  PsngrName: {p} TripCode: 2300SMGBNG PNR No: KS2446587 Date: {today+timedelta(days=e)} DepTime: {hr}: {min} SeatNo: {q} Class: Qatar Airways BoardingPt: {a} BoardingPtNo:  Platform: {otp}  Txn Password: {k} Please carry your photo ID during journey. T and C apply. From Qatar Airways"
                    m=f"91+{n}"
                    pywhatkit.sendwhatmsg(m,v,hr,min+1)
                else:
                    print("Wrong upi_id")
            else:
                print("insufficient bank balance")
        else:
            print("wrong possword")
       


        
    def trai(self):
        # a=input("enter from:")
        # b=input("enter a destination:")
        print("Your Amount Is:")
        k = 0
        for i in range(3):
            k = k * 10 + randint(0, 7)
        amount=k*d

        c=(input("Enter upi id:"))
        j=int(input("enter a password:"))
        if j==pa:
            if self.B_balance>amount:
                if c==self.upi_id:
                    self.B_balance=self.B_balance-k
                    print("Succesfully Booked Your Booking Status Will Send You Later")
                    if k>1500:
                        w.rewar()
                    v=f"KSRTC m-Ticket from: {a} to: {b}  PsngrName: {p} TripCode: 2300SMGBNG PNR No: KS2446587 Date: {today+timedelta(days=e)} DepTime: {hr}: {min} SeatNo: {q} Class:RANICHENNAMA EXPRESS BoardingPt: {a} BoardingPtNo:  Platform: {otp}  Txn Password: {k} Please carry your photo ID during journey. T and C apply. From Indian Railways"
                    m=f"91+{n}"
                    pywhatkit.sendwhatmsg(m,v,hr,min+1)
                    # print("succesfully booked your booking status will send you later")
                
                else:
                    print("Wrong upi_id")
            else:
                print("insufficient balance")
        else:
            print("wrong pin")

    def bus(self):
        # a=input("enter from:")
        # b=input("enter a destination:")
        print("Your Amount Is:")
        k = 0
        for i in range(3):
            k = k * 10 + randint(0,3)
        amount=k*d
        c=(input("Enter upi id:"))
        j=int(input("enter password:"))
        if j==pa:
            if self.B_balance>amount:
                if c==self.upi_id:
                    self.B_balance=self.B_balance-k
                    print("Succesfully booked your booking status will send you later")
                    # print("succesfully booked your booking status will send you later")
                    if k>1000:
                        w.rewar()

                    v=f"KSRTC m-Ticket from: {a} to: {b}  PsngrName: {p} TripCode: 2300SMGBNG PNR No: KS2446587 Date: {today+timedelta(days=e)} DepTime: {hr}: {min} SeatNo: {q} Class: AIRAVAT CLUB CLASS BoardingPt: {a} BoardingPtNo: 3  Platform: {otp}  Txn Password: {k} Please carry your photo ID during journey. T and C apply. From KSRTC"
                    m=f"91+{n}"
                    pywhatkit.sendwhatmsg(m,v,hr,min+1)
                else:
                    print("Wrong upi_id")
            else:
                print("insufficient bank balance")
        else:
            print("wrong pin ")

    def rewar(self):
        a=f"1)\u20B9 10 - \u20B9 100 cash back at zomato"
        b=f"2)\u20B9 5 - \u20B9 50 cash back on mobile reacharge"
        c=f"3)\u20B9 10 - \u20B9 50 cash back on merchant payment"
        d=f"4)\u20B9 302 cash back by reffering "
        e=f"5)\u20B9 5 - \u20B9 100 cash back on flipcart"
        f="7)flat 50% off in zomato order now"
        g="8)Flat 60% off on Tees By Fastrack Sunglasses"
        h="6)Flat\u20B9500 off on all kingdom of white style"
        i="9)Get Flat \u20B9550* free Bonus to play Ludo & 100+ games"
        j="10)New Airtel Wi-fi connection with home delivery no extra"
        k=randint(0,7)
        l=[a,b,c,d,e,f,g,h,i,j]
        self.x.append(l[k])
        print("Congradulation You Win The Reward")

        print(l[k])
        # print(self.x)
    def rewards(self):
        print("YOUR REWARDS ARE")
        print(self.x)
        print(len(self.x))
        g=int(input("Select Your Rewards:"))
        if g==1 or g==2 or g==3 or g==5 or g==6:
            w.mtn()
            y=randint(6,20)
            self.B_balance=self.B_balance+y
            self.x.remove()
            print("availabe rewards are",self.x)
            print(f"\u20B9{b} CASH BACK")
            sleep(3)
            print(f"\u20B9{b} is CREDITED succsesfully to your account")



w=mobile("NITHIN H M",7019279826,"canaraa bank","7019279826@ybl",[])
pos=int(input("enter possword:"))
if pos==pa:
    print(Phone.p)
    w.read()
# else:
#     print("wrong possword")
    while True:
        print("1)Bank Balance\n2)Recharge\n3)DTH\n4)Money Transaction To Number\n5)Money Transaction To Bank\n6)Insurence\n7)Ticket Booking\n8)Rewards\n9)Exit")
        b=int(input(":"))
        if b==1:
            w.ban()
        elif b==2:
            print("1)jiooo\n2)Aiirtel")
            a=int(input(":"))
            if a==1:
                w.rec()
            else:
                w.rec()
        elif b==3:
            print("1)San Direct\n2)Aiirtel")
            a=int(input(":"))
            if a==1:
                w.dth()
            else:
                w.dth()
        elif b==4:
            w.mtn()
        elif b==5:
            w.mtc()
        elif b==6:
            print("NII Jeevan Anand Insurence")
            print("Your Insurence Amount Is:300")
            w.ins(amt=300)
        elif b==7:
            print("1)Flight\n2)Train\n3)Bus\n4)Hotel Booking")
            op=int(input(":"))
            a=input("leaving from:")
            b=input("Destination:")
            d=int(input("Number of passengers:"))
            p=input("Person name:")
            n=int(input("Number:"))
            if len(str(n))==10:
                print("Choose seat number from 1 to 40")


                for i in range(1,d+1):
                    q=int(input(F"{i})seat no:"))
                print("Available dates are")
                for i in range(1,6):
                    future=today+timedelta(days=i)
                    print(f"{i}) {future}")
                e=int(input("Choose any one:"))
                # l=future
                # print(l)
                if e==1 or e==2 or e==3 or e==4 or e==5:
                    # print("your amount is:")
                    # k = 0
                    # for i in range(4):
                    #     k = k * 10 + randint(1,9)
                    # print(k*d)
                    # c=(input("enter upi id:"))
                
                    if op==1:
                        w.flig()
                    elif op==2:
                        w.trai()
                    elif op==3:
                        w.bus()
                    elif op==4:
                        w.hote()
                else:
                    print("Wrong option")
        # elif b==8:
        #     w.rewar()
            else:
                print("Invalide Number Enter Valide Number")
        elif b==8:
            w.rewards()
        elif b==9:
            break
                
         
        
else:
    print("Wrong Possword")





