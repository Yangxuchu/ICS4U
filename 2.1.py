
def is_odd(num):
    return bool(num % 2)

def canDiv57(x):
    return x % 5 == 0 and x % 7 == 0


def thirddigit7(x):
    return x // 100 % 10 == 7

print( thirddigit7(123756))


def getdigit(x,n):
    return x//(10 ** n) % 10

def ex4(x):

    a = getdigit(x,3)
    b = getdigit(x,2)
    c = getdigit(x,1)
    d = getdigit(x,0)
    print(a+b+c+d)
    print(d,c,b,a,sep="")
    print(d,a,b,c,sep="")
    print(a,c,b,d,sep="")

ex4(1234)

print(getdigit(1234,1))







    







