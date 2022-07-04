# calculate the biorhythm value for today and the days around it
# see: http://en.wikipedia.org/wiki/Biorhythm
# tested with Python24      vegaseat     15may2006

import datetime
from math import sin

def getBiorhythm(zd):
    """
    returns the three biorhythm values, given the days since birth zd
    50 is center value, higher values are better
    """
    pi = 3.14159
    zd = int(zd)
    physical = int(50 * (1 + sin((zd / 23.0 - int(zd / 23)) * 360 * pi / 180)))
    emotion = int(50 * (1 + sin((zd / 28.0 - int(zd / 28)) * 360 * pi / 180)))
    intellect = int(50 * (1 + sin((zd / 33.0 - int(zd / 33)) * 360 * pi / 180)))
    return physical, emotion, intellect

print("This program calculates your biorhythm values based on your age in days.")
print("The values for a seven day period are given, with today in the center.")
print("This allows you to see, if you are in a decreasing or increasing cycle.")
print()

bd = input("Enter your birthday (format = mm/dd/yyyy): ")

# split the string into month, day, year
dL = bd.split("/")

# convert to format datetime.date(year, month, day))
birthday = datetime.date(int(dL[2]), int(dL[0]), int(dL[1]))

# get todays date
today = datetime.date.today()

# calculate age in days since birth
age = (today - birthday).days

p = []  # physical well-being list over range of 7 days
e = []  # emotional well-being list over range of 7 days
i = []  # intellectual well-being list over range of 7 days

for ax in range(age-3, age+4):
    px, ex, ix = getBiorhythm(ax)
    p.append(px)
    e.append(ex)
    i.append(ix)

print("-"*58)

print("Birthday     =", birthday.strftime("%d%b%Y"))
print("Today        =", today.strftime("%d%b%Y"))
print("Age in days  =", age)

print("-"*58)

print("Here are your biorhythm values (higher values best):")
print("Days from today %5s %5s %5s %5s %5s %5s %5s" % ('-3', '-2', '-1', '0', '+1', '+2', '+3'))
print("Physical     :  %5d %5s %5s %5s %5s %5s %5s" % (p[0], p[1], p[2], p[3], p[4], p[5], p[6]))
print("Emotional    :  %5d %5s %5s %5s %5s %5s %5s" % (e[0], e[1], e[2], e[3], e[4], e[5], e[6]))
print("Intellectual :  %5d %5s %5s %5s %5s %5s %5s" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

print("-"*58)