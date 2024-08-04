import datetime
now = datetime.datetime.now()
#print(now.minute)
#print('{:0>2}{:0>2}'.format(now.hour,now.minute))
print(now.strftime("%H%M"))