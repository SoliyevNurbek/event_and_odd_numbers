#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
#Print the number of even digits in the variable "var_int".
x=1234
k=0
if ((x%10)%2==0):
    k=k+1
if(((x//10)%10)%2==0):
    k=k+1
if(((x//100)%10)%2==0):
    k=k+1
if((x//1000)%2==0):
    k=k+1
print(k)