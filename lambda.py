
#lambda functions in python

#normal functions
def add(a,b):
    return a+b

print(add(2,3))

#using lambda function

addition = lambda x,y : x+y
print(addition(2,3))

def apply(fx,value):
    return 6+ fx(value)

print(apply(lambda x :x*2, 2))