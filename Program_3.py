#Remove all characters except a
a = input("Enter a String : ")
b=""
for i in a:
    if i == 'a':
        b+=i
print("Original String : ",a)
print("Reduced String : ",b)