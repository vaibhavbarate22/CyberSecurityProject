#data types 
w=30
p ="vaibhav"
q='''vaibhav
kisan
barate
'''
d= 0.322
#variables
mini_1=30
mini2=20
mini22='vaibhav'
mini_22="vaibhav"
mini=0.322
#@mini=vaibhav "while namingh at the beggining only '_' and char are allowed"
# @ or symbols(special characters) is not allowed while naming
print(mini_1)
print(mini2)
print(mini22)
print(mini_22)
print(mini,"\n")
#operators
f = 1
g = 10+2
h = 22-21
i = 22/22
j = 22*1
k = 22-1+12/2*1.22
print(f)
print(g)
print(h)
print(i)
print(k,"\n")

#arithmetic operands
o=56
print()
f=13.4
c=f-f

b = 4
b==c
#b+=3-2/10*9
print(b)

b = True or False
# truth table of "OR"
print(True or True)
print(True or False)
print(False or False)
print(False or True,"\n")

# truth table of "AND"
print(True and True)
print(True and False)
print(False and False)
print(False and True,"\n")

#truth table of "NOT"
print(not(True))
print(not(False),"\n")


#type of variable
l=2>1
t=type(l)
print(t,"\n")

#typecasting 
y=int(input(": "))
u=str(y)
print(type(u),"\n")

#input 
ab=int(input("Enter input no.1 :"))
bc=int(input("Enter input no.2 :"))
print("printing no.1",ab)
print("printing no.2",bc,"\n")

#input + operands
ans=(ab+bc-ab*bc/y)
ans2=int(ans) #this method does not round off the output it directly remove the everything after '.'
#print(type(ans),ans)

#roudoff method
#ans2=round(ans)

print(ans2)
compare = ans2<bc
print(compare,"\n")


#finding square of a number 
print(ab*ab)
print(ab**2)
print("square",ab^2,"\n")#this not the right way to find the square of a number

'''
multi-line comment
'''
#average
print("average is :",(ab+bc)/2)