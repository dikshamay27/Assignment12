#Question 1 :   Name and handle the exception occured in the following program: 
#a=3
#if a<4:
#  a=a/(a-3)
#  print(a)
	 
	 
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)

except Exception as e:
    print(e)

	      
		  
#Question 2 :      Name and handle the exception occurred in the following program: 
#l=[1,2,3]
#print(l[3])


try:
    l=[1,2,3]
    print(l[3])#index 3 is out of range as l has max index 2

except Exception as e:
    print(e)


#Question 3 :       What will be the output of the following code:

 # Program to depict Raising Exception

#try:
#    raise NameError("Hi there")  # Raise Error
#except NameError:
#   print "An exception"
#    raise  # To determine whether the exception was raised or not

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise 



#following will the output of the given program :-

# raise NameError("Hi there")  # Raise Error
# NameError: Hi there


#Question 4 :       What will be the output of the following code:

 # Function which returns a/b
#def AbyB(a , b):
#	try:
#		c = ((a+b) / (a-b))
#	except ZeroDivisionError:
#		print "a/b result in 0"
#	else:
#		print c

# Driver program to test above function
#AbyB(2.0, 3.0)
#AbyB(3.0, 3.0)


def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#following will the output of the given program :-

# -5.0
# a/b result in 0


#Question 5 :    Write a program to show and handle following exceptions: 
#1. Import Error
#2. Value Error
#3. Index Error


#1. Import error

try:
    import sys
    import gw_utility.Book
except Exception as e:
    print(e)

#2.Value Errror

try:
    int("Hello Python")
	except Exception:
	    print("Value Error")

except ValueError as f:
    

#3. Index Error

l=[1,2,3,4,9,7]
try:
    print(l[10])
except Exception as e:
    print(e)


#Question 6 :   create a user defined exception AgeTooSmallError()that warns the user when they have entered age less than 18.type code must kep taking input
# till theuser enters the appro. age no.(lessthan18)

class AgeTooSmallError(Exception):
    pass
age=0
while age<18:
    age = int(input("Enter your age: "))
    try:
        if age<18:
            raise AgeTooSmallError("Age too small")
    except Exception as e:
        print(e)




          	   
