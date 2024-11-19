import getpass #this is used to hide the input/confedential info like password

myname=getpass.getpass("Enter Your Name : ")

print('''''')

name = getpass.getpass("Enter Your  \U00002764 : ")

print('''''')

print(myname,"\U00002764",name,"\n") #this the normal way to print the name 

#print(f"{myname} \U00002764 {name} \n") #this is another way to use print using f-string

#chaining the functions


letter='''Dear <|Name|>
You are Going to \U00002764!
<|Name2|> \U00002764\U00002764'''

'''
print(letter.replace("<|Name|>","vaibhav").replace("<|Name2|>",""))
'''

Namee=getpass.getpass("First name \U00002764 : ")
print("\n")
namee2=getpass.getpass("second name \U00002764 : ")
print("\n")
letter2=f''''dear {Namee}
you are \U00002764 of 
{namee2}
'''

print(letter2.replace(f"{Namee}",f"{name}").replace(f"{namee2}",f"{myname}"))

print(("index is : "),letter.find("v"))

#print(letter.replace(" ","   ")) #this doesn't change the original string bcaz Strings are Immutable
#it create another string with the changes



print("\U00002764\U00002764\U00002764\U00002764")#hex code for the em.
