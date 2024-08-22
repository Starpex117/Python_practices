# ok so this excersices are from the web page Pynative, and i made this

#Exercise 1: Print First 10 natural numbers using while loop

x = 1
while(x < 11):
    print(x)
    x += 1
    


rows = 5
z = 1
for i in range(1, rows + 1):
    
    for j in range (1, i + 1):
        print(z, end= " ")
    print(" ")

for i in range(5):
    
    for j in range(3):
        print("*", end= " ")
    print()


numbers = [1, 2, 4, 6,]

pi_factor = [3.141516]

final = [i * j for i in numbers for j in pi_factor]
print(final)



