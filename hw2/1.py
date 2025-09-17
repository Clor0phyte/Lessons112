a = int(input("a:")) 
b = int(input("b:"))
c = int(input("c:"))

print(f"{a}x^2+{b}x+{c} = 0")

D = b**2 - 4*a*c 

g1 = (-b-(D**(1/2)))/(2*a)
g2 = (-b+(D**(1/2)))/(2*a)
g3 = (-b)/(2*a)

if D>0:
    print(f"x1 = {g1:.2}, x2 = {g2:.2}")
elif D==0:
    print(f"x = {g3:.2}")
else:
    print(f"no answer")