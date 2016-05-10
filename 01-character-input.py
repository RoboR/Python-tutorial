import datetime

CURRENT_YEAR = datetime.date.today().year

name = raw_input("Your name: ")
age = int( raw_input("Your age: ") )

print (name + " will be 100 years old at year ", int(100 - age + 2016) )