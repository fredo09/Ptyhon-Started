## CICLOS FOR WHILE

# for
print("For")
primos = [2,3,5,7]
for primo in primos:
    print (primo)

#range() con for
print("for con range()")
for x in range(10):
    print ('mi valor: %s' % x )

#while
print ("while")
count = 0
while count < 5 :
    print (count)
    count +=1

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
print("Uso del break, continue")
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
print("Uso del else")
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")