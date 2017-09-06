ITEM=["Chole bhature\n","Pavbhaji\n","Aloo tikki\n","Samosa\n","Raj kachauri\n","Plain dosa\n","Masala dosa\n","Uttapam\n","Idli\n","Vada\n","Burger\n","Sandwich\n","Pizza\n","French fries\n","Momos\n","Fried chicken\n","Chicken curry\n","Fish fry\n","Fish curry\n","Butter chicken\n"]

PRICE=["60\n","50\n","30\n","12\n","12\n","20\n","30\n","35\n","20\n","25\n","25\n","15\n","150\n","45\n","40\n","200\n","250\n","275\n","195\n","350\n"]
d=open("ITEM.txt","w")
e=open("PRICE.txt","w")
d.writelines(ITEM)
e.writelines(PRICE)
d.close()
e.close()
class canteen:
    def __init__(self,code="0",q=0):
        self.q=q
        self.code=code
    def stockdisplay(self):
        d=open("ITEM.txt","r")
        f=d.readlines()
        print"\t"*3,
        print"ITEM:",f[self.code-1]
        print "\t"*3,
        print "Quantity:",self.q
    def total(self):
        print "\t"*3,
        print "Total Price:",int(p[self.code-1])*self.q
    def stockenter(self):
        print "\t"*3
        print "Enter item details"
        print "\t"*3,
        self.code=input("Enter code:")
        print "\t"*3
        self.q=input("Enter quantity:")

c=canteen()

a="y"
g=0
l=[]
x=[]
o=[]
while a=="y":
    print "     MENU"
    print "   Enter 1 for vegetarian"
    print "   Enter 2 for non vegetarian"
    print "\t"*3,
    choice=input("Enter option:")
    if choice==1:
        print"\n"*2,
        print"     Vegetarian menu"
        print"\n",
        print"     Enter 1 for north indian"
        print"     Enter 2 for south indian"
        print"     Enter 3 for snacks"
        print"\t"*3,
        ch=input("Enter option:")
        if ch==1:
            print"\t",
            print"     North indian"
            print"\n",
            print"\t",
            print "code    Item       Price"
            print "\n",
            print "\t",
            print "1.   Chole Bhature    60"
            print "\t",
            print "2.   Pavbhaji       50"
            print "\t",
            print "3.   Aloo Tikki      30"
            print "\t",
            print "4.   Samosa       12"
            print "\t",
            print "5.   Raj kachauri    12"
            c.stockenter()
        elif ch==2:
            print "\t",
            print "       South indian"
            print "\n",
            print "\t",
            print "code   Item       Price"
            print "\n",
            print "\t",
            print "6.    Plain dosa    20"
            print "\t",
            print "7.    Masala dosa    30"
            print "\t",
            print "8.    Uttapam        35"
            print "\t",
            print "9.      Idli        20"
            print "\t",
            print "10.     Vada        25"
            c.stockenter()
        elif ch==3:
            print "\t",
            print "        Snacks"
            print "\n",
            print "\t",
            print "code     Item      Price"
            print "\n",
            print "\t",
            print "11.      Burger     25"
            print "\t",
            print "12.      Sandwich    15"
            print "\t",
            print "13.      Pizza       150"
            print "\t",
            print "14.    French fries   45"
            print "\t",
            print "15.      Momos        40"
            c.stockenter()
        else:
            print "Wrong input"
    elif choice==2:
        print "\t",
        print "         Non-Vegetrian"
        print "\n",
        print "\t",
        print "code       Item        Price"
        print "\n",
        print "\t",
        print "16.     Fried chicken    200"
        print "\t",
        print "17.      Chicken curry    250"
        print "\t",
        print "18.      Fish fry       275"
        print "\t",
        print "19.      Fish curry     195"
        print "\t",
        print "20.    Butter chicken    350"
        c.stockenter()
    else:
        print "Wrong Input"
    e=open("PRICE.txt","r")
    d=open("ITEM.txt","r")
    p=e.readlines()
    z=d.readlines()
    g+=(int(p[c.code-1])*c.q)
    y=int(p[c.code-1])*c.q
    o.append(y)
    l.append(z[c.code-1])
    print l
    x.append(c.q)
    print x
    c.stockdisplay()
    c.total()
    print "\t"*3,
    s=raw_input("Want to enter more or not:")
    if s.upper()=='Y':
        a="y"
    else:
        break
print "\n"*3,
w=len(l)
print "ITEM:",
for i in range(w):
    print "\t"*3
    print i+1,".",l[i]
print "Quantity:",
for i in range(w):
    print "\t"*3
    print x[i]
print "Price:",
for i in range(w):
    print "\t"*3
    print i+1,".",o[i]
print "Total price:",g
