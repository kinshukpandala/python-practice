r1, r2, r3 = 3, 5, 7

a1 = 3.14*r1**2
a2 = 3.14*r2**2
a3 = 3.14*r3**2

#to check the largerest area circle 

if r1>r2 and r1>r3:
    print(f"the circle whose radius is {r1} has the largest area")
elif r2>r1 and r2>r3:
    print(f"the circle with radius {r2} has the largest area")
else:
    print(f"The circle with radius {r3} has the largest radius ")

print(a1)
print(a2)
print(a3)
