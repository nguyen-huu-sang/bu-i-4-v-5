## my script using the math module##
import mymath # note no .py
values = [2,4,6,8,10]
print('squares:')
for v in values:
    print (mymath.square(v))
print 'cubes:'
for v in values:
    print (mymath.cube(v))
print('average:'+ str(mymath.average(values))
