#String Slicing 
print('''''')
name=input("Enter your string : ")
print("\n")
nameshort=len(name)
print("Length :",nameshort,"\n")

nameshort2=name[2:]
print("Negative Slicing :",nameshort2,"\n")

nameshort3=name[:-1]
print("Negative Slicing :",nameshort3,"\n")

nameshort4=name[1:10:2]#this is the method that uses [index start : index end : skip value]
print("String slicing with skip func. :",nameshort4,"\n")

#startswith
print("Startswith Result :",name.startswith("v"),"\n") #this func. is case sensitive

#endswith function
print("Endswith result :",name.endswith("a"),"\n") #case sensitive function

#capitalize Function
print("Capitalize Function : ",name.capitalize(),"\n")

#Count Function 
print("Character occured : ",name.count("v"),"\n") #this function count the occurence of the character in the string

#find function
print("Index of the occurance : ",name.find("barate"),"\n") #it returns the index of the given word when it first occured

'''
#Diffrent '\' characters
\n - is a new line character
\t - is a tab space character
\" & \' - it will print double quote & single quote with other text
\\ - it is used to print the blackslash it-self
'''