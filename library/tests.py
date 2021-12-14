from django.test import TestCase

print(2**(3**2), (2**3)**2,)

def fn():
    x=50
    return x

fn()

l=[1,23,4]

m=map(lambda x: 2**x,l)
print(list(m))
import re
result= re.findall('Wel','Wel',1)
print(result)

y=[1,2,3]
y.sort()
print(y)

i='Welcome'

x = ['ab','cd']
print(list(map(len , x)))

a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print('dfsf',b)

print('WELcome to TUR'.capitalize())

z=set('abc')
z.add('san')
z.update(set(['p','q']))
print(z)

def add(c,k):
    c.test = c.test +1
    k=k+1

class Plus:
    def __init__(self):
        self.test=0


def  main():
    p=Plus()
    index=0
    for i in range(25):
        add(p,index)
    print("p.test", p.test)
    print("index-",index)

main()



