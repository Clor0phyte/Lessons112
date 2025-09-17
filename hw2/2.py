n = int(input("Number:"))

temp = n        
reverse = 0 

while n>0:
    dig= n%10
    reverse = reverse*10 + dig
    n = n//101    
if temp==reverse:
        print(f"{temp} is palidrome")
else:
        print(f"{temp} is not palidrome")