#1
def ex1():
    x=input("Enter a number")
    return float(x)
print(ex1())

#2


#3
def ex2(x):
    print("$",round(x,2), sep="")
    print(ex2(5.11546))

#4
def encode(x):
    y = ""
    for i in range(len(x)):
        y=y+chr(ord(x[i]-1))
        return y
    print(encode("bob"))





