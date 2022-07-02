from geopy.geocoders import Nominatim
from geopy import distance 
import datetime as dt

geolocator = Nominatim(user_agent="geoapiExercises")

place1 =  input("Enter the source station: ")
place2 = input("Enter the destination: ")

p1 = geolocator.geocode(place1)
p2 = geolocator.geocode(place2)

# print(p1)
# print(p2)


lat1 , lon1 = (p1.latitude), (p1.longitude)
lat2 , lon2 = (p2.latitude), (p2.longitude)

l1 = (lat1,lon1)
l2 = (lat2,lon2)
# print(l1)
# print(l2)

dis = float(distance.distance(l1,l2).km)
distance = float("{:.2f}".format(dis))
# distance=int(distance)


cost = 0.0
age_m = []

x=int(input("Enter the number of Male passengers: "))

if x == 0:
    pass
else:
    for a in range(1,x+1):
        y=int(input("Enter the age of passengers: "))
        age_m.append(y)
    for a in age_m:
        if a>12 and a<=59:
            cost = cost + (0.75*distance)
        elif a>=6 and a<=12:
            cost = cost + (0.75*distance*50/100)
        elif a>=60:
            cost = cost + (0.75*distance*70/100)
        elif a<=5:
            cost = cost + 0        
        else:
            print("The given age is invalid !")

age_f = []

d=int(input("Enter the number of Female passengers: "))

if d == 0:
    pass
else:
    for b in range(1,x+1):
        y=int(input("Enter the age of passengers: "))
        age_f.append(y)
    for a in age_f:
        if a>12 and a<=59:
            cost = cost + (0.75*distance*70/100)
        elif a>=6 and a<=12:
            cost = cost + (0.75*distance*50/100)
        elif a>=60:
            cost = cost + (0.75*distance*70/100)
        elif a<=5:
            cost = cost + 0        
        else:
            print("The given age is invalid !")

cost = ("{:.2f}".format(cost))
now = dt.datetime.now()

print("\n\n\n\n########################################\n")

print(f"Date: {now.strftime('%d-%m-%Y')} Time: {now.strftime( '%H:%M:%S')}")
print(f"From: {place1.upper()}, To: {place2.upper()}")
print(f"Total number of passengers : {x+d}\nMale: {x}   Female: {d}")
print(f"{distance} kms.")
print(f"Total amount : {cost}.")

print("\n########################################\n\n")