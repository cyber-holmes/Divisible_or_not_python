#Goal;Check whether the given integer inputs are divisible to each other.

#Step1:Take input A.
a = input ("Enter the number: ")

#Step2:Take input B.
b = input ("Enter another number: ")

#Step3:Use conditional statement.
if a %b ==0 :#check a and b are divisible 
 print ("{} is divisible by {}").format(a,b)
elif a %b !=0 :#check a and b are not divisible
 print ("{} is not divisile by {}").format(a,b)
else :
 print ("Please check the number you have typed")
