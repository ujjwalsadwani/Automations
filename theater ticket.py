import datetime as dt
a = dt.datetime.now()
b = a.strftime("%A")
b = b.lower()
c = a.strftime("%d-%m-%Y")
d = a.strftime("%H:%M:%S")
# print(b)
# print(c)
# print(d)
re=[]
pl=[]
gl=[]
sl=[]


Tickets=int(input("Enter the number of tickets: "))
if Tickets>30:
    print("\n\n*******************************\n\n")
    print("The number of seats cannot be more than 30 in a class.")
    print("\n\n*******************************\n\n")
else:
    cl=int(input("\nChoose the class:\n\t1.) Reckliner\n\t2.) Platinum\n\t3.) Gold\n\t4.) Silver\n\t"))

    cost=0
    if b != "tuesday" or "wednesday":
        if cl == 1:
            cost = 400*Tickets
        elif cl == 2:
            cost = 300*Tickets
        elif cl == 3:
            cost = 200*Tickets
        elif cl == 4:
            cost = 110*Tickets
        else:
            print("\n\n*******************************\n\n")
            print("Please choose a valid option.")
            print("\n\n*******************************\n\n")
            exit()
    else:
        if cl == 1:
            cost = 200*Tickets
        elif cl == 2:
            cost = 150*Tickets
        elif cl == 3:
            cost = 100*Tickets
        elif cl == 4:
            cost = 75*Tickets
        else:
            print("\n\n*******************************\n\n")
            print("Please choose a valid option.")
            print("\n\n*******************************\n\n")
            exit()

    def classes():
        if cl == 1:
            classM = "Reckliner"
        elif cl == 2:
            classM = "Platinum"
        elif cl == 3:
            classM = "Gold"
        elif cl == 4:
            classM = "Silver"
        return classM






    o= int(input("\nChoose the showtime:\n\t1.) 9:00 am - 12:00 pm\n\t2.) 12:00 pm - 3.00 pm\n\t3.) 3.00pm - 6.00 pm\n\t4.) 6.00 pm - 9.00 pm\n\t"))



    if o == 1:
        showtime = "Morning (9.00am-12.00pm)"
    elif o == 2:
        showtime = "Matinee (12.00pm-3.00pm)"
    elif o == 3:
        showtime = "Evening (3.00pm-6.00pm)"
    elif o == 4:
        showtime = "Night (6.00pm-9.00pm)"
    else:
        showtime="The given option was invalid !"
        
    print("\n\n*******************************\n\n")
    print(f"Date             : {c}\nTime             : {d}")
    print(f"Showtime         : {showtime}")
    print(f"Class            : {classes()}")
    print(f"Number of Tickets: {Tickets}")
    print(f"Total amount     : ₹ {cost}")
    print("\n\n*******************************\n\n")
