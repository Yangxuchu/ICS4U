
#diudshg
#1
def helloWorld():
    print ("Hello world!")
#2
def greet(a):
    print("Hello",a ,"!")
#3
def greet2():
    a=input("what is your name?")
    print ("Hello",a ,"!")
#4
def plus1(num):
    return num+1
#5
def max3(a,b,c):
   return max(a,b,c)
#6

#7
def sum(n):
    return sum(range(1,n))
#8
def strfirst(str):
    return str[0]
#9
def strhalf(str):
    return str[:len(str)//2]
#10
import random
def guessinggame():
    guesses=0
    number =random.randint(1, 7)
    a=input("guess a number from 1 to 7 pls. ")
    while True:
        guesses=guesses+1
        a=input("guess a number from 1 to 7 pls. ")
        if int(a) <number:
            print("should be highter")

        if int(a) >number:
            print("should be smaller")

        if int(a) == number:
            print ("you are corrcet!")
            break
    return guesses

#text cases
#1
helloWorld()
#2
greet("bob")
#3
greet2()
#4
print(plus1(0))
#5
print(max3(3,6,7))
#7
print(sum(4))
#8
print (strfirst("Jack"))
#9
print (strhalf("Barry"))
#10
guessinggame()













