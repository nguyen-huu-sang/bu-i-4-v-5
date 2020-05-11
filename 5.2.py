import datetime as dt
fomat = '%y-%m-%dT%H:%M:%S'
t1= dt.datetime .strptime('2020-29-04T14:45:52',format)
print('day ' + str(t1.day))
print(month ' + str(t1.month))
print('minute ' + str(t1.minute))
print('sencond ' + str(t1.sencond))
      
# define todays and time
t2 = dt.datetime.now()
diff + t2 - t1
print('how many days difference ? ' + str(diff.days))
      
