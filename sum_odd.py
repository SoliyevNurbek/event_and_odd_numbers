#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_odd" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
x=1234
k=0
if ((x%10)%2==1):
    k=k+(x%10)
if(((x//10)%10)%2==1):
    k=k+((x//10)%10)
if(((x//100)%10)%2==1):
    k=k+((x//100)%10)
if((x//1000)%2==1):
    k=k+(x//1000)
print(k)