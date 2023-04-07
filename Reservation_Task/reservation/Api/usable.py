import datetime

#get current time
d = datetime.datetime.now()

#print date
print(d)

#get month name full version
print(d.strftime("%B"))