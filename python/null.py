import math #to import math class


print("hello world")
print("iamharsh")

int,float
x=22
y=1.3
print(type(y))
print(type(x))

#program to swap to variables 
x,y=y,x
print(x)
print(y)
print(type(y))
print(type(x))

#java as a calculator  
f=x+y
g=x*8
l=y**x #use x as power to y
print(f)
print(math.pi) #to print value of pi
print(g)
print(l)
p=((x**y))
print(p)
w=11//5 # use // in division to get output in int datatype
print(w)

#other data types in python
s='null'  #string data type
print(type(s))

#python is a dynamic type launguage
s=22
print(type(s))
s=True
print(type(s))
print(id(s))  #to get info about location of data type


#string related functions
i="harsh"
print(i.capitalize()) #to capitalize first character of string
print(i.upper())
print(i.lower())
m="harsh"
n=" null"
print(n.strip())#to remove space from ends
print(len(m))
print("Hello\nWorld")
print(m.upper())
print(m.capitalize())
print(m+" "+n) #to combine to strings with a space
print(m+n)
print(4*m)
print(9*"null")

#some more advaced operation on string
#to print a character of specified location
print(m[2])
print(m[0:3])
print(m[2:4])

#boolean data type operations
x=3
y=5
print(x==5)#to check whether x is eqquals to 5 or not
print(x<y)#to compare xand y
print(x>y)#to compare y and x
print(x==y)
# Output: x == y is False
print(x!=y)
# Output: x != y is True
print(x>=y)
# Output: x >= y is False
print(x<=y)
# Output: x <= y is True

#1st if-else
w = 5.7
b = 33
if b>w:
    print("w is smaller than b")
else:
    print("w is greater than b")

#2nd if-else
a=10
b=17
if b<a:
   print("null ahahha")
else : print("gkjhsg")

#3rd if and else if
hu=98
ui=98
if ui>hu:
    print("ui is bda then hu")
elif ui<hu:
    print("sme h bskde") 
else:
    print("equal")   
     

#python snipett to take users choice
harsh=input("Enter string of your choice")
print(harsh)

print("hello world")
nam=input("Enter String or number of your choice")
print(nam)
print(nam*3)#use this type of method to print three times in a single line



#LOOPING IN python
#for loop in python

#program to print seperate characters of a string
r="iamharsh"
for i in r:
    print(i)

#to print even numbers between 0 and 10 using range 
for x in range(0,10,2):
    print(x)    

#while loop in python
#program to print numbers between 1 and 10
i=1
while i<10:
      print(i) 
      i+=1

 #syntax to add values to a list
lst=['1','3','4','7']
print(lst)

 #to print all the values stored in a list in a separate line
for i in lst:
    print(i)

#stores numbers from 1 to 100 in a list
fog=(range(1,100))
print(fog)

#to  print value in a list from position 80 till lst
print(fog[80:])
print(45 in fog)

fog.append(range(1,9821)) #use to add value to a exisitng list
print(fog)
print(len(fog))

